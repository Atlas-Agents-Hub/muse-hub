---
name: dpo-guide
description: "Align language models with human preferences using Direct Preference Optimization — no reward model, no RL loop."
---

# Direct Preference Optimization

## Working setup

Use the files, project settings, and connected tools available for this task. Read the relevant reference before changing an unfamiliar API or format. Run included commands from this skill folder, using the project's actual inputs.

## When to use

- Preference-tuning a model when you lack the infrastructure or appetite for a full
  PPO pipeline.
- Fine-tuning open models on human or AI-generated preference pairs for style,
  helpfulness, or safety.
- Rapid iteration on alignment behavior: DPO trains in hours, letting you test
  data and hyperparameter changes quickly.
- Distilling preferences from a stronger model (generate pairs, have the strong
  model judge, DPO-tune the smaller one).
- As the final stage after SFT in a standard post-training recipe.
- Small teams and researchers who need preference tuning without RL expertise.

## Core concepts

- **The DPO loss**: for each triple, the loss pushes up log π(chosen)/π_ref(chosen)
  − log π(rejected)/π_ref(rejected), passed through a sigmoid scaled by β.
  Intuitively: make the good answer relatively more likely than the bad one,
  without drifting far from the reference model.
- **β (beta)**: the temperature controlling how strongly preferences reshape the
  policy. Low β → aggressive updates, risk of overfitting to pairs. High β →
  conservative, stays near the reference. Typical starting range: 0.1–0.5.
- **Reference model**: usually the SFT checkpoint you started from, kept frozen.
  The KL-to-reference term is what prevents collapse — don't skip it by using a
  mismatched reference.
- **Implicit reward**: DPO never materializes a reward function, but you can read
  one off: r(x,y) = β·log(π(y|x)/π_ref(y|x)). Useful for debugging which pairs the
  model "believes."
- **On-policy vs. off-policy**: DPO is off-policy — it learns from fixed pairs. If
  the policy drifts far from the data distribution, the implicit reward
  extrapolates badly. Iterative DPO (re-collect pairs from the current policy)
  fixes this at the cost of complexity.
- **Variants**: IPO (adds regularization against overfitting to deterministic
  preferences), KTO (works with binary good/bad labels instead of pairs), ORPO
  (merges SFT and preference objectives, no reference model needed), SimPO
  (reference-free with length normalization).
- **Pair quality**: the entire method hinges on what distinguishes chosen from
  rejected. Informative pairs differ on the target behavior; noisy pairs teach
  noise.
- **Length dynamics**: like all preference methods, DPO can learn "longer is
  better" if chosen responses are systematically longer. Watch output length as a
  training metric.

## Practical workflow

1. **Prepare preference triples.** (prompt, chosen, rejected). Chosen and rejected
   should be genuinely comparable — pairs where one is obviously garbage teach the
   model nothing about the decision boundary you care about.
2. **Audit pair quality.** Sample 100+ pairs manually. Check: does the chosen
   response actually demonstrate the desired behavior? Is the rejected one wrong in
   the relevant way, not just worse overall?
3. **Start from a good SFT model.** DPO refines; it doesn't create capabilities.
   The reference model is this SFT checkpoint.
4. **Set hyperparameters.** Learning rate ~5e-7 to 1e-6 (lower than SFT),
   β ≈ 0.1–0.5, 1–3 epochs. Watch the implicit reward margin: it should grow
   steadily, not explode.
5. **Train and monitor.** Track: loss, reward margin (chosen − rejected implicit
   reward), output length, and — critically — win-rate on a held-out eval judged
   by humans or a strong judge model. Also track KL from reference; a collapsing
   KL with rising margin means overfitting.
6. **Evaluate on behavior, not loss.** Run your safety and quality evals. Check
   for the classic DPO pathologies: verbosity increase, sycophancy, and degraded
   performance on tasks absent from the preference data.
7. **Iterate on data.** If a behavior isn't changing, the pairs probably don't
   isolate it. Add targeted pairs for that specific behavior rather than more
   generic data.

Checklist for a DPO run:
- SFT baseline evaluated before starting, so you can measure the delta.
- Pair quality audited manually on a sample.
- Held-out preference accuracy improves without KL collapse.
- Human or strong-judge win-rate confirms the improvement is real.
- Capability benchmarks (reasoning, knowledge) haven't regressed.
- Output length monitored for verbosity drift.

## Common pitfalls

- **Garbage pairs.** DPO amplifies whatever distinguishes chosen from rejected. If
  chosen responses are just longer, you train a verbosity maximizer. Audit pair
  quality first.
- **β too low.** The policy overfits to the pairs, producing extreme probability
  shifts and degenerate outputs on anything slightly off-distribution.
- **Too many epochs.** DPO overfits fast — often 1 epoch is enough. More epochs
  rarely help and frequently hurt.
- **Mismatched reference.** Using a different checkpoint as reference than the one
  training started from breaks the KL anchoring the theory relies on.
- **Expecting exploration.** DPO can't discover behaviors absent from the data. If
  no pair demonstrates the desired behavior, DPO won't invent it — that's a data
  problem, not a hyperparameter problem.
- **Judging by loss alone.** Training loss decreasing while human-judged quality
  flatlines is common. Always keep an independent behavioral eval.
- **Ignoring length.** Not tracking output length during training, then wondering
  why the model rambles. Length is a first-class metric here.
- **One big undifferentiated dataset.** Mixing safety pairs, style pairs, and
  helpfulness pairs without tracking which behavior each subset drives. When
  something goes wrong, you can't attribute it.

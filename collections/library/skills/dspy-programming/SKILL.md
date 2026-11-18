---
name: dspy-programming
description: "Program language models instead of prompting them — DSPy signatures, modules, and optimizers that tune prompts automatically."
---

# DSPy Programming

## Working setup

Use the files, project settings, and connected tools available for this task. Read the relevant reference before changing an unfamiliar API or format. Run included commands from this skill folder, using the project's actual inputs.

## When to use

- Any multi-step LLM pipeline where you're currently hand-tuning prompts and want
  systematic improvement.
- When you have a clear success metric and some labeled examples — the optimizer
  needs both.
- Building RAG, classification, extraction, or agent pipelines you expect to
  maintain as models change (recompile for a new model instead of rewriting
  prompts).
- Teams where prompt changes need to be reviewable and reproducible rather than
  tribal knowledge.
- Research on prompt optimization itself.
- Porting a pipeline to a new model: recompile instead of rewriting prompts by
  hand.

## Core concepts

- **Signatures**: declarative specs of a step's behavior — `context, question ->
  answer` plus a natural-language instruction. Signatures say what, not how; the
  optimizer figures out the how.
- **Modules**: composable building blocks — Predict (basic), ChainOfThought (adds
  reasoning), ReAct (tool loop), and custom modules you write. Modules compose
  into programs; programs are the unit of optimization.
- **Teleprompters (optimizers)**: BootstrapFewShot (generate candidate
  demonstrations from your training set, keep the ones that work), MIPRO (jointly
  optimizes instructions and demonstrations, the strongest default), and others.
  They need: a training set, a metric function, and a validation set.
- **Metrics**: the objective function — exact match, F1, LLM-judge score,
  task-specific checks. The optimizer will ruthlessly maximize whatever you give
  it; a bad metric produces "optimized" prompts that game the metric.
- **Assertions/suggestions**: runtime constraints on module outputs (e.g., "answer
  must be valid JSON") with automatic retry. Cheaper than hoping the prompt
  holds.
- **Compilation**: running the optimizer produces a compiled program — optimized
  prompts + demonstrations baked in. Compile per model; a program optimized for
  one model often underperforms on another without recompiling.
- **Training/validation split**: the optimizer trains on one set and must be
  validated on another. Optimized prompts overfit the training examples otherwise.
- **Custom modules**: when built-ins don't fit, write your own module class with
  a forward method. The optimizer still works — it optimizes whatever structure
  you give it.

## Practical workflow

1. **Define the metric first.** Write the scoring function before any DSPy code.
   Test it on sample outputs — if it doesn't match your judgment of quality, fix
   it now.
2. **Decompose into signatures.** Break the task into steps; write one signature
   per step with clear field names and instructions. Start with the simplest
   module per step (Predict, then ChainOfThought where reasoning helps).
3. **Assemble a training set.** 50–200 labeled examples representative of the
   task. Quality and coverage matter more than size — the optimizer learns
   demonstrations from these.
4. **Hold out validation data.** Split before optimizing. The validation set is
   sacred — never let the optimizer see it.
5. **Run a teleprompter.** Start with BootstrapFewShot for speed; move to MIPRO
   for the final optimization. Validate on the held-out set — optimized prompts
   can overfit the training examples.
6. **Inspect what the optimizer found.** Read the generated demonstrations and
   instructions. Sometimes they're insightful; sometimes they reveal metric
   gaming. Either way, look.
7. **Compile and version.** Save the compiled program; recompile when switching
   models or when the task distribution shifts. Treat compilation as part of your
   build, not a one-off.

Checklist for a DSPy program:
- Metric validated against human judgment on samples.
- Held-out validation set separate from optimizer training data.
- Compiled program inspected, not just scored.
- Recompilation plan for model changes.
- Module decomposition justified (no over-decomposition).

## Common pitfalls

- **Metric gaming.** The optimizer is an adversary against your metric. Vague
  metrics ("quality score 1-5 from an LLM judge") get exploited. Make metrics
  specific and check optimized outputs manually.
- **Tiny training sets.** Optimizing on 10 examples finds prompts that memorize
  those 10. Use enough examples to represent the task's variety.
- **Skipping the held-out set.** Training-set scores after optimization are
  meaningless. Always validate on unseen data.
- **Over-decomposition.** Ten signatures where three would do gives the optimizer
  ten places to overfit and you ten places to debug. Start coarse.
- **Never inspecting compiled prompts.** The optimizer sometimes finds
  bizarre-but-effective prompts. If you can't understand why it works, you can't
  trust it in production — simplify or constrain.
- **One compilation forever.** Models update, data drifts. Recompile on a schedule
  or when metrics degrade, like retraining any model.
- **Optimizing the wrong module.** Spending optimizer budget on a step that
  contributes 5% of errors while the 80% step stays hand-written. Profile errors
  per module first.
- **Metric–judgment mismatch.** The metric says 95%, your eyes say the outputs
  are bad. Trust your eyes; fix the metric; recompile.

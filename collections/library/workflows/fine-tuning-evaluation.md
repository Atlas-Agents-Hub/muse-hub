# Fine-Tune and Evaluate a Model

Improve a model on a defined task while keeping evaluation independent of training.

## Bring these inputs

- Training examples and permitted use
- Held-out tasks, baseline model, and compute budget

## 1. Data Labeling

Read [the Data Labeling method](../skills/data-labeling/SKILL.md). Define the labels or response rubric and review ambiguous examples.

**Carry forward:** A versioned dataset with labeling rules and held-out split.

**Check:** Labels follow the rubric and duplicates do not cross the split.

## 2. Fine Tuning

Read [the Fine Tuning method](../skills/fine-tuning-expert/SKILL.md). Choose and run the training method within the compute budget.

**Carry forward:** A model checkpoint, training configuration, and loss history.

**Check:** Training stays within budget and the checkpoint can be loaded reproducibly.

## 3. Agent Regression Evaluation

Read [the Agent Regression Evaluation method](../skills/agent-regression-evals/SKILL.md). Compare the checkpoint with the baseline on the held-out tasks.

**Carry forward:** A paired evaluation report and deployment recommendation.

**Check:** Measured improvement and regressions are reported with appropriate uncertainty.

## Check the finished work

- Labels follow the rubric and duplicates do not cross the split.
- Training stays within budget and the checkpoint can be loaded reproducibly.
- Measured improvement and regressions are reported with appropriate uncertainty.

## Finish

A paired evaluation report and deployment recommendation. Measured improvement and regressions are reported with appropriate uncertainty.

## Tools for this workflow

Read [the included tool guides](../../../docs/tools/README.md) when a stage calls for those tools.

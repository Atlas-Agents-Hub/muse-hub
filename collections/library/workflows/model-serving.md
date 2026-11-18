# Serve a Model Efficiently

Choose a serving configuration from measured latency, throughput, and cost.

## Bring these inputs

- Model and representative workload
- Latency target and resource budget

## 1. Machine Learning Pipelines

Read [the Machine Learning Pipelines method](../skills/ml-pipeline/SKILL.md). Define the model artifact, preprocessing, version, and serving input contract.

**Carry forward:** A versioned deployment artifact and request contract.

**Check:** The serving inputs reproduce the evaluated preprocessing and model version.

## 2. Vllm Serving

Read [the Vllm Serving method](../skills/vllm-serving/SKILL.md). Benchmark serving configurations against the representative workload.

**Carry forward:** Latency, throughput, memory, and error measurements.

**Check:** Measurements include warm-up, concurrency, and the relevant sequence lengths.

## 3. LLM Cost Optimizer

Read [the LLM Cost Optimizer method](../skills/llm-cost-optimizer/SKILL.md). Compare the benchmarked configurations using actual provider or hardware costs.

**Carry forward:** A costed serving choice and operating limits.

**Check:** The selected configuration meets the target and its prices have an as-of date.

## Check the finished work

- The serving inputs reproduce the evaluated preprocessing and model version.
- Measurements include warm-up, concurrency, and the relevant sequence lengths.
- The selected configuration meets the target and its prices have an as-of date.

## Finish

A costed serving choice and operating limits. The selected configuration meets the target and its prices have an as-of date.

## Tools for this workflow

Read [the included tool guides](../../../docs/tools/README.md) when a stage calls for those tools.

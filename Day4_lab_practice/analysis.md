# Day 4 Lab: Will It Fit, and May I Use It?

## 1. Objective

The objective of this experiment is to estimate the memory required to run local language models and understand how model size, quantization, and context length affect memory usage.

## 2. System and Memory Budget

- Operating system: Windows 11
- Python environment: Existing Day1 practice virtual environment
- Memory budget used in the estimator: 11.0 GB
- Important note: The 11.0 GB budget is provisional. Actual available GPU VRAM and system RAM must be checked separately.

## 3. Memory Estimation Formula

- Weights (GB) = Parameters (billions) × Bytes per parameter
- KV cache (GB) = Parameters (billions) × Context length (in K tokens) × 0.02
- Total estimated memory (GB) = (Weights + KV cache) × 1.10

The additional 10% accounts for estimated overhead.

## 4. Model Configuration Results

| Model configuration | Weights (GB) | KV cache (GB) | Total (GB) | Estimator result |
|---|---:|---:|---:|---|
| 1.5B Q4 | 0.85 | 0.24 | 1.20 | Fits comfortably |
| 8B Q4 | 4.56 | 1.28 | 6.42 | Fits comfortably |
| 8B FP16 | 16.00 | 1.28 | 19.01 | Does not fit |
| 30B Q4 | 17.10 | 4.80 | 24.09 | Does not fit |
| 70B Q4 | 39.90 | 11.20 | 56.21 | Does not fit |

## 5. Context Length Experiment

For an 8B Q4 model, increasing the context length increases the estimated KV cache requirement.

| Context length | Total estimated memory (GB) | Estimator result |
|---|---:|---|
| 4K | 5.72 | Fits comfortably |
| 8K | 6.42 | Fits comfortably |
| 16K | 7.83 | Fits, but tight |
| 32K | 10.65 | Fits, but tight |
| 128K | 27.54 | Does not fit |

**Observation:** A longer context allows the model to process more text, but it requires more memory for the KV cache.

## 6. Quantization Experiment

For an 8B model using an 8K context:

| Precision | Total estimated memory (GB) | Estimator result |
|---|---:|---|
| Q3_K_M | 5.19 | Fits comfortably |
| Q4_K_M | 6.42 | Fits comfortably |
| Q5_K_M | 7.39 | Fits comfortably |
| Q6_K | 8.54 | Fits, but tight |
| Q8_0 | 10.21 | Fits, but tight |
| FP16 | 19.01 | Does not fit |

**Observation:** Lower-bit quantization reduces estimated memory usage. Higher precision generally preserves more numerical information but requires more memory.

## 7. Understanding Model Licences

A model's availability for download does not automatically mean it is unrestricted or open-source.

Before selecting a model, check its official model card and licence for:

- Whether commercial use is permitted.
- Attribution or redistribution requirements.
- Acceptable-use restrictions.
- Tool-calling support.
- Model download size and hardware requirements.

## 8. Actual Ollama Verification

This section must be completed using the actual output from my computer.

Commands used:

```powershell
ollama list
ollama ps
```

- Installed models: [Fill in from `ollama list`]
- Model currently loaded: [Fill in from `ollama ps`]
- Actual model size: [Record the displayed size]
- Estimated memory compared with actual usage: [Complete after checking]

The estimator gives approximate memory requirements. Actual usage can differ because of model architecture, runtime overhead, context settings, and whether the model uses the GPU or system RAM.

## 9. Conclusion

The experiment demonstrates that model size, quantization, and context length influence memory requirements. A smaller quantized model is a practical starting point for local experiments on a memory-limited computer. Before choosing a model, I should verify its actual hardware requirements, licence, commercial-use conditions, and capabilities.

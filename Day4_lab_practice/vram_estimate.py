
"""Day 4: Estimate model memory requirements."""

BYTES_PER_PARAM = {
    "FP16": 2.00,
    "Q8_0": 1.00,
    "Q6_K": 0.81,
    "Q5_K_M": 0.68,
    "Q4_K_M": 0.57,
    "Q3_K_M": 0.43,
}

KV_GB_PER_B_PER_1K = 0.02
OVERHEAD = 1.10

# Estimated available memory budget in GB.
# Change this after confirming the memory available for your model.
AVAILABLE_GB = 11.0


def estimate(params_b, precision="Q4_K_M", context_k=8):
    if params_b <= 0 or context_k <= 0:
        raise ValueError("Parameters and context must be positive.")

    if precision not in BYTES_PER_PARAM:
        raise ValueError("Unsupported precision.")

    weights_gb = params_b * BYTES_PER_PARAM[precision]
    kv_gb = params_b * context_k * KV_GB_PER_B_PER_1K
    total_gb = (weights_gb + kv_gb) * OVERHEAD

    return weights_gb, kv_gb, total_gb


def verdict(total_gb, available_gb):
    if total_gb <= available_gb * 0.7:
        return "Fits comfortably"
    elif total_gb <= available_gb:
        return "Fits, but tight"
    return "Does NOT fit"


def report(name, params_b, precision, context_k):
    weights, kv, total = estimate(params_b, precision, context_k)

    print(
        f"{name:<20} | {precision:<7} | "
        f"{params_b:>5.1f}B | Context {context_k:>3}K | "
        f"Weights {weights:>6.2f} GB | KV {kv:>6.2f} GB | "
        f"Total {total:>6.2f} GB | "
        f"{verdict(total, AVAILABLE_GB)}"
    )


if __name__ == "__main__":
    print(f"Available memory budget: {AVAILABLE_GB:.1f} GB")

    print("\n1. Model configurations")
    report("Qwen small", 1.5, "Q4_K_M", 8)
    report("8B model Q4", 8, "Q4_K_M", 8)
    report("8B model FP16", 8, "FP16", 8)
    report("30B model Q4", 30, "Q4_K_M", 8)
    report("70B model Q4", 70, "Q4_K_M", 8)

    print("\n2. Different context lengths for an 8B Q4 model")
    for context in (4, 8, 16, 32, 128):
        report("8B context test", 8, "Q4_K_M", context)

    print("\n3. Different quantizations for an 8B model")
    for precision in ("Q3_K_M", "Q4_K_M", "Q5_K_M",
                      "Q6_K", "Q8_0", "FP16"):
        report("8B quant test", 8, precision, 8)

#!/usr/bin/env python3
"""Compute bootstrap 95% CIs for headline ASR / bench numbers.

We use an independent-Bernoulli model: ASR is a fraction of n trials
where each trial is bench/attack success/failure. Resample with
replacement (B=10000), report 2.5%-97.5% percentile band.

Sources:
  - data/idea3_defense_qwen7b_L24_excess.json  (n=100 per lambda)
  - data/idea3_defense_L22_excess.json         (n=100 per lambda)
  - data/idea3_defense_L24_excess.json
  - data/idea3_defense_llama8b_L20_excess.json (n=100 per lambda)
  - data/idea3_per_attack_qwen7b.json          (n=12 per attack)
"""
import os
import json
import numpy as np

DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
B = 10000
rng = np.random.default_rng(20260427)


def boot_ci(asr_frac: float, n: int, b: int = B) -> tuple[float, float]:
    """Bootstrap CI for a binomial proportion."""
    k = int(round(asr_frac * n))
    samples = rng.binomial(n, k / n if n else 0, size=b) / n
    lo, hi = np.percentile(samples, [2.5, 97.5])
    return lo, hi


def fmt_pct(x: float) -> str:
    return f"{100 * x:.1f}\\%"


def main():
    print("=== Defense ASR / bench, with bootstrap 95% CI (B=10000) ===\n")
    for f, label in [
        ("idea3_defense_qwen7b_L24_excess.json", "Qwen-7B @ L24"),
        ("idea3_defense_L22_excess.json",        "Qwen-1.5B @ L22"),
        ("idea3_defense_L24_excess.json",        "Qwen-1.5B @ L24"),
        ("idea3_defense_llama8b_L20_excess.json","Llama-3.1-8B @ L20 (null)"),
    ]:
        path = os.path.join(DATA, f)
        if not os.path.exists(path):
            continue
        d = json.load(open(path))
        n = next(iter(d["defense"].values())).get("n", 100)
        print(f"-- {label} (n={n}) --")
        print(f"{'lam':>4}  {'ASR':>5}  {'95% CI':>14}  {'bench':>6}  {'95% CI':>14}")
        for lam, r in sorted(d["defense"].items(), key=lambda x: float(x[0])):
            a_lo, a_hi = boot_ci(r["asr"], n)
            b_lo, b_hi = boot_ci(r["bench"], n)
            print(f"{lam:>4}  {fmt_pct(r['asr']):>5}  [{fmt_pct(a_lo)}, {fmt_pct(a_hi)}]  "
                  f"{fmt_pct(r['bench']):>6}  [{fmt_pct(b_lo)}, {fmt_pct(b_hi)}]")
        print()

    # Per-attack
    pa = json.load(open(os.path.join(DATA, "idea3_per_attack_qwen7b.json")))
    print(f"-- per-attack (Qwen-7B L24 lam={pa['lam']}) --")
    print(f"{'attack':<55}  {'baseline (CI)':>20}  {'defended (CI)':>20}")
    for r in pa["rows"]:
        if r["base_asr"] == 0:
            continue
        bn = r["n"]
        b_lo, b_hi = boot_ci(r["base_asr"], bn)
        d_lo, d_hi = boot_ci(r["def_asr"], bn)
        text = (r["attack_text"][:50] + "..") if len(r["attack_text"]) > 52 \
               else r["attack_text"]
        print(f"{text:<55}  "
              f"{fmt_pct(r['base_asr'])} [{fmt_pct(b_lo)}, {fmt_pct(b_hi)}]    "
              f"{fmt_pct(r['def_asr'])} [{fmt_pct(d_lo)}, {fmt_pct(d_hi)}]")

    # Save a JSON with CIs for paper insertion
    out = {
        "method": f"bootstrap percentile, B={B}",
        "seed": 20260427,
        "qwen7b_L24": {},
        "qwen15b_L22": {},
        "qwen15b_L24": {},
        "llama8b_L20": {},
    }
    for f, key in [
        ("idea3_defense_qwen7b_L24_excess.json", "qwen7b_L24"),
        ("idea3_defense_L22_excess.json",        "qwen15b_L22"),
        ("idea3_defense_L24_excess.json",        "qwen15b_L24"),
        ("idea3_defense_llama8b_L20_excess.json","llama8b_L20"),
    ]:
        path = os.path.join(DATA, f)
        if not os.path.exists(path):
            continue
        d = json.load(open(path))
        n = next(iter(d["defense"].values())).get("n", 100)
        for lam, r in d["defense"].items():
            a_lo, a_hi = boot_ci(r["asr"], n)
            b_lo, b_hi = boot_ci(r["bench"], n)
            out[key][lam] = {
                "n": n,
                "asr": r["asr"], "asr_ci95": [a_lo, a_hi],
                "bench": r["bench"], "bench_ci95": [b_lo, b_hi],
            }
    json.dump(out, open(os.path.join(DATA, "bootstrap_ci.json"), "w"), indent=2)
    print(f"\nSaved CI summary to data/bootstrap_ci.json")


if __name__ == "__main__":
    main()

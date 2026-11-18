# Data Quality Concepts Reference

Deep-dive reference for the Data Quality Auditor skill. Keep SKILL.md lean — this is where the theory lives.

---

## Missingness Mechanisms (Rubin, 1976)

Understanding *why* data is missing determines how safely it can be imputed.

### MCAR — Missing Completely At Random
- The probability of missingness is independent of both observed and unobserved data.
- **Example:** A sensor drops a reading due to random hardware noise.
- **Imputation:** Select a method for the analysis and missingness assumptions. Mean or median replacement changes variation and relationships; assess the resulting bias and uncertainty.
- **Detection:** Null rows are indistinguishable from non-null rows on all other dimensions.

### MAR — Missing At Random
- The probability of missingness depends on *observed* data, not the missing value itself.
- **Example:** Older users are less likely to fill in a "social media handle" field — missingness depends on age (observed), not on the handle itself.
- **Safe to impute?** Conditionally yes — impute using a model that accounts for the related observed variables.
- **Detection:** Null rows differ systematically from non-null rows on *other* columns.

### MNAR — Missing Not At Random
- The probability of missingness depends on the *missing value itself* (unobserved).
- **Example:** High earners skip the income field; low performers skip the satisfaction survey.
- **Safe to impute?** No — imputation will introduce systematic bias. Escalate to domain owner.
- **Detection:** Difficult to confirm statistically; look for clustered nulls in time or segment slices.

---

## Measured completeness and separate quality checks

The included profiler calculates completeness as the percentage of non-null cells among the selected columns and returns it with `score_name: completeness`. It also reports column statistics. This measured percentage does not combine or estimate other quality dimensions.

Evaluate the other properties with explicit project rules: type and format consistency, domain validity, row or key uniqueness, cross-record integrity, and timestamp freshness. Record the denominator and failure examples for each check. Do not assign a numerical score to a property that was not measured or use a general threshold as proof that the data is fit for its intended use.

## Outlier Detection Methods

### IQR (Interquartile Range)
- **Formula:** Outlier if `x < Q1 − 1.5×IQR` or `x > Q3 + 1.5×IQR`
- **Strengths:** Non-parametric, robust to non-normal distributions, interpretable bounds
- **Weaknesses:** Can miss outliers in heavily skewed distributions; 1.5× multiplier is conventional, not universal
- **When to use:** Default choice for most business datasets (revenue, counts, durations)

### Z-score
- **Formula:** Outlier if `|x − μ| / σ > threshold` (commonly 3.0)
- **Strengths:** Simple, widely understood, easy to explain to stakeholders
- **Weaknesses:** Mean and std are themselves influenced by outliers — the method is self-defeating for extreme contamination
- **When to use:** Only when the distribution is approximately normal and contamination is < 5%

### Modified Z-score (Iglewicz-Hoaglin)
- **Formula:** `M_i = 0.6745 × |x_i − median| / MAD`; outlier if `M_i > 3.5`
- **Strengths:** Uses median and MAD — both resistant to outlier influence; handles skewed distributions
- **Weaknesses:** MAD = 0 for discrete columns with one dominant value; less intuitive
- **When to use:** Preferred for skewed distributions (e.g. revenue, latency, page views)

---

## Imputation Strategies

| Method | When | Risk |
|---|---|---|
| Mean | MCAR, continuous, symmetric distribution | Distorts variance; don't use with skewed data |
| Median | MCAR/MAR, continuous, skewed distribution | Safe for skewed; loses variance |
| Mode | MCAR/MAR, categorical | Can over-represent one category |
| Forward-fill | Time series with MCAR/MAR gaps | Assumes value persists — valid for slowly-changing fields |
| Binary indicator | Null % 1–30% | Preserves information about missingness without imputing |
| Model-based | MAR, high-value columns | Most accurate but computationally expensive |
| Drop column | > 50% missing with no business justification | Safest option if column has no predictive value |

**Golden rule:** Always add a `col_was_null` indicator column when imputing with null% > 1%. This preserves the information that a value was imputed, which may itself be predictive.

---

## Common Silent Data Quality Failures

These are the issues that don't raise errors but corrupt results:

1. **Sentinel values** — `0`, `-1`, `9999`, `""` used to mean "unknown" in legacy systems
2. **Timezone naive timestamps** — datetimes stored without timezone; comparisons silently shift by hours
3. **Trailing whitespace** — `"active "` ≠ `"active"` causes silent join mismatches
4. **Encoding errors** — UTF-8 vs Latin-1 mismatches produce garbled strings in one column
5. **Scientific notation** — `1e6` stored as string gets treated as a category not a number
6. **Implicit schema changes** — upstream adds a new category to a lookup field; existing code silently drops new rows

---

## References

- Rubin, D.B. (1976). "Inference and Missing Data." *Biometrika* 63(3): 581–592.
- Iglewicz, B. & Hoaglin, D. (1993). *How to Detect and Handle Outliers*. ASQC Quality Press.
- DAMA International (2017). *DAMA-DMBOK: Data Management Body of Knowledge*. 2nd ed.
- ISO 8000-8: Data quality — Concepts and measuring.

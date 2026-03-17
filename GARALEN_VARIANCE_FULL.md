# Garalén Variance Model  
### Narrative + Statistical + Physical Framework

---

# 1. Narrative Context

Garalén is a non-Republic Outer Rim world under Republic-aligned emergency coordination.

Key characteristics:

- Climate instability (hurricanes, seismic activity)
- Population corridor between coastal and highland regions
- Dependence on Republic emergency logistics
- Civil Coordination Authority governs response

Over a multi-year period, Garalén exhibits:

> A sustained statistical deviation in civil emergency outcomes.

This deviation:

- Is not explained by infrastructure changes
- Is not explained by procedural reforms
- Is not data corruption
- Persists across multiple reporting cycles

After the removal of a specific non-executive dependent:

> System performance returns to baseline expectations.

---

# 2. Modeling Objective

Construct synthetic data such that:

- Republic-level analysis detects a weak anomaly
- Imperial re-analysis detects a stronger statistical deviation
- No explicit causal mechanism is assumed
- Only statistical deviation is observable

---

# 3. Core Variables

## 3.1 Severity \( S_t \)

Represents intensity of environmental events per quarter.

Modeled as:

\[
S_t = \phi S_{t-1} + A \sin\left(\frac{2\pi t}{T}\right) + \epsilon_t
\]

Where:

- \( \phi \): temporal persistence (memory)
- \( A \): seasonal forcing amplitude
- \( T \): seasonal period
- \( \epsilon_t \sim \mathcal{N}(0, \sigma^2) \): stochastic shocks

### Physical interpretation

- AR(1): dissipative system with memory
- Sinusoidal term: external periodic forcing
- Noise: environmental unpredictability

---

## 3.2 Decision Load \( N_t \)

Number of critical decisions per period:

\[
N_t = a + b S_t
\]

Interpretation:

- Base decision load exists at all times
- Higher severity → more critical decision points

This represents the number of "micro-events" in the system.

---

# 4. Baseline System (No Anomaly)

Losses arise from independent failure probabilities:

\[
Y_t \sim \text{Binomial}(N_t, q)
\]

Where:

- \( q \): probability of failure per decision

### Physical analogy

- Many independent trials
- Each trial has failure probability
- System behaves like a standard statistical ensemble

---

# 5. Anomalous System (Child Present)

A non-classical influence slightly reduces failure probability.

This influence is:

- Not deterministic
- Not constant
- Not always active

Modeled as:

\[
p_t \sim \text{Beta}(\alpha, \beta)
\]

Effective failure probability:

\[
q_{eff,t} = q (1 - p_t)
\]

Losses:

\[
Y_t \sim \text{Binomial}(N_t, q_{eff,t})
\]

---

# 6. Interpretation of the Anomaly

The child:

- Does not act globally
- Does not anticipate events
- Does not learn from history

Instead:

> The child influences individual critical decisions when they arise.

Therefore:

- More severe events → more decision points
- More decision points → more opportunities for influence

---

# 7. Key Consequence

Expected reduction in losses:

\[
\Delta Y_t \approx N_t q p_t
\]

Thus:

- Effect is negligible at low severity
- Effect grows at high severity
- No visible "miracle events"
- Only statistical bias

---

# 8. Statistical Structure

The system becomes a **hierarchical stochastic model**:

- Binomial variability (micro-level randomness)
- Beta variability (parameter fluctuations)

This produces:

- Slight overdispersion
- Subtle deviation from baseline expectation
- No obvious anomalies per event

---

# 9. Physical Interpretation

This can be viewed as:

- A many-body system (decisions)
- With a small perturbation in coupling (failure probability)

The anomaly behaves like:

> A weak perturbation that becomes visible only in large systems.

Analogy:

- Small change in interaction strength
- Observable only in macroscopic aggregates

---

# 10. Temporal Behavior

The anomaly:

- Does not follow seasonal phase
- Does not track periodic forcing
- Only depends on instantaneous system size \( N_t \)

Thus:

- Correlation with severity is indirect
- No explicit temporal signature

---

# 11. Detectability

Republic-level detection:

- High tolerance
- Weak statistical flags
- Possibly ignored

Imperial-level detection:

- Cross-period aggregation
- Residual analysis
- Detection of sustained deviation

---

# 12. Removal Event

At time \( t = t^* \):

- The influencing variable disappears

After that:

- System reverts to baseline
- No structural change
- Only statistical normalization

---

# 13. Modeling Philosophy

Constraints:

- No extreme outliers
- No zero-loss miracles
- No visible discontinuities

Desired behavior:

- Smooth statistical deviation
- Subtle but persistent effect
- Realistic variability

---

# 14. Implementation Summary

Core components in code:

- AR(1) + seasonal forcing → severity
- Linear mapping → decision count
- Binomial sampling → losses
- Beta modulation → anomaly

---

# 15. Future Extensions

- Nonlinear decision thresholds
- Multiple interacting regions
- Time-delay in response systems
- Bayesian detection framework
- Causal inference under hidden variables

---

# End of Document
# GARALEN — Statistical & Physical Model Documentation

---

## 1. Modeling Objective

Construct synthetic operational data for a network of humanitarian missions such that:

- Standard statistical analysis detects a weak performance anomaly in one mission
- Aggregated cross-period analysis detects a stronger, sustained deviation
- No explicit causal mechanism is assumed or encoded
- Only the statistical signature of the deviation is observable

The anomaly is designed to be real but subtle: detectable through careful analysis, not visible per-event.

---

## 2. Core Variables

### 2.1 Environmental Severity — $S_t$

Represents the intensity of environmental events (climate, seismic) per quarter.

Modeled as an AR(1) process with seasonal forcing:

$$S_t = \phi S_{t-1} + A \sin\!\left(\frac{2\pi t}{T}\right) + \epsilon_t$$

| Parameter | Interpretation |
|---|---|
| $\phi$ | Temporal persistence (system memory) |
| $A$ | Seasonal forcing amplitude |
| $T$ | Seasonal period |
| $\epsilon_t \sim \mathcal{N}(0, \sigma^2)$ | Stochastic environmental shocks |

**Physical interpretation:** AR(1) as a dissipative system with memory; sinusoidal term as external periodic forcing; noise as environmental unpredictability.

---

### 2.2 Decision Load — $N_t$

Number of critical operational decisions per period:

$$N_t = a + b\, S_t$$

Higher environmental severity produces more critical decision points. This is the number of discrete trials in the loss model.

---

## 3. Baseline System

In the absence of any anomaly, losses arise from independent failure probabilities across decisions:

$$Y_t \sim \text{Binomial}(N_t,\, q)$$

where $q$ is the per-decision failure probability. This is the null model: a standard statistical ensemble with no inter-mission variation beyond sampling noise.

---

## 4. Anomalous System

One mission exhibits a latent reduction in its per-decision failure probability. The influence is:

- Not deterministic
- Not constant across periods
- Not directly observable

Modeled via a Beta-distributed efficiency parameter:

$$p_t \sim \text{Beta}(\alpha, \beta)$$

Effective failure probability for the anomalous mission:

$$q_{\text{eff},t} = q\,(1 - p_t)$$

Losses for the anomalous mission:

$$Y_t \sim \text{Binomial}(N_t,\, q_{\text{eff},t})$$

---

## 5. Structure of the Anomaly

The anomaly acts at the level of individual decisions, not at the event level. Consequently:

- More severe events → more decision points → more opportunities for the influence to manifest
- The effect is negligible at low severity and grows with $N_t$

Expected reduction in losses relative to baseline:

$$\Delta Y_t \approx N_t\, q\, p_t$$

This produces:

- Slight overdispersion relative to a pure Binomial
- A subtle, persistent negative bias in losses for the anomalous mission
- No visible outlier events — only a statistical shift in the distribution

---

## 6. Hierarchical Model Summary

The system is a **two-level hierarchical stochastic model**:

| Level | Variable | Distribution |
|---|---|---|
| Macro | Environmental severity $S_t$ | AR(1) + seasonal |
| Meso | Decision load $N_t$ | Linear function of $S_t$ |
| Micro | Losses $Y_t$ | Binomial$(N_t, q_{\text{eff},t})$ |
| Anomaly | Efficiency parameter $p_t$ | Beta$(\alpha, \beta)$ |

---

## 7. Temporal Behavior

The anomaly parameter $p_t$ is drawn independently each period — it does not track seasonal phase or periodic forcing. Its effect correlates with severity only indirectly, through $N_t$. This means:

- No explicit temporal signature in the anomaly
- Correlation with severity is a consequence of model structure, not a built-in assumption
- Standard seasonal decomposition will not isolate it

---

## 8. Detectability

| Analysis level | Expected behavior |
|---|---|
| Per-event inspection | Anomaly not visible |
| Rolling variance windows | Weak flag |
| Cross-mission percentile ranking | Persistent low-rank signal |
| Aggregated residual analysis | Sustained deviation detectable |

---

## 9. Removal Event

At a defined time $t = t^*$, the anomalous influence is removed. After that point:

- The mission reverts to baseline Binomial behavior
- No structural change in the environment or decision load
- The deviation disappears through statistical normalization

This is a key testable feature of the model: the change point at $t^*$ should be detectable in retrospective analysis.

---

## 10. Implementation

Core pipeline:

```
severity.py      → AR(1) + seasonal forcing → S_t
decisions.py     → linear mapping          → N_t
losses.py        → Binomial sampling        → Y_t (baseline)
anomaly.py       → Beta modulation          → q_eff,t (anomalous mission)
simulation.py    → multi-mission orchestrator
generate_data.py → exports simulation.csv
```

---

## 11. Dynamic Model (In Development)

The static model treats each period as independent. The dynamic model introduces intra-event temporal structure:

- Decision dynamics modeled as a driven spring-mass oscillator
- Numerical integration via **Störmer-Verlet** scheme (symplectic, energy-conserving)
- Asymmetric damping: different resistance to escalation vs. de-escalation
- Anomaly enters as a perturbation to the damping coefficient

This allows modeling of decision momentum and recovery dynamics within a single event.

---

## 12. Modeling Constraints

The model is designed to avoid artifacts that would make detection trivially easy or trivially hard:

- No extreme outliers or zero-loss events
- No visible discontinuities at the anomaly boundary
- Smooth statistical deviation with realistic variability
- Signal-to-noise ratio calibrated to require genuine statistical effort to detect

---

## 13. Potential Extensions

- Nonlinear decision thresholds and saturation effects
- Multiple interacting mission regions with cross-contamination
- Time-delay in environmental response systems
- Bayesian change-point detection framework
- Causal inference under hidden confounders
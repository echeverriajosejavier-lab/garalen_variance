import numpy as np
import matplotlib.pyplot as plt
from garalen_dynamic.config_dynamic import ModelConfigDynamic
from garalen_dynamic.severity_internal import generate_internal_severity
from garalen_dynamic.decisions_dynamic import integrate_event

config = ModelConfigDynamic()

# severidad interna para un evento de pico 50
s_tau = generate_internal_severity(50.0, config)
tau = np.linspace(0, 1, config.n_internal)

# evolución de decisiones sin y con amortiguamiento
N_sin = integrate_event(s_tau, config, gamma=0.0)
N_con = integrate_event(s_tau, config, gamma=2.0)

for i in range(5):
    print(f"tau={i}: s={s_tau[i]:.2f}, N={N_sin[i]:.2f}")

fig, axes = plt.subplots(2, 1, figsize=(10, 6), sharex=True)

axes[0].plot(tau, s_tau)
axes[0].set_ylabel("Severidad interna s(tau)")

axes[1].plot(tau, N_sin, label="sin amortiguamiento")
axes[1].plot(tau, N_con, label="con amortiguamiento")
axes[1].set_ylabel("Decisiones N")
axes[1].set_xlabel("tau")
axes[1].legend()

plt.tight_layout()
plt.show()

# Test de equilibrio

# config_test = ModelConfigDynamic(n_internal=10000)
# s_tau_min = np.ones(config_test.n_internal) * config_test.s_min
# N_eq = integrate_event(s_tau_min, config_test, gamma=0.0)
# print(f"N al final con s=s_min: {N_eq[-1]:.2f}")
# print(f"N esperado (a): {config.a}")

# tau = np.linspace(0, 1, config_test.n_internal)

# plt.plot(tau, N_eq)
# plt.axhline(config.a, color="red", linestyle="--", label=f"N_eq = {config.a}")
# plt.ylabel("N")
# plt.xlabel("tau")
# plt.legend()
# plt.show()
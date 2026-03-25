from dataclasses import dataclass

@dataclass
class ModelConfigDynamic:
    # Parámetros de severidad (AR1 + forzado estacional)
    phi: float = 0.7        # memoria del sistema
    A: float = 1.5          # amplitud estacional
    T: float = 30.0          # período estacional (~30 eventos = 1 año)
    sigma: float = 0.5      # ruido estocástico
    # Parámetros de la dinámica de decisiones
    a : float = 10.0        # carga base
    m: float = 0.75          # masa / sensibilidad al forzado
    gamma_max: float = 2.0  # amortiguamiento máximo de Sora
    k: float = 0.1          # constante elástica del modelo como un resorte
    dt: float = 0.1         # paso del método de Störmer-
    # Parámetros de la severidad interna
    n_internal: float = 50  # tamaño del evento
    tau_peak: float = 0.4
    sigma_left: float = 0.15
    sigma_right: float = 0.25
    s_min: float = 1.0
    seed: int = 42
    # Parámetros temporales
    past: int = 420
    n_S: int = 510
    n_periods: int = 930    # past + n_S
    t_star: int = 900       # past + n_S - 30
    # Parámetros de la anomalía
    k_s: float = 0.02
    t_s: float = 620.0      # 200 + past
    k_c: float = 0.015
    t_c: float = 630.0      # 210 + past
    p_max: float = 1.0
    p_residual: float = 0.01
    lambda_decay: float = 0.3
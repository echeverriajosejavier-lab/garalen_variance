from dataclasses import dataclass

@dataclass
class ModelConfig:
    # Parámetros de severidad (AR1 + forzado estacional)
    phi: float = 0.7        # memoria del sistema
    A: float = 1.5          # amplitud estacional
    T: float = 30.0          # período estacional (~30 eventos = 1 año)
    sigma: float = 0.5      # ruido estocástico

    # Parámetros de carga de desiciones 
    a: float = 10.0         # carga base
    b: float = 5.0          # sensibilidad a la severidad

    # Parámetros de pérdidas
    k_sat: float = 0.025      # abruptez de saturación
    N_0: float = 500.0     # umbral de saturación

    # Parámetros de la simulación
    n_S: float = 510 # años con Sora
    past: float = 420
    n_periods: int = n_S + past  # ~25 años de operaciones
    t_star: int = int (past + n_S - 30)        # evento en que Oblata extrae a Sora (~ 11 años)
    seed: int = 42          # semilla para reproducibilidad

    # Parámetros de la anomalía 
    k_s: float = 0.02        # abruptez de la maduración de Sora
    t_s: float = past + 200.0       # centro de maduración Sora (~año 9)
    k_c: float = 0.015        # abruptez de la receptividad de Crisa
    t_c: float = past + 210.0       # centro receptividad Crisa (~año 9.5)
    lambda_decay: float = 0.3 # velocidad de decaimiento post t_star
    p_residual: float = 0.01 # influencia residual tras la desaparición
    p_max: float = 1 # influencia máxima de Sora en el pico

    # Parámetros de la influencia de la anomalía según severidad
    sigma_g: float = 40.0   
    S_0 : float = 50.0

    # Parámetros para varias misiones

    sigma_obs: float = 0.01     # ruido de observación por misión
    n_missions: float = 30      # número de misiones sin anomalía

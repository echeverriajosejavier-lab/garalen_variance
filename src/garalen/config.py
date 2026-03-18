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
    k_sat: float = 0.3      # abruptez de saturación
    N_0: float = 20.0     # umbral de saturación

    # Parámetros de la simulación
    n_periods: int = 360  # ~12 años de operaciones
    t_star: int = 330        # evento en que Oblata extrae a Sora (~ año 11)
    seed: int = 42          # semilla para reproducibilidad

    # Parámetros de la anomalía 
    k_s: float = 0.5        # abruptez de la maduración de Sora
    t_s: float = 270.0       # centro de maduración Sora (~año 9)
    k_c: float = 0.4        # abruptez de la receptividad de Crisa
    t_c: float = 290.0       # centro receptividad Crisa (~año 9.5)
    lambda_decay: float = 0.3 # velocidad de decaimiento post t_star
    p_residual: float = 0.5 # influencia residual tras la desaparición
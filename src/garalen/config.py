from dataclasses import dataclass

@dataclass
class ModelConfig:
    # Parámetros de severidad (AR1 + forzado estacional)
    phi: float = 0.7        # memoria del sistema
    A: float = 1.5          # amplitud estacional
    T: float = 4.0          # período estacional (en trimestre)
    sigma: float = 0.5      # ruido estocástico

    # Parámetros de carga de desiciones 
    a: float = 10.0         # carga base
    b: float = 5.0          # sensibilidad a la severidad

    # Parámetros de pérdidas
    k_sat: float = 0.3      # abruptez de saturación
    N_0: float = 20.0     # umbral de saturación

    # Parámetros de la anomalía 
    k_s: float = 0.5        # abruptez de la maduración de Sora
    t_s: float = 12.0       # trimestre de la aceleración de Sora (salida de la segunda niñez)
    k_c: float = 0.4        # abruptez de la receptividad de Crisa
    t_c: float = 16.0       # trimestre de aceleración de Crisa (posterios a t_s)

    # Parámetros de la simulación
    n_periods: int = 40     # número de trimestres a simular
    t_star: int = 30        # trimestre en que desaparece la anomalía
    seed: int = 42          # semilla para reproducibilidad
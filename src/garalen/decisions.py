import numpy as np
from garalen.config import ModelConfig

def generate_decisions(S: np.ndarray, config: ModelConfig) -> np.ndarray:
    """
    Genera la serie temporal de carga de decisiones N_t

    N_t = a + b * S_t

    El resultado se redondea a enteros porque representa un conteo de decisiones.
    """

    N = config.a + config.b * S
    
    return np.round(N).astype(int)
import numpy as np
from garalen.config import ModelConfig
from garalen.anomaly import compute_anomaly

def generate_decisions(S: np.ndarray, config: ModelConfig, anomaly: bool = False) -> np.ndarray:
    """
    Genera la serie temporal de carga de decisiones N_t.
    
    Sin anomalía: N_t = a + b * S_t
    Con anomalía: N_eff,t = N_t - delta_t
    donde delta_t son las decisiones prevenidas por Sora.
    """

    N = config.a + config.b * S

    if anomaly:
        p = compute_anomaly(config)
        delta = np.round(p * N).astype(int)
        N = np.maximum(N - delta, 1)
    
    return np.round(N).astype(int)
import numpy as np
from garalen.config import ModelConfig
from garalen.anomaly import _sigmoid, compute_anomaly

def _failure_probability(N: np.ndarray, config: ModelConfig) -> np.array:
    """
    Probabilidad de falla por decisión en función de la carga.

    A mayor carga de decisiones (críticas), mayor probabilidad de falla.
    Satura en 1 por construcción de la sigmoidal.
    """

    return _sigmoid(N, config.k_sat, config.N_0)

def generate_losses(N: np.ndarray, S: np.ndarray, config: ModelConfig, anomaly: bool, rng: np.random.Generator) -> np.ndarray:
    """
    Genera la serie temporal de pérdidas Y_t.

    Sin anomalía: Y_t va como una Binomial(N_t, q(N_t))
    Con anomalía: Y_t va como una Binomial(N_t, q(N_t) * (1 - p_t))
    """
def generate_losses(N: np.ndarray, S: np.ndarray, config: ModelConfig,
                    anomaly: bool, rng: np.random.Generator) -> np.ndarray:
    q = _failure_probability(N, config)
    
    if anomaly:
        p = compute_anomaly(config)
        q_eff = q * (1 - p)
    else:
        q_eff = q
    
    return rng.binomial(N.astype(int), np.clip(q_eff, 0, 1))
import numpy as numpy
from garalen.config import ModelConfig

def generate_severity(config: ModelConfig) -> np.ndarray:
    """
    Genera la serie temporal de severidad S_t.

    S_t = phi * S_{t-1} + A * sin(2*pi*t / T) + epsilon_t

    Usa burn-in de 2 ciclos completos para eliminar el efecto del valor inicial artificial.

    """
    rng = np.random.default_rng(config.seed)

    burn_in = int(2 * config.T)     # 2 ciclos completos
    total = config.n_periods + burn_in

    S = np.zeros(total)
    epsilon = rng.normal(0, config.sigma, size=total)

    for t in range(1,total):
        S[t] = (config.phi *S[t-1] + config.A * np.sin(2 * np.pi * t / config.T) + epsilon[t])

    return S[burn_in:]              # descartamos el burn-in
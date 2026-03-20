import numpy as np
from garalen.config import ModelConfig

def _sigmoid(x: np.ndarray, k: float, x0: float) -> np.ndarray:
    """
    Función sigmoidal generalizada.

    sigma(x, k, x0) = 1 / (1 + exp(-k * (x - x0)))

    k controla la abrupteza, x0 el centro de la transición.

    """

    return 1.0 / (1.0 + np.exp(-k * (x - x0)))

def _failure_probability(N: np.ndarray, config: ModelConfig) -> np.array:
    """
    Probabilidad de falla por decisión en función de la carga.

    A mayor carga de decisiones (críticas), mayor probabilidad de falla.
    Satura en 1 por construcción de la sigmoidal.
    """

    return _sigmoid(N, config.k_sat, config.N_0)

def _anomaly(config: ModelConfig) -> np.ndarray:
    """
    Influencia combinada de Sora y Crisa sobre las Decisiones.

    Antes de t_star: Es el producto de dos sigmoidales en el tiempo.
    Después de t_star: decaimiento exponencial hacia p_residual
    """

    t = np.arange(config.n_periods)
    sora = _sigmoid(t, config.k_s, config.t_s)
    crisa = _sigmoid(t, config.k_c, config.t_c)
    p = sora * crisa

    # normalizar solo pre t_star
    p_pre = p[:config.t_star]
    p_pre = config.p_max * p_pre / p_pre.max()
    p[:config.t_star] = p_pre

    # decaimiento post t_star
    mask = t >= config.t_star
    p_star = p[config.t_star - 1] # valor justo antes de t_star
    decay = config.p_residual + (p_star - config.p_residual) * np.exp(-config.lambda_decay * (t[mask] - config.t_star))
    p[mask] = decay

    return p

def generate_losses(N: np.ndarray, S: np.ndarray, config: ModelConfig, anomaly: bool, rng: np.random.Generator) -> np.ndarray:
    """
    Genera la serie temporal de pérdidas Y_t.

    Sin anomalía: Y_t va como una Binomial(N_t, q(N_t))
    Con anomalía: Y_t va como una Binomial(N_t, q(N_t) * (1 - p_t))
    """
    q = _failure_probability(N, config)

    if anomaly:
        p = _anomaly(config)
        g = np.exp(-0.5 * ((S - config.S_0) / config.sigma_g)**2)
        q_eff = q * (1 - p*g)
    else:
        q_eff = q
    
    Y = rng.binomial(N, q_eff)
    return Y
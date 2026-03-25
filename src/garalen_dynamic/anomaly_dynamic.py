import numpy as np
from garalen_dynamic.config_dynamic import ModelConfigDynamic

def _sigmoid(x: np.ndarray, k: float, x0: float) -> np.ndarray:
    return 1.0 / (1.0 + np.exp(-k * (x - x0)))

def compute_anomaly_dynamic(config: ModelConfigDynamic) -> np.ndarray:
    """
    Calcula la influencia combinada de Sora y Crisa a lo largo del tiempo.
    """
    t = np.arange(config.n_periods)
    edad = t - config.past
    
    sora = _sigmoid(edad, config.k_s, config.t_s - config.past)
    crisa = _sigmoid(edad, config.k_c, config.t_c - config.past)
    sora[t < config.past] = 0.0
    crisa[t < config.past] = 0.0
    
    p = sora * crisa
    p_pre = p[:config.t_star]
    p_pre = config.p_max * p_pre / p_pre.max()
    p[:config.t_star] = p_pre
    
    mask = t >= config.t_star
    p_star = p[config.t_star - 1]
    decay = config.p_residual + (p_star - config.p_residual) * np.exp(
        -config.lambda_decay * (t[mask] - config.t_star)
    )
    p[mask] = decay
    
    return p
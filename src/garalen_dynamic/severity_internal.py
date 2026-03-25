import numpy as np
from garalen_dynamic.config_dynamic import ModelConfigDynamic

def generate_internal_severity(S_peak: float, 
                                config: ModelConfigDynamic) -> np.ndarray:
    """
    Genera la severidad interna s(tau) para un evento dado su pico S_peak.
    
    Gaussiana asimétrica — sube con sigma_left, baja con sigma_right.
    El pico ocurre en tau_peak.
    """
    tau = np.linspace(0, 1, config.n_internal)
    sigma = np.where(tau < config.tau_peak, config.sigma_left, config.sigma_right)
    s = config.s_min + (S_peak - config.s_min) * np.exp(-0.5 * ((tau - config.tau_peak) / sigma) ** 2)
    return s
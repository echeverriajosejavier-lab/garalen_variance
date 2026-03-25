import numpy as np
from garalen_dynamic.config_dynamic import ModelConfigDynamic
from garalen_dynamic.anomaly_dynamic import compute_anomaly_dynamic

def integrate_event(s_tau: np.ndarray, config: ModelConfigDynamic, 
                    gamma: float) -> float:
    """
    Integra la ecuación del resorte para un evento usando Störmer-Verlet.
    
    N_{i+1} = 2N_i - N_{i-1} + dt^2 * (b*s(tau_i) - k*(N_i - a) - gamma*V_i)
    """
    n = len(s_tau)
    N = np.zeros(n)
    
    # condiciones iniciales
    N[0] = config.a
    N[1] = config.a + 0.5 * config.dt**2 * s_tau[0] / config.m
    
    for i in range(1, n-1):
        V_i = (N[i] - N[i-1]) / config.dt  # velocidad centrada
        F_i = (s_tau[i] - config.k * N[i] - gamma * V_i) / config.m
        N[i+1] = 2*N[i] - N[i-1] + config.dt**2 * F_i
    
    return N
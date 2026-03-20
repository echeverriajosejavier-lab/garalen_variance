import numpy as np
import pandas as pd
from dataclasses import dataclass
from garalen.config import ModelConfig
from garalen.severity import generate_severity
from garalen.decisions import generate_decisions
from garalen.losses import generate_losses

@dataclass
class SimulationResult:
    S: np.ndarray           # (n_perios, n_missions + 1)
    N: np.ndarray           # (n_perios, n_missions + 1)
    Y: np.ndarray           # (n_perios, n_missions + 1)
    mission_ids: list       # nombres de las misiones

def run_simulation(config: ModelConfig) -> SimulationResult:
    """
    Orquesta la simulación completa del modelo Garalén.
    
    Genera severidad, carga de decisiones y pérdidas
    con y sin anomalía, usando un único rng para
    garantizar reproducibilidad.

    
    Genera la simulación completa con múltiples misiones.
    
    La primera misión es Crisa (con anomalía).
    Las demás son misiones baseline con ruido de observación
    """
    rng = np.random.default_rng(config.seed)
    
    # Severidad y decisiones base

    S_base = generate_severity(config)
    N_base = generate_decisions(S_base, config)

    n_total = config.n_missions + 1
    S_all = np.zeros((config.n_periods, n_total))
    N_all = np.zeros((config.n_periods, n_total))
    Y_all = np.zeros((config.n_periods, n_total))

    mission_ids = ["crisa"] + [f"mission_{i+1:02d}" for i in range(config.n_missions)]

    for i in range(n_total):
        # ruido de observación
        noise_S = rng.normal(1, config.sigma_obs, size=config.n_periods)
        noise_N = rng.normal(1, config.sigma_obs, size=config.n_periods)
        S_obs = np.clip(S_base * noise_S, 1, 100)
       
        is_crisa = (i == 0)
        N_obs = generate_decisions(S_obs, config, anomaly=is_crisa)
        N_obs = np.clip(N_obs, 1, None).astype(int)
    
        S_all[:, i] = S_obs
        N_all[:, i] = N_obs
        Y_all[:, i] = generate_losses(N_obs, S_obs, config, anomaly=is_crisa, rng=rng)

    return SimulationResult(S=S_all, N=N_all, Y=Y_all, mission_ids=mission_ids)
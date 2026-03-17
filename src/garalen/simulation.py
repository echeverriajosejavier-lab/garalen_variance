import numpy as np
from dataclasses import dataclass
from garalen.config import ModelConfig
from garalen.severity import generate_severity
from garalen.decisions import generate_decisions
from garalen.losses import generate_losses

@dataclass
class SimulationResult:
    S: np.ndarray
    N: np.ndarray
    Y_anomaly: np.ndarray
    Y_baseline: np.ndarray

def run_simulation(config: ModelConfig) -> SimulationResult:
    """
    Orquesta la simulación completa del modelo Garalén.
    
    Genera severidad, carga de decisiones y pérdidas
    con y sin anomalía, usando un único rng para
    garantizar reproducibilidad.
    """
    rng = np.random.default_rng(config.seed)
    
    S = generate_severity(config)
    N = generate_decisions(S, config)
    Y_anomaly = generate_losses(N, config, anomaly=True, rng=rng)
    Y_baseline = generate_losses(N, config, anomaly=False, rng=rng)
    
    return SimulationResult(S=S, N=N, Y_anomaly=Y_anomaly, Y_baseline=Y_baseline)
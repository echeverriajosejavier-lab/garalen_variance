import numpy as np
from garalen.config import ModelConfig
from garalen.severity import generate_severity
from garalen.decisions import generate_decisions
from garalen.losses import generate_losses
from garalen.simulation import run_simulation, SimulationResult

def test_sim():
    config = ModelConfig()
    Sim = run_simulation(config)
    assert isinstance(Sim, SimulationResult)
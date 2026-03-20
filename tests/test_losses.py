import numpy as np
from garalen.config import ModelConfig
from garalen.severity import generate_severity
from garalen.decisions import generate_decisions
from garalen.losses import generate_losses

def test_non_negativity():
    config = ModelConfig()
    rng = np.random.default_rng(config.seed)
    S = generate_severity(config)
    N = generate_decisions(S, config)
    Y_T = generate_losses(N, S, config, anomaly=True, rng=rng)
    Y_F = generate_losses(N, S, config, anomaly=False, rng=rng)
    assert np.all(Y_T >= 0) and np.all(Y_F >= 0)

def test_mistakes_lesser_decisions():
    config = ModelConfig()
    rng = np.random.default_rng(config.seed)
    S = generate_severity(config)
    N = generate_decisions(S, config)
    Y_T = generate_losses(N, S, config, anomaly=True, rng=rng)
    Y_F = generate_losses(N, S, config, anomaly=False, rng=rng)
    assert np.all(Y_T <= N) and np.all(Y_F <= N)

def test_output_length():
    config = ModelConfig()
    rng = np.random.default_rng(config.seed)
    S = generate_severity(config)
    N = generate_decisions(S, config)
    Y_T = generate_losses(N, S, config, anomaly=True, rng=rng)
    Y_F = generate_losses(N, S, config, anomaly=False, rng=rng)
    assert len(Y_T) == config.n_periods and len(Y_F) == config.n_periods

def test_reduction_losses():
    config = ModelConfig()
    rng = np.random.default_rng(config.seed)
    S = generate_severity(config)
    N = generate_decisions(S, config)
    Y_T = generate_losses(N, S, config, anomaly=True, rng=rng)
    Y_F = generate_losses(N, S, config, anomaly=False, rng=rng)
    assert np.mean(Y_T) < np.mean(Y_F)

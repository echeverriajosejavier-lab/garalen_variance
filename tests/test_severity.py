import numpy as np
from garalen.config import ModelConfig
from garalen.severity import generate_severity

def test_output_length():
    config = ModelConfig()
    S = generate_severity(config)
    assert len(S) == config.n_periods

def test_reproducibility():
    config = ModelConfig()
    S1 = generate_severity(config)
    S2 = generate_severity(config)
    assert np.array_equal(S1, S2)

def test_different_seeds():
    config1 = ModelConfig(seed=42)
    config2 = ModelConfig(seed=99)
    S1 = generate_severity(config1)
    S2 = generate_severity(config2)
    assert not np.array_equal(S1, S2)

def test_mean_all_positive():
    config = ModelConfig()
    S = generate_severity(config)
    assert np.all(S>0)
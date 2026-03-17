import numpy as np
from garalen.config import ModelConfig
from garalen.severity import generate_severity
from garalen.decisions import generate_decisions

def test_output_length():
    config = ModelConfig()
    S = generate_severity(config)
    N = generate_decisions(S,config)
    assert len(N) == len(S) 

def test_integrality():
    config = ModelConfig()
    S = generate_severity(config)
    N = generate_decisions(S,config)
    assert np.issubdtype(N.dtype, np.integer)

def test_greater_charge():
    config = ModelConfig()
    S_low = np.array([1.0,2.0,3.0])
    S_high = np.array([2.0,3.0,4.0])
    N_low = generate_decisions(S_low,config)
    N_high = generate_decisions(S_high,config)
    assert np.all(N_high > N_low)

def test_all_positive():
    config = ModelConfig()
    S = generate_severity(config)
    N = generate_decisions(S,config)
    assert np.all(N>0)
from garalen_dynamic.config_dynamic import ModelConfigDynamic
from garalen_dynamic.decisions_dynamic import generate_decisions_dynamic
from garalen_dynamic.anomaly_dynamic import compute_anomaly_dynamic
import numpy as np

config = ModelConfigDynamic()
S = np.ones(config.n_periods) * 50  # severidad constante de prueba
N = generate_decisions_dynamic(S, config, anomaly=False)
print(f"N shape: {N.shape}")
print(f"N mínimo: {N.min()}, N máximo: {N.max()}")

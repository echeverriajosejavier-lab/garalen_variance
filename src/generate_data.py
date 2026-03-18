import numpy as np
import pandas as pd
from pathlib import Path
from garalen.config import ModelConfig
from garalen.simulation import run_simulation

def main():
    config = ModelConfig()
    result = run_simulation(config)
    
    t = np.arange(config.n_periods)
    
    df = pd.DataFrame({
        "t": t,
        "S": result.S,
        "N": result.N,
        "Y_anomaly": result.Y_anomaly,
        "Y_baseline": result.Y_baseline
    })
    
    output_path = Path("data/simulation.csv")
    output_path.parent.mkdir(exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Datos guardados en {output_path}")

if __name__ == "__main__":
    main()
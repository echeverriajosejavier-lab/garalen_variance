import numpy as np
import pandas as pd
from pathlib import Path
from garalen.config import ModelConfig
from garalen.simulation import run_simulation

def to_dataframe(result, config):
    """
    Convierte SimulationResult a DataFrame rago con una fila por evento por misión.
    """
    dfs = []
    t = range(config.n_periods)

    for i, mission_id in enumerate(result.mission_ids):
        df = pd.DataFrame({
            "t": t,
            "mission_id": mission_id,
            "S": result.S[:, i],
            "N": result.N[:, i],
            "Y": result.Y[:, i]
        })
        dfs.append(df)
    
    return pd.concat(dfs, ignore_index=True)

def main():
    config = ModelConfig()
    result = run_simulation(config)

    df = to_dataframe(result, config)

    output_path = Path("data/simulation.csv")
    output_path.parent.mkdir(exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Datos guardados en {output_path}")
    print(f"Shape: {df.shape}")
    print(f"Misiones: {df.mission_id.nunique()}")

if __name__ == "__main__":
    main()
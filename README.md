# GARALEN — Humanitarian Emergency Response Simulation & Anomaly Detection

End-to-end statistical simulation pipeline for modeling humanitarian emergency response operations and detecting subtle performance anomalies across a network of missions.

## Overview

GARALEN generates synthetic operational data for a network of humanitarian missions responding to climate and seismic events. Each mission logs environmental severity, critical decision load, and losses per event. The central question: given noisy, multi-mission data, can a statistically subtle anomaly — one mission consistently outperforming expectations — be reliably detected?

The model is designed so the anomaly is real but weak: detectable through careful statistical analysis, invisible to casual inspection. This mirrors real-world anomaly detection problems where signal-to-noise ratio is low and causal mechanisms are hidden.

## Technical Highlights

- **AR(1) time series** with seasonal sinusoidal forcing for environmental severity
- **Binomial loss processes** with sigmoidal failure-probability saturation
- **Hierarchical stochastic model**: Beta-modulated anomaly over a Binomial baseline
- **Multi-mission simulation** with per-observer measurement noise
- **Dynamic model** (in development): spring-mass oscillator with Störmer-Verlet integration for intra-event decision dynamics and asymmetric damping
- **Anomaly detection** via rolling variance windows, per-event percentile ranking across missions, and scatter analysis
- **Full test suite** with pytest; modular, pip-installable package structure

## Project Structure

```
garalen_variance/
├── src/
│   ├── garalen/                  # static model (complete)
│   │   ├── config.py             # model parameters
│   │   ├── severity.py           # AR(1) + seasonal severity
│   │   ├── decisions.py          # critical decision load
│   │   ├── losses.py             # binomial loss process
│   │   ├── anomaly.py            # sigmoidal anomaly influence
│   │   └── simulation.py         # multi-mission orchestrator
│   ├── garalen_dynamic/          # dynamic model (in development)
│   │   ├── config_dynamic.py
│   │   ├── anomaly_dynamic.py
│   │   ├── decisions_dynamic.py  # Störmer-Verlet integration
│   │   └── severity_internal.py  # intra-event severity profile
│   └── generate_data.py          # generates simulation.csv
├── data/
│   └── simulation.csv
├── notebooks/
│   └── examination.ipynb         # model internals and anomaly analysis
├── tests/                        # pytest suite (13 passing)
├── tests_dynamic/
├── pyproject.toml
└── requirements.txt
```

## Installation

```bash
git clone https://github.com/<your-username>/garalen_variance.git
cd garalen_variance
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Linux/Mac
pip install -e .
pip install -r requirements.txt
```

## Usage

Generate simulation data:
```bash
python src/generate_data.py
```

Run the test suite:
```bash
pytest tests/
```

Open the notebook:
```bash
jupyter notebook notebooks/examination.ipynb
```

## Stack

Python · NumPy · SciPy · pandas · matplotlib · statsmodels · pytest · Jupyter
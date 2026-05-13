# GARALEN — Humanitarian Emergency Response Simulation & Anomaly Detection

A end-to-end statistical simulation pipeline for modeling humanitarian emergency response operations and detecting subtle performance anomalies across multiple missions.

## Overview

GARALEN generates synthetic operational data for a network of humanitarian missions responding to climate and seismic events. Each mission logs severity, critical decision load, and losses per event. The core question: given noisy, multi-mission data, can a statistically subtle anomaly — one mission consistently outperforming expectations — be detected?

The model is designed so the anomaly is real but weak: detectable through careful statistical analysis, not visible to the naked eye. This mirrors real-world anomaly detection problems where signal-to-noise ratio is low and causal mechanisms are hidden.

## Technical Highlights

- **AR(1) time series** with seasonal sinusoidal forcing for environmental severity
- **Binomial loss processes** with sigmoidal failure probability saturation
- **Hierarchical stochastic model**: Beta-modulated anomaly over Binomial baseline
- **Multi-mission simulation** with per-observer measurement noise
- **Dynamic model** (in development): spring-mass oscillator with Störmer-Verlet integration for intra-event decision dynamics and asymmetric damping
- **Anomaly detection** via rolling variance windows, per-event percentile ranking across missions, and scatter analysis
- **Full test suite** with pytest; modular, pip-installable package structure

## Project Structure

```
garalen_variance/
├── src/
│   ├── garalen/                  # static model
│   │   ├── config.py             # model parameters
│   │   ├── severity.py           # AR(1) + seasonal severity
│   │   ├── decisions.py          # critical decision load
│   │   ├── losses.py             # binomial loss process
│   │   ├── anomaly.py            # sigmoidal anomaly influence
│   │   └── simulation.py        # multi-mission orchestrator
│   ├── garalen_dynamic/          # dynamic model (in development)
│   │   ├── config_dynamic.py
│   │   ├── anomaly_dynamic.py
│   │   ├── decisions_dynamic.py  # Störmer-Verlet integration
│   │   └── severity_internal.py  # intra-event severity profile
│   └── generate_data.py          # generates simulation.csv
├── data/
│   └── simulation.csv
├── notebooks/
│   ├── examination.ipynb         # model internals exploration
│   └── analysis.ipynb            # raw data analysis
├── tests/                        # pytest suite (13 passing)
├── tests_dynamic/
└── pyproject.toml
```

## Installation

```bash
git clone https://github.com/<your-username>/garalen_variance.git
cd garalen_variance
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Linux/Mac
pip install -e .
pip install pytest jupyter matplotlib pandas scipy
```

## Usage

Generate simulation data:
```bash
python src/generate_data.py
```

Run tests:
```bash
pytest tests/
```

Open notebooks:
```bash
code notebooks/examination.ipynb
```

## Stack

Python · NumPy · SciPy · pandas · matplotlib · pytest · Jupyter · Git

---

# GARALEN — Simulación de Respuesta a Emergencias y Detección de Anomalías

Pipeline completo de simulación estadística para modelar operaciones de respuesta humanitaria a emergencias y detectar anomalías sutiles de rendimiento entre múltiples misiones.

## Descripción

GARALEN genera datos operacionales sintéticos para una red de misiones humanitarias que responden a eventos climáticos y sísmicos. Cada misión registra severidad del evento, carga de decisiones críticas y pérdidas por evento. La pregunta central: dado un conjunto de datos ruidoso y multimisión, ¿es posible detectar una anomalía estadísticamente sutil — una misión que consistentemente supera las expectativas?

El modelo está diseñado para que la anomalía sea real pero débil: detectable mediante análisis estadístico cuidadoso, no visible a simple vista. Esto replica problemas reales de detección de anomalías con baja relación señal-ruido y mecanismos causales ocultos.

## Aspectos técnicos destacados

- **Series de tiempo AR(1)** con forzamiento estacional sinusoidal para la severidad ambiental
- **Procesos de pérdida binomial** con saturación sigmoidal de la probabilidad de falla
- **Modelo estocástico jerárquico**: anomalía modulada por Beta sobre baseline Binomial
- **Simulación multimisión** con ruido de medición por observador
- **Modelo dinámico** (en desarrollo): oscilador masa-resorte con integración Störmer-Verlet para la dinámica intra-evento de decisiones y amortiguamiento asimétrico
- **Detección de anomalías** mediante ventanas de varianza móvil, ranking percentil por evento entre misiones y análisis de dispersión
- **Suite de tests completa** con pytest; estructura de paquete modular instalable con pip

## Stack

Python · NumPy · SciPy · pandas · matplotlib · pytest · Jupyter · Git
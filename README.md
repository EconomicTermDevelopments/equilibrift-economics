# Equilibrift: An Economic Framework

![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Status: Active](https://img.shields.io/badge/Status-Active-blue.svg)
![Category: Computational Economics](https://img.shields.io/badge/Category-equilibrift-purple.svg)

## Overview
`Equilibrift` is modeled as market conditions where equilibrium exists in theory but remains dynamically unreachable. The repository defines one canonical concept expression and one executable index pipeline. The mechanism focus is adjustment delays and capacity constraints prevent state variables from converging to clearing conditions.

This Phase 2 package includes upgraded documentation, working code with type hints, a 200-row synthetic dataset, notebook examples, semantic metadata, and a working-paper source. The objective is to make the term usable in research and policy workflows immediately, while keeping assumptions transparent and editable.

The project is structured for reproducibility: dataset generation is deterministic, index computation is explicit, and documentation aligns with code variable names. That alignment is the core scaling strategy for the remaining terms.

The same structure is reusable for the rest of TERMPRODUCT: preserve file shape and validation gates, then swap mechanism channels, assumptions, and examples. This keeps cross-term comparisons reliable and makes rollout to the remaining terms faster.

## Installation
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Quick Start
```bash
python generation_script.py
python equilibrift.py
```

## Documentation
- `DEFINITION.md`
- `docs/index.html`
- `paper.tex`

## Citation
Economic Research Collective (2026). "Equilibrift: An Economic Framework."

## License
MIT License.

---
language:
- en
license: mit
task_categories:
- tabular-classification
tags:
- economics
- equilibrift
- computational-economics
- computational-economics
- emerging-terminology
pretty_name: Equilibrift Economics Dataset
size_categories:
- n<1K
---

# Equilibrift Economics Dataset

## Dataset Description
### Summary
Synthetic 200-row dataset for `Equilibrift` measurement and computational experiments.

### Supported Tasks
- Economic analysis
- Computational Economics research
- Computational economics

### Languages
- English (metadata and documentation)
- Python (code examples)

## Dataset Structure
### Data Fields
- `id`: Unique observation id
- `period`: Synthetic adjustment period
- `equilibrium_gap`: Distance between observed state and model-implied equilibrium
- `adjustment_lag`: Lag in quantity and price adjustment
- `capacity_constraint`: Binding production or logistics capacity constraints
- `coordination_failure`: Coordination breakdown intensity among agents
- `expectation_dispersion`: Cross-agent dispersion in expectations
- `policy_response_delay`: Delay in stabilizing policy response
- `adaptive_capacity`: System ability to adapt toward equilibrium
- `equilibrift_index`: Composite term index

### Data Splits
- Full dataset: 200 examples

## Dataset Creation
### Source Data
Synthetic data generated for demonstrating Equilibrift applications.

### Data Generation
Channels are sampled from controlled distributions with correlated structure. The term index is computed from normalized channels and directional weights.

## Considerations
### Social Impact
Research-only synthetic data for method development and reproducibility testing.

## Additional Information
### Licensing
MIT License - free for academic and commercial use.

### Citation
@dataset{equilibrift2026,
title={{Equilibrift Economics Dataset}},
author={{Economic Research Collective}},
year={{2026}}
}

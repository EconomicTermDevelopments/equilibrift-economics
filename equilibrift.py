"""
Equilibrift: computational implementation for computational economics analysis.

Equilibrift refers to market state where a theoretical clearing equilibrium exists but becomes dynamically unreachable due to adaptation lags or capacity constraints that create insurmountable gaps between current system state and equilibrium position. This module provides a reproducible calculator that validates the canonical channels, normalizes each series, computes a weighted index, and supports simple counterfactual policy simulation. The design is intentionally transparent so researchers can inspect how the concept moves from definition to code. Typical uses include comparative diagnostics, notebook-based scenario testing, and integration into empirical pipelines where consistent measurement matters as much as prediction.
"""
from __future__ import annotations

from typing import Optional

import numpy as np
import pandas as pd

# Equilibrift channels track the observable anatomy of the canonical definition.
TERM_CHANNELS = [
    "equilibrium_gap",  # Equilibrium gap captures a distinct economic channel.
    "adjustment_lag",  # Adjustment lag captures a distinct economic channel.
    "capacity_constraint",  # Capacity constraint captures a distinct economic channel.
    "coordination_failure",  # Coordination failure captures a distinct economic channel.
    "expectation_dispersion",  # Expectation dispersion captures a distinct economic channel.
    "policy_response_delay",  # Policy response delay captures a distinct economic channel.
    "adaptive_capacity",  # Adaptive capacity mitigates exposure when it is high.
]

# Weighted channels preserve the repository's existing score logic.
WEIGHTED_CHANNELS = [
    "equilibrium_gap",
    "adjustment_lag",
    "capacity_constraint",
    "coordination_failure",
    "expectation_dispersion",
    "policy_response_delay",
    "adaptive_capacity",
]

# Default weights encode the relative economic importance of each weighted channel.
DEFAULT_WEIGHTS: dict[str, float] = {
    "equilibrium_gap": 0.2,  # Equilibrium gap captures a distinct economic channel.
    "adjustment_lag": 0.16,  # Adjustment lag captures a distinct economic channel.
    "capacity_constraint": 0.16,  # Capacity constraint captures a distinct economic channel.
    "coordination_failure": 0.14,  # Coordination failure captures a distinct economic channel.
    "expectation_dispersion": 0.12,  # Expectation dispersion captures a distinct economic channel.
    "policy_response_delay": 0.12,  # Policy response delay captures a distinct economic channel.
    "adaptive_capacity": 0.1,  # Adaptive capacity mitigates exposure when it is high.
}


class EquilibriftCalculator:
    """
    Compute Equilibrift index scores from tabular data.

    Parameters
    ----------
    weights : dict[str, float] | None
        Optional weights overriding DEFAULT_WEIGHTS. Keys must match
        WEIGHTED_CHANNELS and values must sum to 1.0.
    """

    def __init__(self, weights: Optional[dict[str, float]] = None) -> None:
        # Alternative weights are useful for robustness checks across specifications.
        self.weights = weights or DEFAULT_WEIGHTS.copy()

        # Exact key matching prevents silent omission of economically relevant channels.
        if set(self.weights) != set(WEIGHTED_CHANNELS):
            raise ValueError(f"Weights must include exactly these channels: {WEIGHTED_CHANNELS}")

        # Unit-sum weights keep the index interpretable across datasets.
        if abs(sum(self.weights.values()) - 1.0) >= 1e-6:
            raise ValueError("Weights must sum to 1.0")

    @staticmethod
    def _normalise(series: pd.Series) -> pd.Series:
        """
        Return min-max normalized values on the unit interval.
        """
        lo = float(series.min())
        hi = float(series.max())
        if hi == lo:
            # Degenerate channels should not create spurious variation.
            return pd.Series(np.zeros(len(series)), index=series.index)
        return (series - lo) / (hi - lo)

    def calculate_equilibrift(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Compute normalized channels, composite scores, and qualitative bands.
        """
        # Full channel validation keeps the score tied to the canonical definition.
        missing = [channel for channel in TERM_CHANNELS if channel not in df.columns]
        if missing:
            raise ValueError(f"Missing Equilibrift channels: {missing}")

        out = df.copy()
        for channel in TERM_CHANNELS:
            out[f"{channel}_norm"] = self._normalise(out[channel])

        # Positive channels intensify the mechanism while negative channels offset it.
        out["equilibrift_index"] = (
            + self.weights["equilibrium_gap"] * out["equilibrium_gap_norm"]
            + self.weights["adjustment_lag"] * out["adjustment_lag_norm"]
            + self.weights["capacity_constraint"] * out["capacity_constraint_norm"]
            + self.weights["coordination_failure"] * out["coordination_failure_norm"]
            + self.weights["expectation_dispersion"] * out["expectation_dispersion_norm"]
            + self.weights["policy_response_delay"] * out["policy_response_delay_norm"]
            + self.weights["adaptive_capacity"] * (1.0 - out["adaptive_capacity_norm"])
        )

        # Three bands keep the metric usable in audits, papers, and dashboards.
        out["equilibrift_band"] = pd.cut(
            out["equilibrift_index"],
            bins=[-np.inf, 0.33, 0.66, np.inf],
            labels=["low", "moderate", "high"],
        )
        return out

    def simulate_policy(self, df: pd.DataFrame, channel: str, reduction: float = 0.2) -> pd.DataFrame:
        """
        Simulate a policy shock that reduces one observed channel.
        """
        if channel not in TERM_CHANNELS:
            raise ValueError(f"Unknown Equilibrift channel: {channel}")
        if reduction < 0.0 or reduction > 1.0:
            raise ValueError("reduction must be between 0.0 and 1.0")

        # Counterfactual shocks translate reforms into score movements.
        df_policy = df.copy()
        df_policy[channel] = df_policy[channel] * (1 - reduction)
        return self.calculate_equilibrift(df_policy)


if __name__ == "__main__":
    sample = pd.read_csv("equilibrift_dataset.csv")
    calc = EquilibriftCalculator()
    print(calc.calculate_equilibrift(sample)[["equilibrift_index", "equilibrift_band"]].head(10).to_string(index=False))

    scenario = calc.simulate_policy(sample, channel="equilibrium_gap", reduction=0.15)
    print("\nPolicy Scenario Mean Index:")
    print(float(scenario["equilibrift_index"].mean()))

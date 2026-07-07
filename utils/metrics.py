"""
metrics.py
----------

This module calculates all dashboard metrics for
the AMR Insight application.

Author: Sris
Project: AMR Insight
"""

import pandas as pd


def calculate_metrics(df: pd.DataFrame) -> dict:
    """
    Calculate dashboard metrics.

    Parameters
    ----------
    df : pandas.DataFrame
        Filtered dataset.

    Returns
    -------
    dict
        Dictionary containing all dashboard metrics.
    """

    total_samples = len(df)

    total_organisms = df["Organism"].nunique()

    total_antibiotics = df["Antibiotic"].nunique()

    total_sample_types = df["Sample_Type"].nunique()

    resistant_samples = len(
        df[df["Result"] == "R"]
    )

    sensitive_samples = len(
        df[df["Result"] == "S"]
    )

    intermediate_samples = len(
        df[df["Result"] == "I"]
    )

    if total_samples == 0:
        resistance_percentage = 0
    else:
        resistance_percentage = (
            resistant_samples / total_samples
        ) * 100

    metrics = {
        "total_samples": total_samples,
        "total_organisms": total_organisms,
        "total_antibiotics": total_antibiotics,
        "total_sample_types": total_sample_types,
        "resistant_samples": resistant_samples,
        "sensitive_samples": sensitive_samples,
        "intermediate_samples": intermediate_samples,
        "resistance_percentage": resistance_percentage,
    }

    return metrics
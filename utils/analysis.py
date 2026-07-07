"""
analysis.py
-----------

This module performs statistical analysis on the
Antimicrobial Resistance dataset.

Author: Sris
Project: AMR Insight
"""

import pandas as pd


def generate_analysis(df: pd.DataFrame) -> dict:
    """
    Generate key AMR statistics from the filtered dataset.

    Parameters
    ----------
    df : pandas.DataFrame

    Returns
    -------
    dict
        Dictionary containing important analysis results.
    """

    # ------------------------------------------
    # Empty dataset check
    # ------------------------------------------

    if df.empty:

        return {
            "most_resistant_organism": "N/A",
            "most_tested_antibiotic": "N/A",
            "most_common_sample": "N/A",
            "average_age": 0,
            "male_patients": 0,
            "female_patients": 0,
        }

    # ------------------------------------------
    # Most Resistant Organism
    # ------------------------------------------

    resistant_df = df[df["Result"] == "R"]

    if resistant_df.empty:
        most_resistant = "No Resistant Isolates"
    else:
        most_resistant = (
            resistant_df["Organism"]
            .value_counts()
            .idxmax()
        )

    # ------------------------------------------
    # Most Tested Antibiotic
    # ------------------------------------------

    most_antibiotic = (
        df["Antibiotic"]
        .value_counts()
        .idxmax()
    )

    # ------------------------------------------
    # Most Common Sample
    # ------------------------------------------

    most_sample = (
        df["Sample_Type"]
        .value_counts()
        .idxmax()
    )

    # ------------------------------------------
    # Average Patient Age
    # ------------------------------------------

    average_age = round(df["Age"].mean(), 1)

    # ------------------------------------------
    # Gender Counts
    # ------------------------------------------

    male_patients = len(
        df[df["Gender"] == "Male"]
    )

    female_patients = len(
        df[df["Gender"] == "Female"]
    )

    # ------------------------------------------
    # Return Dictionary
    # ------------------------------------------

    return {

        "most_resistant_organism": most_resistant,

        "most_tested_antibiotic": most_antibiotic,

        "most_common_sample": most_sample,

        "average_age": average_age,

        "male_patients": male_patients,

        "female_patients": female_patients,
    }
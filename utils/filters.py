"""
filters.py: This module creates the sidebar filters and returns the filtered dataset.
"""

import streamlit as st
import pandas as pd


def apply_filters(df: pd.DataFrame) -> pd.DataFrame:

    st.sidebar.title("🦠 AMR Insight")

    st.sidebar.markdown(
        "### Interactive Antibiotic Resistance Surveillance Dashboard"
    )

    st.sidebar.markdown("---")

    st.sidebar.header("🔍 Filters")

    
    # Organism Filter
    organism = st.sidebar.selectbox(
        "Select Organism",
        ["All"] + sorted(df["Organism"].unique())
    )

    
    # Antibiotic Filter
    antibiotic = st.sidebar.selectbox(
        "Select Antibiotic",
        ["All"] + sorted(df["Antibiotic"].unique())
    )

   
    # Sample Type Filter
    sample = st.sidebar.selectbox(
        "Select Sample Type",
        ["All"] + sorted(df["Sample_Type"].unique())
    )

   
    # Result Filter
    result = st.sidebar.selectbox(
        "Select Result",
        ["All", "S", "I", "R"]
    )

    st.sidebar.markdown("---")

    st.sidebar.info(
        "Use these filters to explore antimicrobial resistance patterns."
    )

    
    # Apply Filters
    filtered_df = df.copy()

    if organism != "All":
        filtered_df = filtered_df[
            filtered_df["Organism"] == organism
        ]

    if antibiotic != "All":
        filtered_df = filtered_df[
            filtered_df["Antibiotic"] == antibiotic
        ]

    if sample != "All":
        filtered_df = filtered_df[
            filtered_df["Sample_Type"] == sample
        ]

    if result != "All":
        filtered_df = filtered_df[
            filtered_df["Result"] == result
        ]

    return filtered_df

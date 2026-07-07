"""
export.py
---------

This module handles exporting the filtered dataset.

Author: Sristanka
Project: AMR Insight
"""

import streamlit as st
import pandas as pd


def download_csv(df: pd.DataFrame):
    """
    Display a download button for the filtered dataset.
    """

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 Download Filtered Dataset",
        data=csv,
        file_name="filtered_amr_data.csv",
        mime="text/csv",
        use_container_width=True
    )
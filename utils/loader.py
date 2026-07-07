"""
loader.py
----------

This module is responsible for loading the AMR dataset.

Author: Sris
Project: AMR Insight
"""

import pandas as pd
import streamlit as st


@st.cache_data
def load_data(file_path: str) -> pd.DataFrame:
    """
    Load the antimicrobial resistance dataset.

    Parameters
    ----------
    file_path : str
        Path to the CSV dataset.

    Returns
    -------
    pandas.DataFrame
        Loaded dataset.
    """

    try:
        df = pd.read_csv(file_path)

        # Remove duplicate rows (if any)
        df = df.drop_duplicates()

        # Remove leading/trailing spaces from column names
        df.columns = df.columns.str.strip()

        return df

    except FileNotFoundError:
        st.error(f"Dataset not found: {file_path}")
        st.stop()

    except pd.errors.EmptyDataError:
        st.error("The dataset is empty.")
        st.stop()

    except Exception as e:
        st.error(f"Unexpected Error: {e}")
        st.stop()
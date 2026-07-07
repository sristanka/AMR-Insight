"""
charts.py
---------

This module contains all Plotly visualizations used
in the AMR Insight dashboard.

Author: Sris
Project: AMR Insight
"""

import pandas as pd
import plotly.express as px


# ==========================================================
# Result Distribution Pie Chart
# ==========================================================

def create_result_pie_chart(df: pd.DataFrame):
    """
    Create a pie chart showing
    Sensitive, Intermediate and Resistant isolates.
    """

    result_counts = df["Result"].value_counts()

    fig = px.pie(
        values=result_counts.values,
        names=result_counts.index,
        hole=0.45,
        title="Distribution of Antibiotic Susceptibility Results"
    )

    fig.update_traces(
        textposition="inside",
        textinfo="percent+label"
    )

    return fig


# ==========================================================
# Organism Distribution
# ==========================================================

def create_organism_chart(df: pd.DataFrame):
    """
    Create bar chart showing number of isolates
    for each organism.
    """

    organism_counts = (
        df["Organism"]
        .value_counts()
        .sort_values(ascending=False)
    )

    fig = px.bar(
        x=organism_counts.index,
        y=organism_counts.values,
        labels={
            "x": "Organism",
            "y": "Number of Samples"
        },
        title="Samples per Organism"
    )

    return fig


# ==========================================================
# Antibiotic Distribution
# ==========================================================

def create_antibiotic_chart(df: pd.DataFrame):
    """
    Create bar chart showing how many
    times each antibiotic was tested.
    """

    antibiotic_counts = (
        df["Antibiotic"]
        .value_counts()
        .sort_values(ascending=False)
    )

    fig = px.bar(
        x=antibiotic_counts.index,
        y=antibiotic_counts.values,
        labels={
            "x": "Antibiotic",
            "y": "Number of Tests"
        },
        title="Antibiotic Testing Frequency"
    )

    return fig


# ==========================================================
# Sample Type Distribution
# ==========================================================

def create_sample_type_chart(df: pd.DataFrame):
    """
    Create bar chart for sample type distribution.
    """

    sample_counts = (
        df["Sample_Type"]
        .value_counts()
        .sort_values(ascending=False)
    )

    fig = px.bar(
        x=sample_counts.index,
        y=sample_counts.values,
        labels={
            "x": "Sample Type",
            "y": "Number of Samples"
        },
        title="Clinical Sample Distribution"
    )

    return fig


# ==========================================================
# Gender Distribution
# ==========================================================

def create_gender_chart(df: pd.DataFrame):
    """
    Create gender distribution chart.
    """

    gender_counts = df["Gender"].value_counts()

    fig = px.bar(
        x=gender_counts.index,
        y=gender_counts.values,
        labels={
            "x": "Gender",
            "y": "Patients"
        },
        title="Gender Distribution"
    )

    return fig


# ==========================================================
# Age Distribution
# ==========================================================

def create_age_histogram(df: pd.DataFrame):
    """
    Create histogram showing patient age distribution.
    """

    fig = px.histogram(
        df,
        x="Age",
        nbins=10,
        title="Age Distribution of Patients"
    )

    return fig


# ==========================================================
# Resistance Heatmap
# ==========================================================

def create_resistance_heatmap(df: pd.DataFrame):
    """
    Create a heatmap showing the number of resistant (R)
    isolates for each organism-antibiotic combination.
    """

    resistant_df = df[df["Result"] == "R"]

    heatmap_data = pd.crosstab(
        resistant_df["Organism"],
        resistant_df["Antibiotic"]
    )

    fig = px.imshow(
        heatmap_data,
        text_auto=True,
        aspect="auto",
        color_continuous_scale="Reds",
        labels=dict(
            x="Antibiotic",
            y="Organism",
            color="Resistant\nCount"
        ),
        title="Organism vs Antibiotic Resistance Heatmap"
    )

    return fig
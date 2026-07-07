import streamlit as st

from utils.loader import load_data
from utils.filters import apply_filters
from utils.metrics import calculate_metrics
from utils.charts import (
    create_result_pie_chart,
    create_organism_chart,
    create_antibiotic_chart,
    create_sample_type_chart,
    create_gender_chart,
    create_age_histogram,
    create_resistance_heatmap
)
from utils.analysis import generate_analysis
from utils.export import download_csv


# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="AMR Insight",
    page_icon="🦠",
    layout="wide"
)


# ==========================================================
# LOAD DATA
# ==========================================================

df = load_data("data/amr_data.csv")


# ==========================================================
# SIDEBAR FILTERS
# ==========================================================

filtered_df = apply_filters(df)


# ==========================================================
# CALCULATE METRICS
# ==========================================================

metrics = calculate_metrics(filtered_df)

analysis = generate_analysis(filtered_df)


# ==========================================================
# TITLE
# ==========================================================

st.title("🦠 AMR Insight")

st.subheader("Interactive Antimicrobial Resistance Surveillance Dashboard")

st.markdown("---")


# ==========================================================
# DASHBOARD METRICS
# ==========================================================

st.header("📊 Dashboard Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("🧪 Samples", metrics["total_samples"])

with col2:
    st.metric("🦠 Organisms", metrics["total_organisms"])

with col3:
    st.metric("💊 Antibiotics", metrics["total_antibiotics"])

with col4:
    st.metric(
        "📈 Resistance Rate",
        f"{metrics['resistance_percentage']:.1f}%"
    )

st.markdown("---")


# ==========================================================
# RESULT SUMMARY
# ==========================================================

st.header("🧾 Susceptibility Summary")

col1, col2, col3 = st.columns(3)

with col1:
    st.success(
        f"Sensitive (S): {metrics['sensitive_samples']}"
    )

with col2:
    st.warning(
        f"Intermediate (I): {metrics['intermediate_samples']}"
    )

with col3:
    st.error(
        f"Resistant (R): {metrics['resistant_samples']}"
    )

st.markdown("---")


# ==========================================================
# CHARTS
# ==========================================================

st.header("📊 Visual Analytics")

st.plotly_chart(
    create_result_pie_chart(filtered_df),
    use_container_width=True
)

st.plotly_chart(
    create_organism_chart(filtered_df),
    use_container_width=True
)

st.plotly_chart(
    create_antibiotic_chart(filtered_df),
    use_container_width=True
)

st.plotly_chart(
    create_sample_type_chart(filtered_df),
    use_container_width=True
)

st.plotly_chart(
    create_gender_chart(filtered_df),
    use_container_width=True
)

st.plotly_chart(
    create_age_histogram(filtered_df),
    use_container_width=True
)

st.plotly_chart(
    create_resistance_heatmap(filtered_df),
    use_container_width=True
)

st.markdown("---")


# ==========================================================
# ANALYSIS
# ==========================================================

st.header("🔬 Dataset Insights")

col1, col2 = st.columns(2)

with col1:

    st.info(
        f"**Most Resistant Organism:** "
        f"{analysis['most_resistant_organism']}"
    )

    st.info(
        f"**Most Tested Antibiotic:** "
        f"{analysis['most_tested_antibiotic']}"
    )

    st.info(
        f"**Most Common Sample:** "
        f"{analysis['most_common_sample']}"
    )

with col2:

    st.info(
        f"**Average Patient Age:** "
        f"{analysis['average_age']} years"
    )

    st.info(
        f"**Male Patients:** "
        f"{analysis['male_patients']}"
    )

    st.info(
        f"**Female Patients:** "
        f"{analysis['female_patients']}"
    )

st.markdown("---")


# ==========================================================
# DATASET PREVIEW
# ==========================================================

st.header("📋 Dataset Preview")

st.dataframe(
    filtered_df,
    use_container_width=True
)

st.markdown("---")


# ==========================================================
# DOWNLOAD
# ==========================================================

st.header("📥 Export Data")

download_csv(filtered_df)

st.markdown("---")

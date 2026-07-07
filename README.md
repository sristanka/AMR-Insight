# 🦠 AMR Insight

An interactive **Antimicrobial Resistance (AMR) Surveillance Dashboard** built using **Python, Pandas, Plotly, and Streamlit**.

The application enables users to explore antimicrobial resistance datasets through interactive visualizations, statistical summaries, and filtering capabilities, making AMR data easier to understand and analyze.

---

## 📖 Overview

Antimicrobial Resistance (AMR) is one of the biggest challenges in modern healthcare. Monitoring resistance patterns helps researchers and healthcare professionals understand trends in bacterial resistance against antibiotics.

AMR Insight provides a simple, interactive dashboard for exploring antimicrobial resistance datasets.

---

## ✨ Features

- 📊 Interactive Dashboard
- 📈 Resistance Rate Calculation
- 🦠 Organism Distribution
- 💊 Antibiotic Distribution
- 🥧 Susceptibility Result Pie Chart
- 🔥 Resistance Heatmap
- 📅 Filter by Collection Date
- 🧪 Filter by Organism
- 💊 Filter by Antibiotic
- 📋 Dataset Preview
- 📥 Export Filtered Dataset as CSV

---

## 📂 Project Structure

```text
AMR_Insight/
│
├── app.py
│
├── data/
│   ├── amr_data.csv
│   └── generate_dataset.py
│
├── utils/
│   ├── loader.py
│   ├── filters.py
│   ├── metrics.py
│   ├── charts.py
│   ├── analysis.py
│   └── export.py
│
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- Plotly
- NumPy

---

## 📊 Dashboard Analytics

The dashboard provides:

- Total Samples
- Number of Organisms
- Number of Antibiotics
- Resistance Percentage
- Sensitive / Intermediate / Resistant Counts
- Organism Distribution
- Antibiotic Distribution
- Sample Type Distribution
- Gender Distribution
- Age Distribution
- Resistance Heatmap

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/AMR_Insight.git
```

Move into the project directory:

```bash
cd AMR_Insight
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## 📸 Screenshots

Screenshots will be added after project completion.

---

## 🔮 Future Improvements

- Upload custom AMR datasets
- PDF report generation
- Advanced statistical analysis
- Machine learning-based resistance prediction
- Geographic resistance visualization

---

## 👨‍💻 Author

**Sris**

Biotechnology Undergraduate | Bioinformatics Enthusiast

---

## 📜 License

This project is licensed under the MIT License.
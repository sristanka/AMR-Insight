import pandas as pd
import random
from datetime import datetime, timedelta

# Make the random data reproducible
random.seed(42)

# List of bacterial organisms
organisms = [
    "Escherichia coli",
    "Klebsiella pneumoniae",
    "Staphylococcus aureus",
    "Pseudomonas aeruginosa",
    "Acinetobacter baumannii",
    "Enterococcus faecalis"
]

# List of antibiotics
antibiotics = [
    "Ampicillin",
    "Amoxicillin",
    "Ceftriaxone",
    "Ciprofloxacin",
    "Gentamicin",
    "Amikacin",
    "Meropenem",
    "Vancomycin",
    "Linezolid",
    "Piperacillin-Tazobactam"
]

# Sample types
sample_types = [
    "Blood",
    "Urine",
    "Sputum",
    "Wound Swab",
    "CSF"
]

# Gender
genders = ["Male", "Female"]

# Results
results = ["S", "I", "R"]  # Sensitive, Intermediate, Resistant

# Resistance probability for each organism
# Format = [Sensitive, Intermediate, Resistant]
probabilities = {
    "Escherichia coli": [0.45, 0.10, 0.45],
    "Klebsiella pneumoniae": [0.35, 0.10, 0.55],
    "Staphylococcus aureus": [0.55, 0.10, 0.35],
    "Pseudomonas aeruginosa": [0.25, 0.10, 0.65],
    "Acinetobacter baumannii": [0.20, 0.10, 0.70],
    "Enterococcus faecalis": [0.60, 0.10, 0.30]
}

records = []

start_date = datetime(2025, 1, 1)

# Generate 1000 records
for i in range(1, 1001):

    organism = random.choice(organisms)
    antibiotic = random.choice(antibiotics)

    result = random.choices(
        results,
        weights=probabilities[organism]
    )[0]

    age = random.randint(1, 90)

    gender = random.choice(genders)

    sample = random.choice(sample_types)

    date = start_date + timedelta(days=random.randint(0, 364))

    records.append({
        "Patient_ID": f"P{i:04d}",
        "Age": age,
        "Gender": gender,
        "Sample_Type": sample,
        "Organism": organism,
        "Antibiotic": antibiotic,
        "Result": result,
        "Collection_Date": date.strftime("%Y-%m-%d")
    })

# Create DataFrame
df = pd.DataFrame(records)

# Save CSV
df.to_csv("amr_data.csv", index=False)

print("===================================")
print(" Dataset Generated Successfully!")
print("===================================")
print(f"Total Records: {len(df)}")
print()
print(df.head())
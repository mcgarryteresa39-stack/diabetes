import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency

# Load data
df = pd.read_csv("diabetes.csv")

binary_vars = [
    'HighBP',
    'HighChol',
    'Stroke',
    'HeartDiseaseorAttack',
    'PhysActivity',
    'Smoker',
    'Fruits',
    'Veggies',
    'HvyAlcoholConsump',
    'Sex',
    'Education'
]

def cramers_v(confusion_matrix):
    chi2, p, dof, expected = chi2_contingency(confusion_matrix)
    n = confusion_matrix.sum().sum()
    r, k = confusion_matrix.shape
    if n == 0 or min(r-1, k-1) == 0:
        return np.nan
    return np.sqrt(chi2 / (n * min(r-1, k-1)))

print("Chi-square tests of association vs Diabetes_012\n")
for var in binary_vars:
    if var not in df.columns:
        print(f"{var}: NOT IN DATA\n")
        continue
    # Build contingency table
    ct = pd.crosstab(df[var], df['Diabetes_012'])
    if ct.size == 0:
        print(f"{var}: empty crosstab\n")
        continue
    try:
        chi2, p, dof, expected = chi2_contingency(ct)
        cv = cramers_v(ct)
        print(f"Variable: {var}")
        print(ct)
        print(f"chi2 = {chi2:.4f}, p = {p:.4e}, dof = {dof}, Cramer's V = {cv:.4f}\n")
    except Exception as e:
        print(f"Error testing {var}: {e}\n")

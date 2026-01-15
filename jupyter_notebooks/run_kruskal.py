import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import kruskal

# Load data
df = pd.read_csv("diabetes.csv")

# Prepare BMI_Category_Code
bmi_order = ['Underweight', 'Normal Weight', 'Overweight', 'Obese']
bmi_map = {k: i+1 for i, k in enumerate(bmi_order)}
if 'BMI_Category' in df.columns:
    df['BMI_Category_Code'] = df['BMI_Category'].map(bmi_map)
else:
    conditions = [
        df['BMI'] <= 18.5,
        (df['BMI'] > 18.5) & (df['BMI'] <= 24.8),
        (df['BMI'] >= 25) & (df['BMI'] <= 29.9),
        df['BMI'] >= 30,
    ]
    values = ['Underweight', 'Normal Weight', 'Overweight', 'Obese']
    df['BMI_Category'] = np.select(conditions, values, default=np.nan)
    df['BMI_Category_Code'] = df['BMI_Category'].map(bmi_map)

vars_to_test = ['GenHlth', 'BMI', 'BMI_Category_Code']
alpha = 0.05
labels = sorted(df['Diabetes_012'].dropna().unique())

results = []
for var in vars_to_test:
    groups = [df.loc[df['Diabetes_012'] == g, var].dropna() for g in labels]
    non_empty = [grp for grp in groups if len(grp) > 0]
    if len(non_empty) < 2:
        out = f"Not enough non-empty groups for {var} - skipping"
        print(out)
        results.append((var, None, None, out))
        continue
    stat, p = kruskal(*non_empty)
    medians = {int(lbl): df.loc[df['Diabetes_012']==lbl, var].median() for lbl in labels}
    sig = 'reject H0' if p < alpha else 'fail to reject H0'
    out = f"{var}: H={stat:.4f}, p={p:.4e} -> {sig}; medians={medians}"
    print(out)
    results.append((var, stat, p, medians))

# Save boxplots to files and list filenames
plot_files = []
for var in vars_to_test:
    try:
        plt.figure(figsize=(6,4))
        sns.boxplot(x='Diabetes_012', y=var, data=df)
        plt.title(f"Boxplot of {var} by Diabetes_012")
        plt.tight_layout()
        fname = f"boxplot_{var}.png".replace(' ', '_')
        plt.savefig(fname)
        plt.close()
        plot_files.append(fname)
    except Exception as e:
        print(f"Could not create boxplot for {var}: {e}")

print('\nSaved plots:', plot_files)

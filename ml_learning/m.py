# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# %%
df_data = pd.read_csv("/home/parrot/Documents/machine_learning/datasets/kidney_disease.csv")

# %%
df_data = df_data.drop(columns=['id'])

# %%
df_data.columns = [
    'age','blood_pressure','specific_gravity','albumin','sugar',
    'red_blood_cells','pus_cell','pus_cell_clumps','bacteria',
    'blood_glucose_random','blood_urea','serum_creatinine','sodium',
    'potassium','haemoglobin','packed_cell_volume',
    'white_blood_cell_count','red_blood_cell_count','hypertension',
    'diabetes_mellitus','coronary_artery_disease','appetite',
    'peda_edema','anemia','class'
]

# %%
# Convert known numeric columns
num_fix_cols = [
    'packed_cell_volume',
    'white_blood_cell_count',
    'red_blood_cell_count'
]

for col in num_fix_cols:
    df_data[col] = pd.to_numeric(df_data[col], errors='coerce')

# %%
# Clean string columns FIRST
for col in df_data.select_dtypes(include='object').columns:
    df_data[col] = (
        df_data[col]
        .astype(str)
        .str.strip()
        .str.lower()
        .str.replace('\t', '', regex=False)
    )

# %%
# Fix inconsistent labels
df_data['diabetes_mellitus'] = df_data['diabetes_mellitus'].replace({' yes':'yes'})
df_data['coronary_artery_disease'] = df_data['coronary_artery_disease'].replace({'\tno':'no'})
df_data['class'] = df_data['class'].replace({'ckd\t':'ckd', 'notckd':'notckd', 'not ckd':'notckd'})

# %%
# Imputation functions
def mean_value_imputation(df_data, column):
    df_data[column] = df_data[column].fillna(df_data[column].mean())

def mode_value_imputation(df_data, column):
    df_data[column] = df_data[column].fillna(df_data[column].mode()[0])

# %%
# Apply imputation
num_col = [col for col in df_data.columns if df_data[col].dtype != 'object']
cat_col = [col for col in df_data.columns if df_data[col].dtype == 'object']

for col in num_col:
    mean_value_imputation(df_data, col)

for col in cat_col:
    mode_value_imputation(df_data, col)

# %%
# Encode categorical variables
df_data['class'] = df_data['class'].map({'ckd': 1, 'notckd': 0})

df_data['red_blood_cells'] = df_data['red_blood_cells'].map({'normal': 1, 'abnormal': 0})
df_data['pus_cell'] = df_data['pus_cell'].map({'normal': 1, 'abnormal': 0})
df_data['pus_cell_clumps'] = df_data['pus_cell_clumps'].map({'present': 1, 'notpresent': 0})
df_data['bacteria'] = df_data['bacteria'].map({'present': 1, 'notpresent': 0})
df_data['hypertension'] = df_data['hypertension'].map({'yes': 1, 'no': 0})
df_data['diabetes_mellitus'] = df_data['diabetes_mellitus'].map({'yes': 1, 'no': 0})
df_data['coronary_artery_disease'] = df_data['coronary_artery_disease'].map({'yes': 1, 'no': 0})
df_data['appetite'] = df_data['appetite'].map({'good': 1, 'poor': 0})
df_data['peda_edema'] = df_data['peda_edema'].map({'yes': 1, 'no': 0})
df_data['anemia'] = df_data['anemia'].map({'yes': 1, 'no': 0})

# %%
# Final NaN check
print(df_data.isnull().sum())

# %%
df_data.head()

# %%
# Correlation heatmap (numeric only)
plt.figure(figsize=(16, 10))
sns.heatmap(df_data.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
plt.show()

# %%
# Target correlation
target_corr = df_data.corr()['class'].abs().sort_values(ascending=False)[1:]
print(target_corr)

# %%
print(df_data['class'].unique())

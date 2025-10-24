#
# Sefty, 2025/10/22
# File: Sefty_Correlation_Analysis.py
# Apply correlation analysis to business problems
#

# Data Manipulation and Analysis
import pandas as pd
import numpy as np

# Data Visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Statistical Analysis
from scipy import stats

# 1. Input
# Read the CSV file
df = pd.read_csv('Correlataion_Analysis_Data.csv')
df.info()

# 2. Process
correlation_matrix = df.iloc[:,1:6].corr()
print(correlation_matrix.round(3))

# 3. Output
# print('Data loaded successfully!')
# print(f'Datset shape : {df.shape}')
sns.heatmap(correlation_matrix)
plt.title('Sefty is the most intelligent person in the world')
plt.tight_layout()
plt.show()


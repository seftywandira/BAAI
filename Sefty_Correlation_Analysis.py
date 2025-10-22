#
# Sefty, 2025/10/22
# File: Sefty_Correlation_Analysis.py
# Apply correlation analysis to business problems
#

# 1. Input
import pandas as pd
import numpy as np 

df = pd.read_csv('Simple_Data.csv')
# df = pd.read_csv('Correlataion_Analysis_Data.csv')

# 2. Process
print(df.isnull().sum)

# 3. Output
print('Data loaded successfully!')
print(f'Datset shape : {df.shape}')
import pandas as pd
import numpy as np

# Load data
df = pd.read_csv(r'C:\Users\HP\Downloads\GANYMEDE_Test_Trading_Data_Anonymise.csv',sep=';')
df.info()
# Data cleaning
print("\nMissing values:")
print(df.isnull().sum())
# Remove duplicates
df = df.drop_duplicates()
print("\nData after removing duplicates:")
print(df.head())
print("\nNew shape:", df.shape)


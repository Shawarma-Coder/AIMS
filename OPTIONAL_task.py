import pandas as pd
import numpy as np

# Sample DataFrame
df = pd.read_csv('cars.csv')

# 1. Ordinal Encoding
def ordinal_encoding(df, column):
    unique_values = df[column].unique()
    ordinal_map = {}
    
    # assign integers to each unique category
    idx = 0
    for value in unique_values:
        ordinal_map[value] = idx
        idx += 1
    
    # Create a new column 
    ordinal_encoded = []
    for val in df[column]:
        ordinal_encoded.append(ordinal_map[val])
    
    # Assign values to the new column
    df[column + '_ordinal'] = ordinal_encoded
    return df

# 2. One-Hot Encoding
def one_hot_encoding(df, column):
    unique_values = df[column].unique()
    for value in unique_values:
        
        #where checks if the condition is true for the value in the series if true 2nd param is used else 3rd is used
        
        df[column + '_' + str(value)] = np.where(df[column] == value, 1, 0)
    return df


df.head()

# Applying ordinal encoding
df = ordinal_encoding(df, 'fuel')

# Applying one-hot encoding
df = one_hot_encoding(df, 'brand')

# Display the DataFrame
print(df)

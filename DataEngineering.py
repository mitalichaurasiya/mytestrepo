#Handling Missing Values (NaN - Not a Number):
import numpy as np # Used for NaN
import pandas as pd # Added pandas import

'''data_with_nan = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, np.nan, 35, 28],
    'City': ['New York', 'Los Angeles', np.nan, 'Houston']
}
df_nan = pd.DataFrame(data_with_nan)
print("\nOriginal DataFrame with NaNs:")
print(df_nan)

##Check for missing values
print("\nMissing values (True if missing):")
print(df_nan.isnull())

# Drop rows with any missing values
df_dropped_rows = df_nan.dropna()
print("\nDataFrame after dropping rows with NaNs:")
print(df_dropped_rows)

# Fill missing values (e.g., with a specific value, mean, or median)
df_filled_age = df_nan['Age'].fillna(df_nan['Age'].mean())
df_filled = df_nan.copy() # Create a copy to avoid modifying original df_nan
df_filled['Age'] = df_filled_age
df_filled['City'].fillna('Unknown', inplace=True) # Fill 'City' NaNs with 'Unknown'
print("\nDataFrame after filling NaNs:")
print(df_filled)'''





#Handling Duplicates:
data_with_duplicates = {
    'ID': [1, 2, 3, 1, 4],
    'Value': ['A', 'B', 'C', 'A', 'D']
}
df_dup = pd.DataFrame(data_with_duplicates)
print("\nOriginal DataFrame with duplicates:")
print(df_dup)

# Check for duplicates
print("\nDuplicate rows (True if duplicate):")
print(df_dup.duplicated())

# Drop duplicate rows (keeps the first occurrence by default)
df_no_duplicates = df_dup.drop_duplicates()
print("\nDataFrame after dropping duplicates:")
print(df_no_duplicates)

# Drop duplicates based on a specific column (e.g., 'ID')
df_no_duplicates_id = df_dup.drop_duplicates(subset=['ID'])
print("\nDataFrame after dropping duplicates based on 'ID':")
print(df_no_duplicates_id)
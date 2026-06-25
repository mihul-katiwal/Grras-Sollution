# # Handling Null Values in DataFrame

# import pandas as pd

# data = {
#     "Name": ["Mihul", "Mayank", "Mohammed"],
#     "Age": [20, None , 18],
#     "Salary": [5000, 6000, None] 
# }

# df = pd.DataFrame(data)
# print("Original DataFrame")
# print(df)

# # null findout | fillna | dropna

# print("\nNull Values Count in DataFrame")
# null_counts = df.isnull().sum()
# print(null_counts)

# print("\nNull Values in DataFrame")
# print(df.isnull())

# print("\nDataFrame after filling null values with mean")
# df_filled = df.fillna(df.mean(numeric_only=True))
# print(df_filled)

# print("\nDataFrame after dropping rows with null values")
# df_dropped = df.dropna()
# print(df_dropped)



# # Encoding Categorical Variables

# from sklearn.preprocessing import LabelEncoder
# import pandas as pd

# data = {
#     "Name": ["Mihul", "Mayank", "Mohammed", "Divya", "Manya", "Priya"],
#     "Age": [20, None, 18, 19, 20, 18],
#     "Salary": [5000, 6000, None, 7000, 8000, 9000],
#     "Gender": ["Male", "Male", "Male", None ,"Female", "Female"]
# }

# df = pd.DataFrame(data)
# print("Original DataFrame")
# print(df)

# # Label Encoding

# le = LabelEncoder()

# df_label = df.copy()

# df_label['Gender'] = df['Gender'].fillna('Unknown')  
# df_label['Gender_Encoded'] = le.fit_transform(df_label['Gender'])
# print("\nDataFrame after Label Encoding")
# print(df_label)



# # One-Hot Encoding

# import pandas as pd
# data = {
#     "Color": ["Red", "Blue", "Green", "Red", "blue"],
# }

# df = pd.DataFrame(data)
# print("Original DataFrame")
# print(df)

# encoded_df = pd.get_dummies(df, columns=['Color'], prefix='Color')
# print("\nDataFrame after One-Hot Encoding")
# print(encoded_df)



# Handling Missing Values

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

data = {
    "Colors": ['Red', 'Green', 'Blue', 'Orange', 'Blue', np.nan]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Handling Null Values
df.dropna(inplace=True)
print("\nAfter Removing Null Values:")
print(df)

# Label Encoding

le = LabelEncoder()
df["Colors_Encoder_1"] = le.fit_transform(df["Colors"])

print("\nAfter Label Encoding:")
print(df)

# Method 2
df["Colors_Encoder_2"] = LabelEncoder().fit_transform(df["Colors"])
print(df)

# Method 3

import sklearn
df["Colors_Encoder_3"] = sklearn.preprocessing.LabelEncoder().fit_transform(df["Colors"])
print(df)



# One Hot Encoding

from sklearn.preprocessing import OneHotEncoder
print(df)

# Drop cols of Label Encoding

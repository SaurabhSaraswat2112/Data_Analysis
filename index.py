import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load CSV file
df = pd.read_csv("data.csv")

# Display first five rows
print(df.head())

# Dataset information
print(df.info())

# Summary statistics
print(df.describe())

# Check missing values
print(df.isnull().sum())

# Fill numerical columns with median
numeric_cols = df.select_dtypes(include=np.number).columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())

# Fill categorical columns with mode
categorical_cols = df.select_dtypes(include='object').columns
for col in categorical_cols:
    df[col] = df[col].fillna(df[col].mode()[0])


print("Duplicate rows:", df.duplicated().sum())

df = df.drop_duplicates()


for col in numeric_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    df = df[(df[col] >= lower) & (df[col] <= upper)]

df.to_csv("cleaned_data.csv", index=False)

print("Data cleaned successfully.")

df[numeric_cols[0]].hist(bins=20, color='skyblue')
plt.title("Distribution")
plt.xlabel(numeric_cols[0])
plt.ylabel("Frequency")
plt.show()

if len(categorical_cols) > 0:
    df[categorical_cols[0]].value_counts().plot(kind='bar', color='orange')
    plt.title("Category Counts")
    plt.xlabel(categorical_cols[0])
    plt.ylabel("Count")
    plt.show()

plt.boxplot(df[numeric_cols[0]])
plt.title("Box Plot")
plt.show()

if len(numeric_cols) >= 2:
    plt.scatter(df[numeric_cols[0]], df[numeric_cols[1]], color='green')
    plt.xlabel(numeric_cols[0])
    plt.ylabel(numeric_cols[1])
    plt.title("Scatter Plot")
    plt.show()
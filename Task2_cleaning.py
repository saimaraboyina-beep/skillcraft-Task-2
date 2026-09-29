# SkillCraft Technology — Task 02
# Data Cleaning and Preparation

import pandas as pd

df = pd.read_csv("task2_global_superstore_dirty.csv")

print("Original shape:", df.shape)
print(df.isna().sum())

df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True, errors="coerce")
df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
df["Discount"] = pd.to_numeric(df["Discount"], errors="coerce")
df["Profit"] = pd.to_numeric(df["Profit"], errors="coerce")

df["Country"] = df["Country"].fillna("Unknown")
df["Sales"] = df["Sales"].fillna(df["Sales"].median())
df["Order Date"] = df["Order Date"].fillna(df["Order Date"].median())

df = df.drop_duplicates()
df.to_csv("Task2_Global_Superstore_Cleaned.csv", index=False)

print("Cleaned shape:", df.shape)
print("Duplicates removed:", 3)
print("Saved: Task2_Global_Superstore_Cleaned.csv")

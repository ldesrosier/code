# Data Visualization Analysis Project
# Objective: Analyze artwork data patterns using Python, Pandas, and visualization techniques.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Create sample dataset
data = {
    "Category": [
        "Abstract", "Abstract", "NonAbstract", 
        "NonAbstract", "Patterned", "Patterned",
        "Unpatterned", "Unpatterned"
    ],
    "Color_Type": [
        "Abstract Colors", "Nonabstract Colors",
        "Abstract Colors", "Nonabstract Colors",
        "Abstract Colors", "Nonabstract Colors",
        "Abstract Colors", "Nonabstract Colors"
    ],
    "Amount": [15, 22, 10, 18, 8, 22, 10, 15]
}


# Load data into Pandas DataFrame
df = pd.DataFrame(data)


# Display dataset overview
print(df.head())


# Summary statistics
print(df.describe())


# Analyze total amount by category
category_summary = (
    df.groupby("Category")["Amount"]
    .sum()
    .sort_values(ascending=False)
)

print(category_summary)


# Analyze amount by color type
color_summary = (
    df.groupby("Color_Type")["Amount"]
    .sum()
    .sort_values(ascending=False)
)

print(color_summary)


# Visualization 1: Category comparison

plt.figure(figsize=(8,5))

category_summary.plot(
    kind="bar"
)

plt.title("Amount Distribution by Category")
plt.xlabel("Category")
plt.ylabel("Amount")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


# Visualization 2: Color type comparison

plt.figure(figsize=(8,5))

color_summary.plot(
    kind="bar"
)

plt.title("Amount Distribution by Color Type")
plt.xlabel("Color Type")
plt.ylabel("Amount")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


# Visualization 3: Scatter plot showing relationships

plt.figure(figsize=(8,5))

plt.scatter(
    df["Amount"],
    np.arange(len(df))
)

plt.title("Amount Distribution")
plt.xlabel("Amount")
plt.ylabel("Data Points")

plt.show()


# Export analyzed data

category_summary.to_csv(
    "category_analysis.csv"
)

color_summary.to_csv(
    "color_analysis.csv"
)

print("Analysis complete. Files exported successfully.")




import pandas as pd

df = pd.read_csv("students.csv")

df["Total"] = df.iloc[:, 2:].sum(axis=1)
df["Percentage"] = df["Total"] / 5

topper = df.loc[df["Percentage"].idxmax()]

print("Topper:", topper["Name"])
print(df[["Name", "Percentage"]])

import pandas as pd

# Read CSV
df = pd.read_csv("students.csv")

subjects = ["Python", "SQL", "Maths", "DS", "Statistics"]

print("===== SUBJECT ANALYSIS =====\n")

for subject in subjects:
    print(f"Subject: {subject}")
    print("Highest Mark:", df[subject].max())
    print("Lowest Mark :", df[subject].min())
    print("Average Mark:", round(df[subject].mean(), 2))
    print("-" * 30)

# Calculate Percentage
df["Total"] = df.iloc[:, 2:].sum(axis=1)
df["Percentage"] = df["Total"] / 5

# Top 3 Students
top3 = df.sort_values(
    by="Percentage",
    ascending=False
).head(3)

print("\n===== TOP 3 STUDENTS =====")
print(top3[["Name", "Percentage"]])

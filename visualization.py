import pandas as pd
import matplotlib.pyplot as plt

# Read CSV data
df = pd.read_csv("students.csv")

# Calculate percentage
df["Total"] = df.iloc[:, 2:].sum(axis=1)
df["Percentage"] = df["Total"] / 5

# Create bar chart
plt.figure(figsize=(8,5))
plt.bar(df["Name"], df["Percentage"])

plt.title("Student Percentage Analysis")
plt.xlabel("Students")
plt.ylabel("Percentage")

plt.tight_layout()

plt.savefig("student_performance.png")

print("Chart saved as student_performance.png")

plt.show()

import pandas as pd

# Read CSV
df = pd.read_csv("students.csv")

# Calculate Total and Percentage
df["Total"] = df.iloc[:, 2:].sum(axis=1)
df["Percentage"] = df["Total"] / 5

# Grade Function
def grade(p):
    if p >= 90:
        return "A+"
    elif p >= 80:
        return "A"
    elif p >= 70:
        return "B+"
    elif p >= 60:
        return "B"
    else:
        return "C"

# Pass/Fail Function
def result(p):
    if p >= 40:
        return "PASS"
    else:
        return "FAIL"

# Apply Functions
df["Grade"] = df["Percentage"].apply(grade)
df["Result"] = df["Percentage"].apply(result)

print("===== STUDENT GRADE REPORT =====")
print(df[["Name","Percentage","Grade","Result"]])

# Save Report
df.to_csv("student_report.csv", index=False)

print("\nReport saved as student_report.csv")

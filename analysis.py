import pandas as pd

def analyze_results(file):
    df = pd.read_csv(file)

    df["Total"] = df.iloc[:, 2:].sum(axis=1)
    df["Percentage"] = df["Total"] / 5

    topper = df.loc[df["Percentage"].idxmax()]

    print("===== RESULT ANALYSIS =====")
    print("Topper:", topper["Name"])
    print("Percentage:", round(topper["Percentage"], 2))

    print("\nStudent Results:")
    print(df[["Name", "Percentage"]])

if __name__ == "__main__":
    analyze_results("students.csv")

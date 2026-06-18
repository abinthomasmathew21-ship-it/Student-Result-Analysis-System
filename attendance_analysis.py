import pandas as pd

df = pd.read_csv("attendance.csv")

print("Average Attendance:",
      round(df["Attendance"].mean(),2))

low = df[df["Attendance"] < 80]

print("\nLow Attendance Students:")
print(low)

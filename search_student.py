import pandas as pd

df = pd.read_csv("students.csv")

student = input("Enter Student Name: ")

result = df[df["Name"].str.lower() == student.lower()]

if len(result) > 0:
    print(result)
else:
    print("Student not found")

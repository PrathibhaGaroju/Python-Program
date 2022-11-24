#importing pandas package
import pandas as pd


data = pd.read_csv("nba.csv", index_col ="Name")

first = data.loc[["Age", "College", "Salary"]]

print(first)
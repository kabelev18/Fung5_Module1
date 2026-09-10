import pandas as pd

df = pd.read_csv("C:\\Users\\kabel\\OneDrive\\Desktop\\Comp BME\\Mod 1\\Fung5_Module1\\Metadata and Protein Data for Module 1.csv")

for header in df.columns:
    print(header)
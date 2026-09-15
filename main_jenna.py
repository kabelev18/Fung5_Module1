import pandas as pd

df= pd.read_csv("/Users/phong/Desktop/BME 2315/Mod 1/Metadata and Protein Data for Module 1.csv")

for header in df.columns:
    print(header)   

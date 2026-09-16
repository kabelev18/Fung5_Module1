# import code from class
import pandas as pd

df = pd.read_csv("C:\\Users\\kabel\\OneDrive\\Desktop\\Comp BME\\Mod 1\\Fung5_Module1\\Metadata and Protein Data for Module 1.csv")

for header in df.columns:
    print(header)

# creating a class to hold the patient data
from patient_katia import *

import matplotlib.pyplot as plt
import numpy as np
import statistics

Patient.instantiate_from_csv(r"C:\Users\kabel\OneDrive\Desktop\Comp BME\Mod 1\Fung5_Module1\Metadata and Protein Data for Module 1.csv")

for patient in Patient.all_patients:
    print(patient)

# sorting patients by age at death
Patient.all_patients.sort(key=Patient.get_age_at_death, reverse=False)

print("Patients sorted by age at death: ")
for patient in Patient.all_patients:
    print(patient)

# filter subset of patients based on 2 attributes: female patients with years of education > 12
female_educated_patients = Patient.filter(Patient.all_patients, sex="Female", years_of_ed=12)
print("Female patients with years of education > 12: ")

for patient in female_educated_patients:
    print(patient)

# making a bar graph of different Amyloid-Beta40 levels in Males vs. Females
female_amyloid = []
male_amyloid = []

for patient in Patient.all_patients:
    if patient.sex == "Female":
        female_amyloid.append(patient.ABeta40)
    if patient.sex == "Male":
        male_amyloid.append(patient.ABeta40)

# calculating the mean and standard deviation of Amyloid-Beta40 levels in Males vs. Females
female_mean = statistics.mean(female_amyloid)
male_mean = statistics.mean(male_amyloid)

female_stdev = statistics.stdev(female_amyloid)
male_stdev = statistics.stdev(male_amyloid)

# printing out the mean and standard deviation of Amyloid-Beta40 levels in Males vs. Females
print("Female Amyloid-Beta40 Mean: ")
print(f"Mean = {female_mean}")
print(f"Standard deviation = {female_stdev}")

print("Male Amyloid-Beta40 Mean: ")
print(f"Mean = {male_mean}")
print(f"Standard deviation = {male_stdev}")

# labeling the bar graph with error bars
sex_labels = ["Female", "Male"]
mean_sex = [female_mean, male_mean]
stdev_sex = [female_stdev, male_stdev]
yerr = [np.zeros(len(mean_sex)), stdev_sex]

# making a bar graph of different Amyloid-Beta40 levels in Males vs. Females
plt.bar(sex_labels, mean_sex, yerr=yerr, capsize=10)
plt.title("Average Amyloid-Beta40 Levels by Sex")
plt.xlabel("Sex")
plt.ylabel("Average Amyloid-Beta40 Levels")
plt.show()

# making a scatter plot of amyloid40 levels vs. age at death
amyloid40 = []
age_at_death = []

# making a scatter plot of amyloid40 levels vs. age at death
for patient in Patient.all_patients:
    amyloid40.append(patient.ABeta40)
    age_at_death.append(patient.age_at_death)

# making a scatter plot of amyloid40 levels vs. age at death
plt.scatter(amyloid40, age_at_death, color='blue')
plt.title("Amyloid-Beta40 Levels vs. Age at Death")
plt.xlabel("Amyloid-Beta40 Levels")
plt.ylabel("Age at Death")
plt.show()
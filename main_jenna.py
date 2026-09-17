import pandas as pd

df= pd.read_csv("/Users/phong/Desktop/BME 2315/Mod 1/Metadata and Protein Data for Module 1.csv")

for header in df.columns:
    print(header)   

from patient_jenna import *
import matplotlib.pyplot as plt
import numpy as np
import statistics
# Create Patient objects using the information stored in the CSV file
Patient.instantiate_from_csv(r"/Users/phong/Desktop/BME 2315/Mod 1/Metadata and Protein Data for Module 1.csv")


# Print the information stored for each patient
for patient in Patient.all_patients:
    print(patient)


# 5. Arrange the patients from the lowest to highest ABeta42 value
Patient.all_patients.sort(key=Patient.get_ABeta42, reverse=False)

print("Patients sorted by ABeta42:")

for patient in Patient.all_patients:
    print(patient)

# 6. Select patients who have a graduate degree and an APOE 4_4 genotype
graduate_APOE44_patients = Patient.filter(
    Patient.all_patients,
    highest_education="Graduate (PhD/Masters)",
    APOE_genotype="4_4"
)

print("Patients with Graduate (PhD/Masters) education and APOE 4_4:")

for patient in graduate_APOE44_patients:
    print(patient)


# 7. Separate pTAU measurements into female and male patient groups

female_pTAU = []
male_pTAU = []

for patient in Patient.all_patients:

    if patient.sex == "Female":
        female_pTAU.append(patient.pTAU)

    if patient.sex == "Male":
        male_pTAU.append(patient.pTAU)


# Calculate the average pTAU level for each sex
female_mean = statistics.mean(female_pTAU)
male_mean = statistics.mean(male_pTAU)
# Calculate how much the pTAU measurements vary within each group
female_stdev = statistics.stdev(female_pTAU)
male_stdev = statistics.stdev(male_pTAU)

# Display the calculated mean and standard deviation for each group
print("Female pTAU Mean:")
print(f"Mean = {female_mean}")
print(f"Standard deviation = {female_stdev}")

print("Male pTAU Mean:")
print(f"Mean = {male_mean}")
print(f"Standard deviation = {male_stdev}")


# Use the means and standard deviations to create the bar graph
sex_labels = ["Female", "Male"]
mean_sex = [female_mean, male_mean]
stdev_sex = [female_stdev, male_stdev]

# Add standard deviation error bars to show variation within each group
plt.bar(sex_labels, mean_sex, yerr=stdev_sex, capsize=10)

plt.title("Average pTAU Levels by Sex")
plt.xlabel("Sex")
plt.ylabel("Average pTAU Levels")

plt.show()


# 8. Scatter plot of pTAU vs. age at death

pTAU = []
age_at_death = []

for patient in Patient.all_patients:

    pTAU.append(patient.pTAU)
    age_at_death.append(patient.age_at_death)

# Plot pTAU levels against age at death for each patient
plt.scatter(pTAU, age_at_death)

plt.title("pTAU Levels vs. Age at Death")
plt.xlabel("pTAU Levels")
plt.ylabel("Age at Death")

plt.show()



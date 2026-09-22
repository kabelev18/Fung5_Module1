import csv

# Defines the Patient class and the information stored for each patient
class Patient:

    def __init__(self, patient_id, age_at_death, sex,
                 Highest_level_of_education, APOE_genotype,
                 last_CASI_score, ABeta42, pTAU):

        self.patient_id = patient_id
        self.age_at_death = age_at_death
        self.sex = sex
        self.Highest_level_of_education = Highest_level_of_education
        self.APOE_genotype = APOE_genotype
        self.last_CASI_score = last_CASI_score
        self.ABeta42 = ABeta42
        self.pTAU = pTAU
     # Adds the newly created patient to the class list of all patients
        Patient.all_patients.append(self)

    # formats the patient information of selected qualities for data analysis
    def __repr__(self):
        return f"{self.patient_id}: ({self.age_at_death} | {self.sex} | {self.Highest_level_of_education} | {self.APOE_genotype} | {self.last_CASI_score} | {self.ABeta42} | {self.pTAU})"

    # Returns the patient's ABeta42 value so patients can be sorted by this variable
    def get_ABeta42(self):
        return self.ABeta42

    # Stores every Patient object created from the dataset
    all_patients = []

    # Reads patient data from the CSV file and converts each row into a Patient object
    @classmethod
    def instantiate_from_csv(cls, filename: str):

        with open(filename, encoding="utf8") as f:
            reader = csv.DictReader(f)
            rows_of_patients = list(reader)
            # Processes each row of the dataset to create an individual patient
            for row in rows_of_patients:
                Patient(
                    patient_id=row['Donor ID'],
                    age_at_death=(row['Age at Death']),
                    sex=row['Sex'],
                    Highest_level_of_education=row['Highest level of education'],
                    APOE_genotype=row['APOE Genotype'],
                    last_CASI_score=(row['Last CASI Score']),
                    ABeta42=(row['ABeta42 pg/ug']),
                    pTAU=(row['pTAU pg/ug'])
                )

     # Returns patients that match the selected education and APOE genotype
    @classmethod
    def filter(cls, list, Highest_level_of_education="any", APOE_genotype="any"):

        all_patients = list
        remove_list = []
        # Identifies patients who do not meet the selected filtering criteria
        for patient in all_patients:
            if Highest_level_of_education != "any" and patient.Highest_level_of_education != Highest_level_of_education:
                remove_list.append(patient)

            elif APOE_genotype != "any" and patient.APOE_genotype != APOE_genotype:
                remove_list.append(patient)
        # Creates a new list containing only patients who meet the criteria
        all_patients = [patient for patient in all_patients if patient not in remove_list]

        return all_patients
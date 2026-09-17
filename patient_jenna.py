import csv

# Defines the Patient class and the information stored for each patient
class Patient:

    def __init__(self, patient_id: str, age_at_death: int, sex: str,
                 highest_education: str, APOE_genotype: str,
                 CASI_score: float, ABeta42: float, pTAU: float):

        self.patient_id = patient_id
        self.age_at_death = age_at_death
        self.sex = sex
        self.highest_education = highest_education
        self.APOE_genotype = APOE_genotype
        self.CASI_score = CASI_score
        self.ABeta42 = ABeta42
        self.pTAU = pTAU
     # Adds the newly created patient to the class list of all patients
        Patient.all_patients.append(self)

    # formats the patient information of selected qualities for data analysis
    def __repr__(self):
        return f"{self.patient_id}: ({self.age_at_death} | {self.sex} | {self.highest_education} | {self.APOE_genotype} | {self.CASI_score} | {self.ABeta42} | {self.pTAU})"

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
                    age_at_death=int(row['Age at Death']),
                    sex=row['Sex'],
                    highest_education=row['Highest level of education'],
                    APOE_genotype=row['APOE Genotype'],
                    CASI_score=float(row['Last CASI Score']),
                    ABeta42=float(row['ABeta42 pg/ug']),
                    pTAU=float(row['pTAU pg/ug'])
                )

     # Returns patients that match the selected education and APOE genotype
    @classmethod
    def filter(cls, list, highest_education="any", APOE_genotype="any"):

        all_patients = list
        remove_list = []
        # Identifies patients who do not meet the selected filtering criteria
        for patient in all_patients:
            if highest_education != "any" and patient.highest_education != highest_education:
                remove_list.append(patient)

            elif APOE_genotype != "any" and patient.APOE_genotype != APOE_genotype:
                remove_list.append(patient)
        # Creates a new list containing only patients who meet the criteria
        all_patients = [patient for patient in all_patients if patient not in remove_list]

        return all_patients
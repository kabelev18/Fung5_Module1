import csv

# Creating class with a few attributes picked out
class Patient:

    def __init__(self, patient_id: str, age_at_death: int, sex: str, years_of_ed: int, ABeta40: float, tTAU: float):
        self.patient_id = patient_id
        self.age_at_death = age_at_death
        self.sex = sex
        self.years_of_ed = years_of_ed
        self.ABeta40 = ABeta40
        self.tTAU = tTAU

        Patient.all_patients.append(self)

# creating a __repr__ method to print out the attributes of the class in a readable format
    def __repr__(self):
        return f"{self.patient_id}: ({self.age_at_death} | {self.sex} | {self.years_of_ed} | {self.ABeta40} | {self.tTAU})"

# creating a method to get the age at death of the patient
    def get_age_at_death(self):
        return self.age_at_death

# creating a class attribute to hold all instances of the class
    all_patients = []
    @classmethod
    def instantiate_from_csv(cls, filename: str):

        with open(filename, encoding="utf8") as f:
            reader = csv.DictReader(f)
            rows_of_patients = list(reader)

            for row in rows_of_patients:
                Patient(
                    patient_id=row['Donor ID'],
                    age_at_death=int(row['Age at Death']),
                    sex=row['Sex'],
                    years_of_ed=int(row['Years of education']),
                    ABeta40=float(row['ABeta40 pg/ug']),
                    tTAU=float(row['tTAU pg/ug'])
                )

# creating a class method to filter the list of patients based on sex and years of education
    @classmethod
    def filter(cls, list, sex="any", years_of_ed="any"):

        all_patients = list
        remove_list = []

# looping through the list of patients and removing any patients that do not match the filter criteria
        for patient in all_patients:
            if sex != "any" and patient.sex != sex:
                remove_list.append(patient)
            elif years_of_ed != "any" and patient.years_of_ed <= years_of_ed:
                remove_list.append(patient)

        all_patients = [patient for patient in all_patients if patient not in remove_list]

        return all_patients
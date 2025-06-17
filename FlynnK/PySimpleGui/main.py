from patient import Patient
from datetime import datetime

patients = [
    Patient("Flynn", "Walsh", datetime(2000,12,17), 125, 70.5, False),
    Patient("Napat", "P", datetime(2000,6,14), 145, 90.2, False),
    Patient("Archer", "Skipsy", datetime(2000, 1, 6), 135, 67.8, True)
]

# def convert_patients_to_table_data():
#     patients_data = []
#     for patient in patients:
#         strings = patient.convert_values_to_strings()
#         patients_data.append(strings)
#     return patients_data

print(patients[0].convert_values_to_strings())
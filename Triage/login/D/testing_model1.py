import pandas as pd
import random
import risk_model_v2 as rm


index = random.randint(1,100)
df = pd.read_csv("merged_shuffled_final_80000.csv")
actual_output_row = {'Age': 19, 'Gender': 'Female', 'Systolic_BP': '120', 'Heart_Rate': '85', 'Temperature': '98.6', 'Oxygen': '103', 'Chest_Pain': True, 'Severe_Breathlessness': True, 'Sudden_Confusion': True, 'Stroke_Symptoms': False, 'Seizure': False, 'Severe_Trauma': False, 'Uncontrolled_Bleeding': False, 'Loss_of_Consciousness': False, 'Severe_Allergic_Reaction': True, 'Persistent_Fever': True, 'Vomiting': False, 'Moderate_Abdominal_Pain': False, 'Persistent_Cough': True, 'Moderate_Breathlessness': False, 'Severe_Headache': False, 'Dizziness': True, 'Dehydration': False, 'Palpitations': False, 'Migraine': False, 'Mild_Headache': False, 'Sore_Throat': False, 'Runny_Nose': False, 'Mild_Cough': False, 'Fatigue': True, 'Body_Ache': True, 'Mild_Abdominal_Pain': False, 'Skin_Rash': False, 'Mild_Back_Pain': True, 'Mild_Joint_Pain': False, 'Diabetes': True, 'Hypertension': True, 'Heart_Disease': True, 'Asthma': False, 'Chronic_Kidney_Disease': False, 'Previous_Stroke': False, 'Smoker': True, 'Obese': False, 'Previous_Heart_Attack': True, 'Previous_Hospitalization': False}

# X = df.drop(columns=["Risk", "Department"])
# sample_patient_dict = df.iloc[index].to_dict()
print(index)
# print(actual_output_row.to_dict())
print(rm.predict_risk(actual_output_row))

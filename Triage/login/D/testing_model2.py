import pandas as pd
import random
import department_model as rm


index = random.randint(1,100)
df = pd.read_csv("merged_shuffled_final_80000.csv")
actual_output_row = df.iloc[index].to_dict()

# X = df.drop(columns=["Risk", "Department"])
# sample_patient_dict = df.iloc[index].to_dict()
print(index)
print(actual_output_row["Department"])
print(rm.predict_department(actual_output_row))

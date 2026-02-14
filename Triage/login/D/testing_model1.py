import pandas as pd
import random
import risk_model_v2 as rm


index = random.randint(1,100)
df = pd.read_csv("merged_shuffled_final_80000.csv")
actual_output_row = df.iloc[index]

# X = df.drop(columns=["Risk", "Department"])
# sample_patient_dict = df.iloc[index].to_dict()
print(index)
# print(actual_output_row.to_dict())
print(rm.predict_risk(actual_output_row))

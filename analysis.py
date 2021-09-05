import pandas as pd

pd.set_option('display.max_columns', 8)
general = pd.read_csv('test/general.csv')
prenatal = pd.read_csv('test/prenatal.csv')
sports = pd.read_csv('test/sports.csv')
# prenatal.rename(columns={'HOSPITAL': 'hospital', 'Sex': 'gender'}, inplace=True)
# sports.rename(columns={'Hospital': 'hospital', 'Male/female': 'gender'}, inplace=True)
prenatal.columns = general.columns
sports.columns = general.columns
result_df = pd.concat([general, prenatal, sports], ignore_index=True)
result_df.drop(columns=['Unnamed: 0'], inplace=True)

result_df.dropna(how='all', inplace=True)
result_df['gender'] = result_df['gender'].replace(['man', 'male', 'woman', 'female'], ['m', 'm', 'f', 'f'])

result_df[result_df.hospital == 'prenatal'] = result_df[result_df.hospital == 'prenatal'].fillna({'gender': 'f'})
result_df = result_df.fillna({'bmi': 0, 'diagnosis': 0, 'blood_test': 0, 'ecg': 0, 'ultrasound': 0, 'mri': 0, 'xray': 0,
                              'children': 0, 'months': 0})

general_hospital_patients_count = len(result_df[result_df.hospital == 'general'])
general_hospital_stomach_patients_count = len(
    result_df[(result_df.hospital == 'general') & (result_df.diagnosis == 'stomach')])

sports_hospital_patients_count = len(result_df[result_df.hospital == 'sports'])
sports_hospital_dislocation_patients_count = len(
    result_df[(result_df.hospital == 'sports') & (result_df.diagnosis == 'dislocation')])

general_patients_median_age = result_df.loc[result_df.hospital == 'general', 'age'].median()
sports_patients_median_age = result_df.loc[result_df.hospital == 'sports', 'age'].median()

blood_test_count_table = pd.pivot_table(result_df[result_df.blood_test == 't'], values='blood_test', index='hospital',
                                        aggfunc='count')
print(f"The answer to the 1st question is {result_df['hospital'].value_counts().idxmax()}")
print(f"The answer to the 2nd question is "
      f"{round((general_hospital_stomach_patients_count / general_hospital_patients_count), 3)}")
print(f"The answer to the 3rd question is "
      f"{round(sports_hospital_dislocation_patients_count / sports_hospital_patients_count, 3)}")

print(f"The answer to the 4th question is {general_patients_median_age - sports_patients_median_age}")
print(
    f"The answer to the 5th question is {blood_test_count_table['blood_test'].idxmax()},"
    f" {blood_test_count_table['blood_test'].max()} blood tests")

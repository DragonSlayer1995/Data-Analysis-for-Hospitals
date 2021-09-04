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
print(f'Data shape: {result_df.shape}')
print(result_df.sample(n=20, random_state=30))


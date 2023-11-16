import pandas as pd


csv_file_path = 'diabetes.csv'
df = pd.read_csv(csv_file_path)

total_count=(df[(df['Glucose']>120) & (df['BloodPressure']>90) & (df['SkinThickness']>30) & (df['Insulin']>150) & (df['BMI']>25) ])
diabetes_count=len(total_count[total_count['Outcome']==1])

#print(total_count)
#print(diabetes_count)


print("probability of diabetes with given conditions : ",diabetes_count/len(total_count))

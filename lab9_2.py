import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the diabetes dataset from a CSV file
csv_file_path = 'diabetes1.csv'
data = pd.read_csv(csv_file_path)

# Data Preprocessing
# Replace missing values with means and medians
data['Glucose'].replace(0, data['Glucose'].mean(), inplace=True)
data['BloodPressure'].replace(0, data['BloodPressure'].mean(), inplace=True)
data['BMI'].replace(0, data['BMI'].mean(), inplace=True)
data['SkinThickness'].replace(0, data['SkinThickness'].median(),inplace=True)
data['Insulin'].replace(0, data['Insulin'].median(),inplace=True)

#drop duplicates
data.drop_duplicates(inplace=True)

diabetes_df=data.drop(columns=['Outcome','Type'])

statistics = pd.DataFrame({
    
    'Mean'  : diabetes_df.mean(),
    'Median': diabetes_df.median(),
    'Mode'  : diabetes_df.mode().iloc[0],
    'Min'   :  diabetes_df.min(),
    'Max'   : diabetes_df.max(),
    'Standard_dev' :  diabetes_df.std()
    
})

print("statistics of all the attributes excluding outcome : \n\n ",statistics)

print("\n\nCorrelation coefficients of age with other attributes excluding outcome : \n")
age_correlations = diabetes_df.corr()['Age']
bmi_correlations = diabetes_df.corr()['BMI']

print(age_correlations)

print("\n\nCorrelation coefficients of bmi with other attributes excluding outcome : \n")

print(bmi_correlations)

print("\n\n")
# Scatter plots
attributes = diabetes_df.columns
for attribute in attributes:
    if attribute != 'Age' and attribute != 'BMI':
        # Scatter plot for 'Age' and other attributes
        plt.figure(figsize=(6, 4))
        plt.scatter(data['Age'], data[attribute], alpha=0.5)
        plt.title(f'Scatter Plot: Age vs. {attribute}')
        plt.xlabel('Age')
        plt.ylabel(attribute)
        plt.show()

        # Scatter plot for 'BMI' and other attributes
        plt.figure(figsize=(6, 4))
        plt.scatter(data['BMI'], data[attribute], alpha=0.5)
        plt.title(f'Scatter Plot: BMI vs. {attribute}')
        plt.xlabel('BMI')
        plt.ylabel(attribute)
        plt.show()
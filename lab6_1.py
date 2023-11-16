import pandas as pd

data = {
    'Name': ['Ram', 'Sam', 'Prabhu'],
    'Aadhar No':[959389389173,959389389179,959389389159],
    'Contact No':[9840787333,9840787343,9840787353],
    'DOB':['12-2-1990','12-2-2000','12-2-2010'],
    'Address':['No 23, Kandigai, Chennai 127','No 73, Melakottaiyu, Chennai 127','No 43, Anna Nagar, Chennai 102']
}

df = pd.DataFrame(data)

# Specify the file path where you want to save the CSV file
csv_file_path1 = 'Aadhar_DB.csv'

# Save the DataFrame to a CSV file
df.to_csv(csv_file_path1, index=False)  # Set index=False to exclude row numbers in the CSV file

print(f"CSV file '{csv_file_path1}' created successfully.")

csv_file_path2 = 'SBIAccountHolder.csv'

df2=pd.read_csv(csv_file_path2)
df1=pd.read_csv(csv_file_path1)

merged_df = pd.merge(df1, df2, on=['Aadhar No','Name'], how='outer')
merged_df.to_csv('merged_file.csv', index=False)



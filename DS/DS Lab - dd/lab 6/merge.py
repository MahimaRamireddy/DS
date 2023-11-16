import csv

# Read data from the first CSV file
table1data = []
with open("SBIAccountHolder.csv", mode="r") as file:
    reader = csv.reader(file)
    table1data = list(reader)

# Read data from the second CSV file
table2data = []
with open("Aadhar_DB.csv", mode="r") as file:
    reader = csv.reader(file)
    table2data = list(reader)

# Create a dictionary to store the data from the second table
table2dict = {}
for row in table2data[1:]:  # Skip the header row
    name = row[0]
    aadhar_no = row[1]
    table2dict[(name, aadhar_no)] = row[2:]

# Merge the data from both tables based on "Name" and "Aadhar No"
merged_data = []
header = table1data[0] + table2data[0][2:]  # Combine headers
merged_data.append(header)

for row1 in table1data[1:]:
    name = row1[0]
    aadhar_no = row1[3]
    if (name, aadhar_no) in table2dict:
        merged_row = row1 + table2dict[(name, aadhar_no)]
        merged_data.append(merged_row)

# Write the merged data to a new CSV file
merged_csv_file = 'MergedData.csv'
with open(merged_csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(merged_data)

print(f'{merged_csv_file} created successfully.')





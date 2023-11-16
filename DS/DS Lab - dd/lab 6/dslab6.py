import csv

#Data in table
data = [
    ['Name', 'Account Number', 'Account Type', 'Aadhar No', 'Balance'],
    ['Ram',9893893891, 'SB', 959389389173, 8989839],
    ['Sam',9893893898, 'CA', 959389389179, 7690990],
    ['Prabhu',9893893871, 'SB', 959389389159, 989330],
]


csv_file = 'SBIAccountHolder.csv'

# Writing the data
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f'{csv_file} created successfully.')

#functions
#append
def append(name, account_number, account_type, aadhar_no, balance):
    with open(csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, account_number, account_type, aadhar_no, balance])
    print(f'Record added successfully.')

# delete
def delete(account_number):
    data = []
    with open(csv_file, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1] != str(account_number):  
                data.append(row)

    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print(f'Data of account: {account_number} has been deleted successfully.')

# Function to credit an account
def credit(account_number, amount):
    data = []
    updated = False
    with open(csv_file, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1] == str(account_number):  # Check if the account number matches
                row[4] = str(int(row[4]) + amount)  # Update the balance
                updated = True
            data.append(row)

    if updated:
        with open(csv_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
        print(f'Amount {amount} credited to Account Number {account_number} successfully.')
    else:
        print(f'Account Number {account_number} not found.')

# Function to debit an account
def debit(account_number, amount):
    data = []
    updated = False
    with open(csv_file, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1] == str(account_number):  # Check if the account number matches
                if row[2] == 'SB' and int(row[4]) - amount < 0:
                    print(f'Error: Insufficient balance for Account Number {account_number}.')
                else:
                    row[4] = str(int(row[4]) - amount)  # Update the balance
                    updated = True
            data.append(row)

    if updated:
        with open(csv_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
        print(f'Amount {amount} debited from account no. {account_number} successfully.')
    else:
        print(f'Account Number :{account_number } is not found.')

# Function to print account details given the account number
def printdets(account_number):
    with open(csv_file, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1] == str(account_number):  # Check if the account number matches
                print(f'Account Number: {row[1]}')
                print(f'Name: {row[0]}')
                print(f'Account Type: {row[2]}')
                print(f'Aadhar No: {row[3]}')
                print(f'Balance: {row[4]}')
                return
    print(f'account no:{account_number} is not found.')



#Menu 
while True:
    print('Enter the choice: 1.Append Record 2.Delete Record 3.Credit 4.Debit 5.Print Account Details 6.Exit')

    choice = int(input('Enter your choice: '))

    if choice == 1:
        name = input('Enter Name: ')
        account_number = int(input('Enter Account Number: '))
        account_type = input('Enter Account Type: ')
        aadhar_no = int(input('Enter Aadhar No: '))
        balance = int(input('Enter Balance: '))
        append(name, account_number, account_type, aadhar_no, balance)

    elif choice == 2:
        account_number = int(input('Enter Account Number to delete: '))
        delete(account_number)

    elif choice == 3:
        account_number = int(input('Enter Account Number to credit: '))
        amount = int(input('Enter Amount to credit: '))
        credit(account_number, amount)

    elif choice == 4:
        account_number = int(input('Enter Account Number to debit: '))
        amount = int(input('Enter Amount to debit: '))
        debit(account_number, amount)

    elif choice == 5:
        account_number = int(input('Enter Account Number to print details: '))
        printdets(account_number)

    elif choice == 6:
        print('Exiting....')
        break

    else:
        print('Invalid choice. Please select a valid option.')

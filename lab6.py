import pandas as pd

data = {
    'Name': ['Ram', 'Sam', 'Prabhu'],
    'Account Number': [9893893891,9893893898,9893893871],
    'Account Type': ['SB', 'CA', 'SB'],
    'Aadhar No':[959389389173,959389389179,959389389159],
    'Balance':[8989839,7690990,989330]
}

df = pd.DataFrame(data)

# Specify the file path where you want to save the CSV file
csv_file_path = 'SBIAccountHolder.csv'

# Save the DataFrame to a CSV file
df.to_csv(csv_file_path, index=False)  # Set index=False to exclude row numbers in the CSV file

print(f"CSV file '{csv_file_path}' created successfully.")

while True:
    print("\n1.Append record of account holder\n2.Delete record\n3.Credit\n4.Debit\n5.Print account details\n6.exit")
    n=int(input("enter an option : "))
    if n==1:
       df1 = pd.read_csv(csv_file_path)
       name = input("Enter Name: ")
       Account_no = int(input("Enter Account Number(length 10): "))
       if Account_no <10000000000 and Account_no>999999999:
           
        if Account_no not in df1['Account Number'].values:
                Account_type = input("Enter Account Type(SB or CA): ")
                Aadhar_no = int(input("Enter Aadhar Number(length 12): "))
                balance = float(input("Enter Balance(>=0): "))

                if Aadhar_no > 99999999999 and Aadhar_no<1000000000000 and balance>=0 and Account_type in ['SB','CA']:
                    
                    new_record = {
                    'Name': name,
                    'Account Number': Account_no,
                    'Account Type': Account_type,
                    'Aadhar No':Aadhar_no,
                    'Balance':balance
                    }

                    df1 = df1._append(new_record, ignore_index=True)
                    df1.to_csv(csv_file_path, index=False)

                    print("new record added successfully!")
                else :
                    print("invalid details")
        else :
            print("account already exists. try again!")

       else:
        print("invalid account no!")


    elif n==2:
        df1 = pd.read_csv(csv_file_path)
        acc_no=int(input("enter the account no of record to be deleted : "))
        if acc_no in df1['Account Number'].values:
            df1 = df1[df1['Account Number'] != acc_no]
            df1.to_csv(csv_file_path, index=False)
            print("record is deleted successfully!")
        else :
            print("account no doesnt exist.try again!")

        
    elif n==3:
        df1 = pd.read_csv(csv_file_path)
        acc_no=int(input("enter the account no of : "))
        if acc_no in df1['Account Number'].values:
            credit=float(input("enter the amount to be credited : "))
            df1.loc[df1['Account Number'] == acc_no, 'Balance'] +=credit
            new_balance = df1.loc[df1['Account Number'] == acc_no, 'Balance'].values
            print("amount credited! new balance = ",new_balance)
        else :
            print("account no doesnt exist.try again!")


    elif n==4:
        df1 = pd.read_csv(csv_file_path)
        acc_no=int(input("enter the account no  : "))
        if acc_no in df1['Account Number'].values:
            debit=float(input("enter the amount to be debited : "))
            current_balance = df1.loc[df1['Account Number'] == acc_no, 'Balance'].values
            acc_type=df1.loc[df1['Account Number'] == acc_no, 'Account Type'].values
            if current_balance > debit  :
                df1.loc[df1['Account Number'] == acc_no, 'Balance'] -=debit
                new_balance = df1.loc[df1['Account Number'] == acc_no, 'Balance'].values
                print("amount debited! new balance = ",new_balance)
            elif current_balance < debit and acc_type=='CA':
                 df1.loc[df1['Account Number'] == acc_no, 'Balance'] =0
                 new_balance = df1.loc[df1['Account Number'] == acc_no, 'Balance'].values
                 print("amount debited! new balance = ",new_balance)
            else :
                print("insufficient balance! current balance : ",current_balance)
        else :
            print("account no doesnt exist.try again!")

         
    elif n==5:
        df1 = pd.read_csv(csv_file_path)
        acc_no=int(input("enter the account no : "))
        if acc_no in df1['Account Number'].values:
            name=df1.loc[df1['Account Number'] == acc_no, 'Name'].values
            type=df1.loc[df1['Account Number'] == acc_no, 'Account Type'].values
            aadhar=df1.loc[df1['Account Number'] == acc_no, 'Aadhar No'].values
            bal=df1.loc[df1['Account Number'] == acc_no, 'Balance'].values
            print("\naccount details : ")
            print("Name : ",name)
            print("account no : ",acc_no)
            print("account type : ",type)
            print("aadhar no : ",aadhar)
            print("balance : ",bal)
        else :
            print("account doesnt exist. try again!")

    elif n==6:
        break
    
    else :
        print("enter a valid option")
import pandas as pd
data = {
    'Name' : ['Ram','Sam','Prabhu'],
    'Account Number' : [ 9893893891, 9893893898, 9893893871],
    'Account Type' : ['SB', 'CA', 'SB'],
    'Adhaar_No' : [ 959389389173, 959389389179, 959389389159],
    'Balance': [ 8989839, 7690990, 989330]
}

df = pd.DataFrame(data)

df.to_csv('SBIAccountHolder.csv',index = False)
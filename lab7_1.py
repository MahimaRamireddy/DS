import pandas as pd


csv_file_path = 'diabetes.csv'
df = pd.read_csv(csv_file_path)

total_count=len(df[df['Outcome']==1])+len(df[df['Outcome']==0])
diabetes_count=len(df[df['Outcome']==1])

#print(total_count)
#print(diabetes_count)

print("probability of diabetes",diabetes_count/total_count)


while True :
    print("1.age above 50\n2.age between 40 and 50\n3.age between 30 and 40\n4.age below 30\n5.exit")
    n=int(input("enter an option : "))
    
    if n==1:
        
        age_50_dia=len(df[(df['Outcome']==1) & (df['Age']>50)])
        age_50= len(df[ (df['Age']>50)])
        
        #print(df[(df['Age']>50)])
        
        #print(age_50_dia)
        #print(age_50)
        
        print("probability of diabetes age above 50 : ",age_50_dia/age_50)
        
    elif n==2:
        
        age_45_dia=len(df[(df['Outcome']==1) & (df['Age']<=50) & (df['Age']>=40)])
        age_45= len(df[ (df['Age']<=50) & (df['Age']>=40)])
        
        #print(age_45_dia)
        #print(age_45)
        
        print("probability of diabetes age between 40 and 50 : ",age_45_dia/age_45)
        
        
        
    elif n==3:
        
        age_34_dia=len(df[(df['Outcome']==1) & (df['Age']<=40) & (df['Age']>=30)])
        age_34= len(df[ (df['Age']<=40) & (df['Age']>=30)])
        
        #print(age_34_dia)
        #print(age_34)
        
        print("probability of diabetes age between 30 and 40 : ",age_34_dia/age_34)
        
        
    elif n==4:
        
        age_30_dia=len(df[(df['Outcome']==1) & (df['Age']<30)])
        age_30= len(df[(df['Age']<30)])
        
        #print(age_30_dia)
        #print(age_30)
        
        print("probability of diabetes age below 30 : ",age_30_dia/age_30)
        
    elif n==5:
        
        print("programme closed.....")
        break
    
    else:
        print("invalid option!")

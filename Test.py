import pandas as pd
file_path = 'file.csv' 
df = pd.read_csv(file_path)
#اضافه کردن اسم ستون ها به لیست 
nameColumnList=[]
for item in df[0:0]:
    nameColumnList.append(item)

def isNominal(column_values):
    nominal_types = (int, float)
    return all(isinstance(value, nominal_types) for value in column_values)


def minColumn(nameColumn):
    if(isNominal(df[nameColumn])):
     print(f"nameColumn:{nameColumn}\t\t\tminColumn: {df[nameColumn].min()}")


def maxColumn(nameColumn):
    if(isNominal(df[nameColumn])):
     print(f"nameColumn:{nameColumn}\t\t\tmaxColumn: {df[nameColumn].max()}") 


def meanColumn(nameColumn):
    if(isNominal(df[nameColumn])):
        print(f"nameColumn:{nameColumn}\t\t\tmeanColumn: {df[nameColumn].mean()}") 


def medianColumn(nameColumn):
    if(isNominal(df[nameColumn])):
        print(f"nameColumn:{nameColumn}\t\t\tmedianColumn: {df[nameColumn].median()}") 
    

for nameC in nameColumnList:
    meanColumn(nameC)


    

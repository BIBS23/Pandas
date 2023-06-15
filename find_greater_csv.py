import pandas as pd

dict = {
    'Reg No' : ['ABC123','ECH256','FET235','ECS042','CSE069'],
    'Name' : ["Bibin","Abin","Ajay","Ajai","Joseph"],
    'Semester' : ["S5","S8","S2","S4","S6"],
    'College' : ["ABC","ECH","FET","ECS","CSE"],
    'CGPA' : [8,7,6.5,9.1,9.5]

}

df = pd.DataFrame(dict)

df.to_csv('toppers.csv')   # convert to csv
mylist = pd.read_csv('toppers.csv')  #read csv

sort = mylist[mylist['CGPA']>9] # sorting

print(sort)

import pandas as pd

dict = {
    'Reg No' : ['ABC123','ECH256','FET235','ECS042','CSE069'],
    'Name' : ["Bibin","Abin","Ajay","Ajai","Joseph"],
    'Semester' : ["S5","S8","S2","S4","S6"],
    'College' : ["ABC","ECH","FET","ECS","CSE"],
    'CGPA' : [9.8,7.5,9.9,9.1,9.5]

}

df = pd.DataFrame(dict)

df.to_csv('toppers.csv')
mylist = pd.read_csv('toppers.csv')
sort = mylist.sort_values(['CGPA'])

print(sort)

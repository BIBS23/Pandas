import pandas as pd
import matplotlib.pyplot as plt

dict = {
    'Temp': [28,30,40,27],
    'Date':['18-06-2023','19-06-2023','20-06-2023','21-06-2023']
}

df = pd.DataFrame(dict)
df.to_csv('temperature.csv')

mydata=pd.read_csv('temperature.csv')
x = mydata['Temp'].values
y = mydata['Date'].values

mylabel = ['Teekoy','Erattupetta','Kottayam','Ernakulam']

plt.pie(x,labels = mylabel)

plt.show()




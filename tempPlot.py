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

plt.xlabel('Temperature')
plt.ylabel('Dates')
plt.title('Tempature in my cities')
plt.scatter(x,y)

plt.show()




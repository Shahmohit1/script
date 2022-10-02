#TASK 3
# importing pandas in order to read .csv file 
import pandas as pd

#creating an empty list in case required to store some values 
inter =[]
# Using pd.read_csv command to .csv file
data=pd.read_csv("python.csv")

#Making acolumn named Compare to Visually confirm the Squares of number
data['Compare'] = data['Number']*data['Number']

#making a column named wrong entry which shows Which Squares are worng
data['Wrong Entry'] = data['Compare'] != data['Square']
inter = data.loc[data['Wrong Entry'] ]

# we use len(inter) which will give answer 2 which actually need in task 3
print('Number of wrong entries for square of a number in python.csv file is',len( inter))
#Arranging in Ascending order
f=data.sort_values('Number')
# printing f
print (f)

#Task 4
#importing matplot lib for plotting of file in task 3
import matplotlib.pyplot as plt
plt.title('Task 4')
plt.xlabel('Number')
plt.ylabel('Square')
plt.grid()
plt.scatter(f['Number'],f["Square"],label="Squares in data")
#plotting number and Compare to Compare difference in both the lines 
plt.scatter(f['Number'],f["Compare"],label='Actual Squares')
plt.legend()
plt.show()
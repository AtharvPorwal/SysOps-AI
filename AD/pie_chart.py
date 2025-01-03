import matplotlib.pyplot as plt  
import numpy as np  
labels = ['Category A', 'Category B', 'Category C', 'Category D']  
data = np.random.rand(4)  
plt.figure(figsize=(8, 8))  
plt.pie(data, labels=labels, autopct='%1.1f%%', startangle=140)  
plt.title('Random Data Pie Chart')  
plt.show() 


import matplotlib.pyplot as plt
import numpy as np

# Generate random data
np.random.seed(0)
data = np.random.rand(5)
data /= data.sum()

# Define labels
labels = ['A', 'B', 'C', 'D', 'E']

# Create a pie chart
plt.figure(figsize=(6, 6))
plt.pie(data, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title('Random Pie Chart')
plt.show()

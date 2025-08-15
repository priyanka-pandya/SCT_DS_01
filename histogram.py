import pandas as pd 
import matplotlib.pyplot as plt

#load cleaned dataset
df = pd.read_csv('cleaned_data.csv')

#select the population column for the latest year 
population_2024 = df['2024']

#create histogram
plt.figure(figrsize=(10,6))
plt.hist(population_2024, bins=30, color='skyblue', edgecolor='black')
plt.title('Population Distribution in 2024')
plt.xlabel('Population')    
plt.ylabel('Numbers of Countries')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
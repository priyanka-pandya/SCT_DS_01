import pandas as pd

# Load dataset, skip metadata rows, fix encoding issue means removing extra rows above the table
population_df = pd.read_csv("population.csv", skiprows=4, encoding='latin1')

# Drop fully empty rows
population_df.dropna(how='all', inplace=True)

# Fill other missing values with 0
population_df.fillna(0, inplace=True)

# Rename columns for clarity
population_df.rename(columns={
    'Country Name': 'country',
    'Country Code': 'code'
}, inplace=True)

 
# Preview cleaned data
print(population_df.head(5))

# Check for missing values
print(population_df.isnull().sum())

# remove rows where country name is missing
population_df.dropna(subset=['country'])

duplicates= population_df.duplicated().sum()
print(duplicates)
df = population_df.drop_duplicates()

#save the cleaned dataset
df.to_csv("cleaned_data.csv",index=False)

print ("cleaned data saved successfully")

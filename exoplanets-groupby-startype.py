pip install pandas
pip install tabulate

import pandas as pd
from tabulate import tabulate

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('mini.csv')

# Define a dictionary to map first letters of st_spectype to groups
spectype_groups = {
    'A': [],
    'F': [],
    'G': [],
    'K': [],
    'M': []
}

# Iterate through the DataFrame and categorize rows into respective groups
for index, row in df.iterrows():
    first_letter = row['st_spectype'][0]
    if first_letter in spectype_groups:
        # Change the 'st_spectype' cell for the group it belongs
        row['st_spectype'] = first_letter
        spectype_groups[first_letter].append(row)

# Create a new DataFrame for the selected elements
selected_df = pd.concat([pd.DataFrame(group) for group in spectype_groups.values()])

# Count the elements in each group
group_counts = {key: len(value) for key, value in spectype_groups.items()}

# Print the count of elements in each group
print("\nNumber of elements in each group:")
print(tabulate(group_counts.items(), headers=['Spectype Group', 'Count'], tablefmt='pretty'))

# Save selected elements in a CSV file
selected_df.to_csv('output.csv', index=False)

# Print the tables for each group using tabulate
for key, value in spectype_groups.items():
    print(f'\nGroup: {key}')
    print(tabulate(value, headers='keys', tablefmt='pretty', showindex=False))
#https://scipython.com/book2/chapter-2-the-core-python-language-i/questions/problems/p26/earth-similarity-index/

!import pandas as pd

# Load data from Excel file
excel_file = 'path/to/your/excel/file.xlsx'
df = pd.read_excel(excel_file)

# The column indexes of fields *after the first, name field* within the
# provided data table for the properties needed to calculate the ESI
cols = (1, 2, 4, 6)
n = len(cols)
# The terrestrial values of those parameters and their weights
x_earth, w = (1, 1, 1, 288.), (0.57, 1.07, 0.70, 5.58)

# Create a new DataFrame to store the results
result_df = pd.DataFrame(columns=['Planet Name', 'Star Name', 'ESI', 'ESIi', 'ESIe'])

print('-'*42)
print('Planet/Satellite Name   Star Name   ESI  ESIi ESIe')
print('-'*42)

for index, row in df.iterrows():
    name = str(row.iloc[0])[:15].lstrip()  # Assuming the first column contains the names
    star_name = str(row.iloc[8])  # Assuming the star name is in the 9th column
    fields = row.iloc[1:].tolist()

    ESI = 1
    #IST global
    for i, col in enumerate(cols):
        xi = float(fields[col])
        ESI *= (1 - abs((xi - x_earth[i])/(xi + x_earth[i])))**(w[i]/n)

        #                 radio(radios terrestres)                     densidad(g/cm3)                        ve     (m/s)                                                         Temperatura(K)
        #((1 - abs((xi - 1)/(xi + 1)))**(0.57/4)) * ((1 - abs((xi - 5.515)/(xi + 5.515)))**(1.07/4)) * ((1 - abs((xi - 11183.87)/(xi + 11183.87)))**(0.7/4)) * ((1 - abs((xi - 288)/(xi + 288)))**(5.58/4))

    #IST interior
    for i, col in enumerate(cols):
        xi = float(fields[col])
        ESIi *= (1 - abs((xi - x_earth[i])/(xi + x_earth[i])))**(w[i]/n)


        #                 radio(radios terrestres)                     densidad(g/cm3)
        #((1 - abs((xi - 1)/(xi + 1)))**(0.57/2)) * ((1 - abs((xi - 5.515)/(xi + 5.515)))**(1.07/2))

    #IST exterior
    for i, col in enumerate(cols):
        xi = float(fields[col])
        ESIe *= (1 - abs((xi - x_earth[i])/(xi + x_earth[i])))**(w[i]/n)

        #             ve     (m/s)                                                         Temperatura(K)
        #((1 - abs((xi - 11183.87)/(xi + 11183.87)))**(0.7/2)) * ((1 - abs((xi - 288)/(xi + 288)))**(5.58/2))



    #ESI = ESI**(1/n)

    # Append the result to the new DataFrame
    result_df = result_df.append({'Planet Name': name, 'Star Name': star_name, 'ESI': ESI}, ignore_index=True)

    # Print the result in the console
    print('{:<21s}   {:<11s}   {:5.3f}'.format(name, star_name, ESI))

print('-'*42)

# Save the result to a new Excel file
result_excel_file = 'path/to/your/result/excel/file.xlsx'
result_df.to_excel(result_excel_file, index=False)
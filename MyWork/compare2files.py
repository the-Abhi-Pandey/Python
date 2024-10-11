#---------------------------------------find difference between two sheets


import pandas as pd

file_path = r'"C:\Users\2186236\OneDrive - Cognizant\Desktop\Target Entity Trend Details 070123 - 063024.xlsx"'
df1 = pd.read_excel(file_path, sheet_name='DEV')
df2 = pd.read_excel(file_path, sheet_name='PROD')

diff_df = df1.compare(df2)
print(diff_df)

# diff_df.to_csv('differences.csv', index=False)          #export data in CSV

# print("Differences exported to 'differences.csv'")



# ------------------------------------find difference and export in excel

# import pandas as pd

# # Load the Excel file
# file_path = r'C:\Users\2186236\OneDrive - Cognizant\Desktop\Python\MyWork\Entity_trend.xlsx'
# df1 = pd.read_excel(file_path, sheet_name='DEV')
# df2 = pd.read_excel(file_path, sheet_name='PROD')

# # Compare the two dataframes and show differences
# diff_df = df1.compare(df2)

# # Export the differences to an Excel file
# output_file_path = r'C:\Users\2186236\OneDrive - Cognizant\Desktop\Python\MyWork\differences.xlsx'
# diff_df.to_excel(output_file_path, index=False)

# print(f"Differences exported to '{output_file_path}'")



#---------------------------------------find difference between two files
'''

import pandas as pd

# Load data from two files
file1 = r'C:\Users\2186236\OneDrive - Cognizant\Desktop\sheet1.csv'
file2 = r'C:\Users\2186236\OneDrive - Cognizant\Desktop\sheet2.csv'

df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)

# Compare the data
comparison = df1.compare(df2)

# Show the differences
print(comparison)
'''

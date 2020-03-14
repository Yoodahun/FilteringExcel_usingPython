import pandas as pd
import datetime

# dateTime
time = datetime.datetime.now().date()

# Read excel file
excelFile = pd.read_excel(f'../{time}-과일.xlsx')
# Filtering condition
condition = (excelFile['과일이름'] == '멜론')
# Filtering
excelFile_filtered = excelFile[condition]
size = excelFile_filtered.index

# row count filtered_file
print(len(excelFile_filtered))

#filtered
fruits = excelFile_filtered['과일이름']
print(fruits)
print(type(fruits))

# Export Filtered excel file
excelFile_filtered.to_excel('과일필터.xlsx', index=False)
fruits.to_excel('과일이름.xlsx', index=False)

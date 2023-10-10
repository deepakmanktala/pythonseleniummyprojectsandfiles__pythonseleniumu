import pandas as pd
import xlsxwriter

file = 'LoginInvalidUsernamePassword.xlsx'
# Load spreadsheet
xl1 = pd.ExcelFile(file)
xl = pd.ExcelFile(file)

writer = pd.ExcelWriter('LoginInvalidUsernamePassword.xlsx', engine='xlsxwriter')
yourData.to_excel(writer, 'Sheet2')
writer.save()
# Print the sheet names
print(xl.sheet_names)

# Load a sheet into a DataFrame by name: df1
df1 = xl.parse('Sheet1')
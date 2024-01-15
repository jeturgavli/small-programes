import openpyxl

filename = input('Enter Name Of Your Excel File (without extension): ')

try:
    # Attempt to load the workbook
    workbook = openpyxl.load_workbook(f'Excel_File/{filename}.xlsx')
    sheet = workbook['Sheet1']

    # Access cell value
    cell_value = sheet['A1'].value
    print(f'Cell A1 Value: {cell_value}')

    # Write to Excel file
    sheet['B1'] = 'Hello, Python!'
    
    # Save the modified workbook
    modified_filename = f'{filename}_modified.xlsx'
    workbook.save(f'Excel_File/{modified_filename}')
    print(f'Modified Excel file saved as: {modified_filename}')

except FileNotFoundError:
    print(f"Error: The file 'Excel_File/{filename}.xlsx' does not exist.")
except openpyxl.utils.exceptions.InvalidFileException:
    print(f"Error: The file 'Excel_File/{filename}.xlsx' is not a valid Excel file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


# you can interact with and manipulate Excel files using Python. 
# There are several libraries available for this purpose, 
# such as openpyxl, pandas, and xlrd. 
# These libraries allow you to read, 
# write, and perform various operations on Excel files 
# programmatically.

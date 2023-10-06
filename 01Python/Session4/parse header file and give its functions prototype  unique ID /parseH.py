import os
import re
from openpyxl import Workbook

header_file=os.path.dirname(os.path.realpath(__file__))+"/DIO.h"

def extract_prototypes(header_file):
    prototypes = []
    id_counter = 1
    with open(header_file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if re.match(r'^\s*[/*#]',line):
                continue
            else:
                prototypes.append(f"IDX{str(id_counter).zfill(3)} {line}")
                id_counter += 1
    return prototypes
def write_xlsx():
    xlsx_file=os.path.dirname(os.path.realpath(__file__))+"/DIO.xlsx"
    # Create a new Excel workbook
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Function Prototypes"
    # Add headers to the Excel sheet
    sheet.append(["ID", "Prototype"])
    prototypes = extract_prototypes(header_file)

    # Add function prototypes to the Excel sheet
    for prototype in prototypes:
        sheet.append([prototype.split()[0], prototype.split(' ', 1)[1]])

    workbook.save(xlsx_file)

    print(f"Function prototypes saved to {xlsx_file}")

write_xlsx()
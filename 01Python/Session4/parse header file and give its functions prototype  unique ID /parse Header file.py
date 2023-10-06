import os
import re
from openpyxl import Workbook

header_file=os.path.dirname(os.path.realpath(__file__))+"/DIO.h"

def extract_prototypes(header_file):
    prototypes = []
   
    with open(header_file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if re.match(r'^\s*[/*#]',line):    ## Pass comments line and defines
                continue
            else:
                prototypes.append(line)
                
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
    print(prototypes)

 
    count=0
    for i in prototypes:
        count+=1

     # Add function prototypes to the Excel sheet
    for i in range(0,count):
        data=[f"IDX00{i+1}",prototypes[i]]
        sheet.append(data)

        
    workbook.save(xlsx_file)

    print(f"Function prototypes saved to {xlsx_file}")

write_xlsx()



import os
import re
from openpyxl import Workbook
class headerParser:
    name=""
    def __init__(self,name):
        self.header_file=os.path.dirname(os.path.realpath(__file__))+name

    def extract_prototypes(self,header_file):
        prototypes = []
    
        with open(self.header_file, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if re.match(r'^\s*[/*#]',line):    ## Pass comments line and defines
                    continue
                else:
                    prototypes.append(line)
                    
        return prototypes 

    def write_xlsx(self):
        self.xlsx_file=os.path.dirname(os.path.realpath(__file__))+"/DIO.xlsx"
        # Create a new Excel workbook
        workbook = Workbook()
        sheet = workbook.active
        sheet.title = "Function Prototypes"
        # Add headers to the Excel sheet
        sheet.append(["ID", "Prototype"])
        prototypes = self.extract_prototypes(self.header_file)
        #print(prototypes)
        count=0
        for i in prototypes:
            count+=1
        # Add function prototypes to the Excel sheet
        for i in range(0,count):
            data=[f"IDX00{i+1}",prototypes[i]]
            sheet.append(data)

            
        workbook.save(self.xlsx_file)

        print(f"Function prototypes saved to {self.xlsx_file}")

    def __del__(self):
        pass

if __name__ == "__main__":
    parse=headerParser("/DIO.h")
    parse.write_xlsx()


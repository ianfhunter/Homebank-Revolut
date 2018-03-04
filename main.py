#!/usr/bin/env python
import os.path
import time
from datetime import date
from datetime import datetime
import re


csv_file = "transaction.csv"

if not os.path.isfile(csv_file):
    # I would fix this if it mattered more to me.    
    print("You must have a csv file exactly called 'transaction.csv'.")
    quit()

# Open Exported Transaction Document
with open(csv_file, "r") as ins:
    array = []
    for line in ins:
        array.append(line)

array.pop(0) # We don't need the first line.
translated_array = []
for line in array:
    print(line)
    translated_line = ""
    cols = line.split(";")
    dt = datetime.strptime(cols[0], '%d %b %Y ')
    translated_line += dt.strftime("%d/%m/%Y")     # Date
    translated_line += ";;;;"
    translated_line += ";"
    pattern = re.compile(r'\s+')
    cols[2] = re.sub(pattern, '', cols[2])
    cols[3] = re.sub(pattern, '', cols[3])

    if(cols[2]): # Expenditure
        translated_line += "-" + cols[2]
    if(cols[3]): # Income
        translated_line += cols[3]
    translated_line += ";;"
    translated_line += "ATAG" # Some tag, I don't use these personally
    translated_array.append(translated_line)

# Write back your new, formatted document
with open("transaction_formatted.csv", "w") as ins:
    for line in translated_array:
        ins.write(line + "\n")
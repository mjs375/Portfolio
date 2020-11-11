# READING AND WRITING CSV FILES IN PYTHON

- **What is a CSV File?:** *a ```CSV``` (Comma-Separated Values) file is a type of plain-text file that uses specific structuring to arrange tabular data, and usually handle large amounts of data (a convenient way to export data from spreadsheets and databases). The first line usually specifies the types of data: they are column headings.*
  - **The Separator:** *the most common is the ```,```, but can also be ```:```, ```;```, ```\t```(tab). One must one which delimiter is being used to properly parse the CSV file.*
```csv
col1name,col2name,col3name
row1-data1,row1-data2,row1-data3
row2-data1,row2-data2,row2-data3
row3-data1,row3-data2,row3-data3
```

### CSV Library: Read & Write
- ```csv``` library provides the ability to both read and write to CSV files.
  - *Example CSV file:*
```csv
name,department,birthday month
John Smith,Accounting,November
Erica Meyers, IT, March
```
- **Reading:**
```python
import csv

with open('employee_birthday.txt') as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=",")
  line_count = 0
  for row in csv_reader:
    if line_count == 0:
      print(f"Column names are {', '.join(row)}")
      line_count += 1
    else:
      print(f"\t{row[0] works in the {row[1]} department, and was born in {row[2]}.")
      line_count += 1
    print(f"Processed {line_count} lines.")
```

- **Writing:**









## SOURCES

- [Real Python: Reading and Writing CSV Files in Python](https://realpython.com/python-csv/)

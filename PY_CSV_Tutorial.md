# READING AND WRITING CSV FILES IN PYTHON

- **How?:** *use Python's built-in ```csv``` library.*
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

### Reading CSV Files
- *Reading from a CSV is done using the ```reader``` object, using the ```open()``` function, which returns a file object, which in turn is passed to the ```reader```, which does the most of the work. Below is a simple output of a CSV file using a for-loop to iterate each row, and using indexing to get each row's column-data:*
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
- **Reading CSV Files into a Dictionary:**
  - *instead of just dealing with individual string elements, you can read CSV data into a dictionary, the keys coming from the first line (if not, specify your own keys by setting the ```fieldnames``` parameter to a list containing them).*
```python
import csv

with open('employee_birthday.txt', mode='r') as csv_file:
  csv_reader = csv.DictReader(csv_file)
  line_count = 0
  for row in csv_reader:
    if line_count == 0:
      print(f"Column names are {', '.join(row)}")
      line_count += 1
    print(f"\t{row['name']} works in the {row['department']} department, and was born in {row['birthday month']}.")
    line_count +=1
  print(f"Processed {line_count} lines.")
```

- **CSV Reader Optional Parameters:**
  - ```delimiter```: *specifies the character used to separate each field, the default being ",".*
    - *in the example below, you could specify a delimiter other than ",", so that a comma can be safely in the data itself.*
  - ```quotechar```: *specifies the character used to surround fields that containing the delimiter character, the default is a double quote (' " ').*
    - *the special nature of the selected delimiter is ignored when in quoted strings, so as that as that special character isn't also in the data, you can wrap data in that to nullify the ",".*
  - ```escapechar```: *specifies the character used to escape the delimiter character, in case quotes aren't used (default is no escape character).*
    - *escape characters work just like in format strings.*
```csv
name,address,date joined
john smith, 1132 Main St Hoboken NJ, 07030, Jan 4
erica meyers, 120 South St Hoboken NJ, 07030, Mar 2
    => Note that the address field contains a ",".
```

### Writing CSV Files
- *you can write to a CSV file using a ```writer``` object and the ```.write_row()``` method.*
  - ```quotechar``` optional parameter: *tells the ```writer``` which character to use to quote fields when writing; it is based on the ```quoting``` parameter:*
    - ```quoting = csv.QUOTE_MINIMAL```: *```.writerow()``` will only quote fields if they contain the delimiter or the quotechar (default).*
    - ```quoting = csv.QUOTE_ALL```: *```.writerow()``` will quote all fields.*
    - ```quoting = csv.QUOTE_NONNUMERIC```: *```.writerow()``` will quote all fields containing text data and convert all numeric fields to the ```float``` data-type.*
    - ```quoting = csv.QUOTE_NONE: *delimiters will be escaped instead of quoted (you must also provide a value for the ```escapechar``` parameter).*
```python
import csv

with open("employee_file.csv", mode="w") as employee_file:
  employee_writer = csv.writer(employee_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
  
  employee_writer.writerow(['John Smith', 'Accounting', 'November'])
  employee_writer.writerow(['Erica Meyers', 'IT', 'March'])
```
=>
```csv
John Smith,Accounting,November
Erica Meyers,IT,March
```


- **Writing CSV Files from a Dictionary:**
```python
import csv

with open("employee_file2.csv", mode="w") as csv_file:
  fieldnames = ['emp_name', 'dept', 'birth_month'] # required when writing a dict (Dict needs to know keys)
  writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
  
  writer.writeheader() # Uses fieldnames
  writer.writerow({'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'})
  writer.writerow({'emp_name': 'Erica Meyers', 'dept': 'IT', 'birth_month': 'March'})
```

## Parsing CSV Files with the Pandas Library
- **Python Install:** ```$ pip install pandas``` (Anaconda Install: ```$ conda install pandas```)
- **Reading CSV w/ Pandas:** *```pandas.read_csv()``` opens, analyzes, and reads the CSV file, and stores it in a DataFrame*
```csv
Name,Hire Date,Salary,Sick Days remaining
Graham Chapman,03/15/14,50000.00,10
John Cleese,06/01/15,65000.00,8
```
```python
import pandas
df = pandas.read_csv('file.csv') # read CSV into a pandas DataFrame
print(df)
```





## SOURCES

- [Real Python: Reading and Writing CSV Files in Python](https://realpython.com/python-csv/)

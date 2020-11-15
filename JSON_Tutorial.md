# Working with JSON Data in Python
- the *de facto* standard for information exchange, be it gathering API information or storing data in a document database. JSON is human-readable, akin to C-type languages (C, Python). JSON supports primitive data types (strings, numbers) as well as nests lists and objects (looks just like a Python dictionary!)
  - **JavaScript Object Notation**: *though it was inspired by Javascript, it is now its own standard, so you don't need JavaScript actually*
   - Example ```file.JSON```:
```json
{
  "firstName": "Jane",
  "lastName": "Doe",
  "hobbies": ["running", "sky-diving", "singing"],
  "age": 35,
  "children": [
    {
      "firstName": "Alice",
      "age": 6
    }
    {
      "firstName": "Bobby",
      "age": 8
    }
  ]
}
```

### Using JSON in Python
- **```import json```**: *JSON is Python-native, and can be encoded / decoded easily.*
  - **Encoding:** *aka __serialization__, or the transformation of data into a 'series of bytes' to be stored/transmitted. (Decoding = 'deserialization'.)*
  
Python | JSON
-------|------
dict | object
list, tuple | array
str | string
int, long, float | number
True | true
False | false
None | null

### Writing a JSON File
```python
data = {
  "president": {
    "name": "Barack Obama",
    "term": 44
    }
} # this information needs to be saved/stored!
```
```python
with open("data_file.json", "w") as write_file:
  json.dump(data, write_file)
```





<hr>

[Source](https://realpython.com/python-json/)

#Dictionary & Sets
# Dictionaries are mutable mappings in Python
info = {
    "name": "John",
    "age": 20 ,
    
    "is_student": True,
    "grades": [85, 90, 78],
    "address": {
        "city": "New York",
        "zip": "10001",
    }
}
print(info["name"])  # Accessing value by key
#print(info)
print(info.keys())  # Get all keys
print(list(info.values()))  # Get all values
pairs = print((listinfo.items())) # Get all key-value pairs
print(len(list(info.keys())))  # Get number of keys
print(pairs[0])  # 
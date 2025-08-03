info = {
    "name": "dictionary",
    "Subject" : ["python","C","Java"],
    "Topics": ["data structures", "algorithms", "design patterns"],
    "Difficulty": ("easy", "medium", "hard"),
    "Resources": {
        "Books": ["Introduction to Algorithms", "Python Crash Course", "Effective Java"],
        "Websites": ["GeeksforGeeks", "W3Schools", "Stack Overflow"],
        "Videos": ["YouTube Tutorials", "Coursera Courses"],
     "is_advanced": True,
      "last_updated": "2023-10-01",
    
    },
   
   
}
print (len(list(info.keys())))
print("Dictionary Information:")
print(info)
print([info["name"]]) 
print(info["Resources"]["Books"])  # Accessing nested dictionary


# Accessing dictionary
info["name"] = "Python Dictionary"  # Modifying a value
print("\nModified Name:")
print(info["name"])
print("info")

#Dictionary mutability

info["Difficulty"] = ("easy", "medium", "hard", "expert")  # Modifying a tuple
print("\nModified Difficulty Level:")  
print(info["Difficulty"])
print(info.keys())  # Displaying keys of the dictionary
print(info.values())  # Displaying values of the dictionary
print(list(info.values()))  # Converting values to a list 
print(info.items())  # Displaying key-value pairs as tuples
print(info.get("name"))  # Using get() method to access a key / no error if key does not exist
print(info.get("non_existent_key", "Default Value"))  # Using get() with a default value
info.update({"new_key": "new_value"})  # Adding a new key-value pair
print("\nUpdated Dictionary:")
print(info)
pairs=list(info.items())  # Converting dictionary to a list of key-value pairs
print(pairs[0])
print(pairs[1])
print(pairs[2])  # Accessing specific key-value pairs 
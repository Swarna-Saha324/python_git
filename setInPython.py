#Set is the collection of unique elements
#Sets are unordered, unchangeable, and do not allow duplicate values.
#Sets are mutable, meaning you can add or remove items after the set has been created.
#Sets are defined using curly braces {} or the set() constructor.
#list, [tuple], and dictionary are not sets.
#Sets can be used to perform mathematical set operations like union, intersection, and difference.
#Example of a set in Python
collection = {1, 2, 3, 4, 5 , "hello", "world", 1, 2, 3, 4}  # Duplicate values are ignored
print("Set Collection:", collection)
print("Length of Set:", len(collection))  # Length of the set
print(type(collection))  # Type of the collection
collection1 ={ }
print(type(collection1))  # Empty set is of type dict, not set
# To create an empty set, use set()
collection2 = set()  # Correct way to create an empty set
print("Empty Set:", collection2)
#Set Methods
collection.add(6)  # Adding an element to the set
print("Set after adding an element:", collection)
collection.remove(2)  # Removing an element from the set
print("Set after removing an element:", collection)
collection.discard(3)  # Discarding an element (no error if not found)
collection.pop()  # Removes and returns an arbitrary element
print("Set after pop operation:", collection)
collection.clear()  # Clearing the set
print("Set after clearing:", collection)  # Set is now empty
collection.add()
# Set operations
set_a = {1, 2, 3}

#list of python keywords
#keywords = [
   # "False", "None", "True", "and", "as", "assert", "async", "await",
   # "break", "class", "continue", "def", "del", "elif", "else", "except",
   # "finally", "for", "from", "global", "if", "import", "in", "is",
   # "lambda", "nonlocal", "not", "or", "pass", "raise", "return",
   # "try", "while", "with", "yield"
#]
marks = [76, 85, 90, 65,67, 80, 95, 70, 60, 55]
print("Marks:", marks)
print("Maximum Marks:", max(marks))
print("Minimum Marks:", min(marks))
print (len(marks))
print(type(marks))
print(marks[0])  # accessing the first element
print(marks[-1])  # accessing the last element
print(marks[2:5])  # slicing from index 2 to 4
print(marks[::2])  # slicing with step 2
marks.append(100)  # adding an element to the end
print("After appending 100:", marks)
marks.insert(0, 50)  # inserting an element at index 0
print("After inserting 50 at index 0:", marks)
marks.remove(65)  # removing the first occurrence of 65
print("After removing 65:", marks)
marks.pop()  # removing the last element
print("After popping the last element:", marks)
#list mutable
#string immutable
marks.sort()  # sorting the list in ascending order
student = ["Alice", 95.5, "A"]
student[0] = "Bob"  # changing the name
print("Updated student name:", student)
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 + list2  # concatenating two lists
print("Concatenated list:", list3)
#list1.append([7, 8])  # appending another list Adds the argument as a single element
#print("After appending [7, 8]:", list1)
list1.extend([9, 10])  # extending the list with multiple elements Adds each element of the iterable
print("After extending with [9, 10]:", list1)
list1.sort()
print("Sorted list:", list1)
list1.sort(reverse=True)
print("Reversed list:",list1 )  # sorting in descending order 
list1.reverse()  # reversing the list
print("Reversed list:", list1)  # reversing the list
list1.insert(1, 100)  # inserting 100 at index 1
print("After inserting 100 at index 1:", list1)
list1.pop(2)  # removing the element at index 2
print("After popping the element at index 2:", list1)
# Tuple example
# Tuples are immutable sequences in Python
tuple1 = (1, 2, 3, 4, 5)
print("Tuple:", tuple1)
print("Type of tuple1:", type(tuple1))  # checking the type of tuple
print("First element of tuple:", tuple1[0])  # accessing the first element 
print("Last element of tuple:", tuple1[-1])  # accessing the last element
print("Slice of tuple from index 1 to 3:", tuple1[1:4])  # slicing from index 1 to 3
print("Tuple length:", len(tuple1))  # getting the length of the tuple
tup1=(1,)
print("Single element tuple:", tup1)  # single element tuple
print("Type of single element tuple:", type(tup1))  # checking the type of single element tuple
tup2=(1)
print("type of tup2:", type(tup2))  # this is not a tuple, it's an integer
# Converting a tuple to a list
list_from_tuple = list(tuple1)
print("List from tuple:", list_from_tuple)  # converting tuple to list
# Converting a list to a tuple
tuple_from_list = tuple(list1)
print("Tuple from list:", tuple_from_list)  # converting list to tuple
tup4 = (1, 2, 3, 4, 5)
# Checking if an element exists in a tuple
print("Does 3 exist in tup4?", 3 in tup4)  # checking for existence of an element
print("Does 6 exist in tup4?", 6 in tup4)  # checking for non-existent element
# Tuple unpacking
a, b, c, d, e = tup4  # unpacking the tuple into variables
print("Unpacked values:", a, b, c, d, e)  # printing unpacked values
# Nested tuples
nested_tuple = (1, (2, 3), (4, 5, 6), 7)
print("Nested tuple:", nested_tuple)  # printing the nested tuple
# Accessing elements in a nested tuple
print("Element at index 1 in nested tuple:", nested_tuple[1])  # accessing the second element
print("Element at index 0 in nested tuple's second element:", nested_tuple[1][0])  # accessing an element in the nested tuple
# Tuple methods
print("Count of 1 in tup4:", tup4.count(1))  # counting occurrences of an element
print("Index of 3 in tup4:", tup4.index(3))  # finding the index of an element
#palindrome example
list10= [1, 2, 3, 2, 1]
# Checking if a list is a palindrome
copy_list10 = list10.copy()  # copying the list
copy_list10.reverse()  # reversing the copied list
#print("Is list10 a palindrome?", list10 == copy_list10)  
# Checking if a list is a palindrome
if (list10 == copy_list10):
      print("list10 is a palindrome")
else:
      print("list10 is not a palindrome")

# Dictionary example
# Dictionaries are mutable mappings in Python
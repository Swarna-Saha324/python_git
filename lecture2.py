str1='tghjjljlk'
str2="Swarna Saha"
#escape_sequence characters \n \t \r \b \f \v
print(str1+" "+str2)
print(len(str1))
#indexing and slicing (accessing characters in a string)
print(str1[0])  
print(str2[1:5])  #slicing ending index is exclusive
print(str2[-1])  #negative indexing
print(str2[-5:-1])  #slicing with negative indexing
print(str2[0:5:2])  #slicing with step
print(str2[::-1])  #reversing a string
#string Functions
str3=" i am a Python Programmer "
print(str3.endswith("mmer "))  #check if string ends with a substring
print(str3.startswith(" I am "))  #check if string starts with a substring
print(str3.find("Python"))  #find the index of a substring
print(str3.replace("Python", "Java"))  #replace a substring with another substring
print(str3.upper())  #convert string to uppercase
print(str3.lower())  #convert string to lowercase
print(str3.strip())  #remove leading and trailing whitespace
print(str3.split())  #split string into a list of words
print(str3.split("a"))  #split string into a list of words with a specific delimiter
print(str3.split(" "))  #split string into a list of words with space as delimiter
print(str3.title())  #convert string to title case
print(str3.capitalize())  #capitalize the first letter of the string
print(str3.isalpha())  #check if string contains only alphabetic characters
print(str3.isalnum())  #check if string contains only alphanumeric characters
print(str3.isdigit())  #check if string contains only digits
print(str3.islower())  #check if string is in lowercase
print(str3.isupper())  #check if string is in uppercase
print(str3.isnumeric())  #check if string contains only numeric characters
print(str3.isidentifier())  #check if string is a valid identifier
print(str3.count("a"))  #count the number of occurrences of a substring
print(str3.center(50, '*'))  #center the string with a specific character
str4="Hello World"
print(str4.count("o"))  #count the number of occurrences of a character
marks=76
if marks >= 90:
    grade = 'A'
elif marks >= 80 and marks < 90:
    grade = 'B'
elif marks >= 70 and marks < 80:
    grade = 'C'
elif marks >= 60 and marks < 70:
    grade = 'D'
else:
    grade = 'F'

print(f"Your grade is: {grade}")  #formatted string literals
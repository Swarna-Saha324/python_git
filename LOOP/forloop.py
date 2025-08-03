#for loop
"""num =[1,4,9,16,25,36,49,64,81,100]
for n in num:
    print(n)"""
tuple = (1, 2, 3, 4, 5)
for i in tuple:
    print(i)

string = "Hello"  
for char in string:
    print(char)
else:
    print("Loop completed without interruption.")

# Using a for loop to iterate through a list
list_data = [10, 20, 30, 40, 50]
for item in list_data:
    print(item)

list_data1 = [1, 2, 3, 4, 5]
X=3
index = 0
for item in list_data1:
    if item == X:
        print  (" Found 3, breaking the loop.", index)
    index += 1
    

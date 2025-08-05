cities=["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
Names=["Alice", "Bob", "Charlie", "David", "Eve"]
def print_len(list):

    print("Length of the list is:", len(list))

print_len(cities) # calling the function with a list argument
print_len(Names) # calling the function with another list argument
# Function to print the values of a list
def print_values(list):
    for item in list:
        print(item, end=" ")
        print()  # for a new line after printing all items
print_values(cities)  # calling the function with a list argument

print_values(Names)  # calling the function with another list argument

#homework
def in_hw():
    x= int (input("Enter a number: "))
    if(x% 2 == 0):
        print("Even")
    else:
        print("Odd")
in_hw()  # calling the homework function


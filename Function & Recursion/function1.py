#block of statements that perform  specific task
#redundant code
# avoid redundancy
#functions define
def add(x, y): #parameters
    """Adds two numbers and returns the result."""
    sum = x + y
    print(sum)
    return x + y
add(2,3) #function call /arguments
#Functions are two types
# 1. Built-in functions for example print(), input(), len() ,range()
# 2. User-defined functions
print("Swarna", end=" ") #end is used to avoid new line
print("Saha")

def cal_product(x=1, y=1): #default parameters
    """Calculates the product of two numbers."""
    product = x * y
    return product
cal_product(2, 3) # passing arguments
cal_product() # using default parameters
def cal_sum(y,x=1) : #default parameters should be at the end
    """Calculates the sum of two numbers."""
    sum = x + y
    print("Sum is:", sum)
    return sum
cal_sum(2) # passing arguments
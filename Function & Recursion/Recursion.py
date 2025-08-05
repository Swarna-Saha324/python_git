#When a function calls itself, it is called recursion.
#loops are used to repeat a block of code, but recursion is used to solve problems by breaking them down into smaller subproblems.
#Recursion is a powerful technique that can simplify code and make it more elegant.
#Recursion can be used to solve problems like factorial, Fibonacci series, etc.
#Recursion can lead to infinite loops if not handled properly, so it is important to have a base case to stop the recursion.
#Example of recursion
def show (n):
    if(n==0):
        return 0
    print(n)
    show(n-1)
    print("end")
show(5) # calling the function with an argument
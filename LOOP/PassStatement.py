#pass is a null statement in Python.
# It is used when a statement is required syntactically but you do not want any command or code to execute.
# It is often used as a placeholder for future code.
def example_function():
    pass  # This function does nothing for now
# Example of using pass in a loop
for i in range(5):
    if i == 2:
        pass  # Placeholder for future code
    print(i)

n=7
sum = 0
for i in range(1, 11):
    sum = sum + i

print(f"The sum of numbers from 1 to 10 is: ", sum)

factorial = 1
num = int (input("Enter a number to calculate its factorial: "))
for i in range(1, num + 1):
    factorial *= i

print(f"The factorial of {num} is: {factorial}")
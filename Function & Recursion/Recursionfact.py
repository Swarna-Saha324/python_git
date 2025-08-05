def fact(n):
    if n == 0 or n == 1:  # Base case /termination /stop condition
        return 1
    else:
        return n * fact(n - 1)  # Recursive call
c=3
factorial = fact(c)  # Example usage
print(f"Factorial of {c} is:{factorial}") # Output the result
def calc_sum(n):
    if n == 0:  # Base case: if n is 0
        return 0
    else:
        return n + calc_sum(n - 1)  # Recursive case: add n to the sum of numbers less than n

sum=calc_sum(5)
print(sum)
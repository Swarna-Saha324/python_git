my_list = [1, 2, 3, 4, 5]

def print_list(lst):
    # Use recursion to sum the elements of the list
    if not lst:  # Base case: if the list is empty
        return 0
    else:
        # Recursive case: sum the first element and the rest of the list
        return lst[0] + print_list(lst[1:])

total = print_list(my_list)
print("Sum of the list elements is:", total)


def calc_sum(n):
    if n == 0:  # Base case: if n is 0
        return 0
    else:
        return n + calc_sum(n - 1)  # Recursive case: add n to the sum of numbers less than n

sum=calc_sum(5)
print(sum)
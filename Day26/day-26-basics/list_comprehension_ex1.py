numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
print(f"Original list: {numbers}")
# create a new list from numbers, but new list numbers must be squared
squared_numbers = [sq * sq for sq in numbers]
print(f"Squared list: {squared_numbers}")

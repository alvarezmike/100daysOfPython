# You are going to write a list comprehension to create a new list
# called result. This new list should only contain the even numbers from the list.

numbers = [1, 1, 2, 3,  5, 8, 13, 21, 34, 55]
print(f"Original list: {numbers}")

result = [n for n in numbers if n % 2 == 0]
print(f"Even numbers from list: {result}")

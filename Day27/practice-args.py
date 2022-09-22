def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(6, 8, 17))
# this was done to practice unlimited arguments using *args

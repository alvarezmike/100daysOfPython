fruits = ["Apple", "Pear", "Orange"]

# TODO: catch the exception


def make_pie(index):
    fruit = fruits[index]
    print(fruit + " pie")


try:
    make_pie(4)

except IndexError:
    print(make_pie(0))
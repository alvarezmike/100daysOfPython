# something that  may cause an error
try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])

# do this if there was an exception
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Writing something into file")

# is possible to have multiple exceptions
except KeyError as error_message:
    print(f"The key {error_message} does not exists")

# do this if there was no exception
else:
    content = file.read()
    print(content)

# do this no matter what happens
finally:
    file.close()
    print("File was closed")


#regular function
def greet():
  name = input("What is your name ?\n")
  print(f"Welcome, have a wondeful day {name}")


#function with input
def greet_name(name): #paramter
  print(f"Hello {name}")
  print("Gave a great morning.")

#greet_name("Michael") #argument

#function with more than one parameter
def greet_more(name,location):
   print(f"Hello {name}\n")
   print(f"How is it in {location}")

greet_more("Michael","Florida")
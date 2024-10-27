### List Comprehension  ###

# List comprehension offers a shorter syntax when you want to create a new list based on 
# the values of an existing list.

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "n" in x:
    newlist.append(x)

print(f"New List:", newlist)
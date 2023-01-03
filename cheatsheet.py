# Python Cheat Sheet

# List
## List is unordered, mutable, and allows duplicate elements

## Creating a list
list_of_things = ["thing", "thing", "thing2"]
## Adding to end of list
list_of_things.append("thing3")

## Loop through list with iterator and value
for i, thing in enumerate(list_of_things):
    print(str(i) + thing)

## Access item in list
thing = list_of_things[1]

## Remove item from list (end), pass arg to remove specific index
list_of_things.pop()
## Insert item into list
list_of_things.insert(1, "thing2")

## Loop through list with iterator
for thing in range(len(list_of_things)):
    print(thing)

## While loop and remove each item from the end
while len(list_of_things) > 0:
    list_of_things.pop()

## List comprehension example, a short hand way to loop a list
some_list = ["item1", "item2", "item3"]
for item in some_list:
    print(f"The item is: {item}")

## List comprehension, for (thing) in (iterable) if (condition)
list_comprehension_list = ["item1", "item2", "item3"]
[print(f"The item is: {item}") for item in list_comprehension_list if "item" in item]


# Tuple
## Tuple is ordered (order won't change), immutable, and allows duplicate elements

## Creating a tuple
tuple_of_things = ("thing", "thing2", "thing3")

## Access item in tuple
thing2 = tuple_of_things[1]

# Set


# Dictionary


# First-order functions


# Higher-order functions


# Lambda


# Map, Filter, Reduce

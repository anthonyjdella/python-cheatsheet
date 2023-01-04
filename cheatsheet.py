# Python Cheat Sheet

################################################################################

# List
# List is ordered (order won't change), mutable, and allows duplicate elements

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

################################################################################

# Tuple
## Tuple is ordered (order won't change), immutable (can't change values), and allows duplicate elements
## Use tuple over list when the items won't change, because it's faster

## Creating a tuple
tuple_of_things = ("thing", "thing2", "thing3")

## Access item in tuple
thing2 = tuple_of_things[1]

################################################################################

# Set
## Set is unordered (you won't know what position items are in), mutable, and doesn't allow duplicate elements

## Creating a set
some_set = {"thing", "thing2", "thing3"}

## Access item in set
## You can't access items in a set, because it's unordered

## Add item to set
some_set.add("thing4")

## Remove item from set
some_set.remove("thing4")

################################################################################

# Dictionary
## Dictionary are key-value pairs, ordered, mutable, and doesn't allow duplicate 

## Creating a dictionary
a_dictionary = {"key": "value", "key2": "value2"}

## Access item in dictionary
value = a_dictionary["key"]
another_way_to_access_value = a_dictionary.get("key")

## Add value in dictionary
a_dictionary["key3"] = "new_value"
a_dictionary.update({"key3": "new_value"}) # another way to add a value, but it's slower

## Change value in dictionary
a_dictionary["key"] = "new_value"
a_dictionary.update({"key": "new_value"}) # another way to change value, but it's slower

## Remove item in dictionary
a_dictionary.pop("key") # will remove key and value

## Loop through dictionary
for item in a_dictionary:
    print(item) # get key
    print(a_dictionary[item]) # get value

################################################################################

# First-order functions

################################################################################

# Higher-order functions

################################################################################

# Lambda

################################################################################

# Map, Filter, Reduce

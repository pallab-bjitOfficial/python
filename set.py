this_set = {"apple", "cherry", "banana", }
print(this_set)

print("banana" in this_set)  # return boolean

# add items
this_set.add("mango")
print(this_set)

tropical = {"pineapple", "mango", "papaya"}

# add items from another set into the current set,

this_set.update(tropical)
print(this_set)

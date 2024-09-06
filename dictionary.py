this_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(this_dict)

# access items
brand = this_dict["brand"]
print(brand)

# get the list of keys
keys = this_dict.keys()
print(keys)

# get the list of values
values = this_dict.values()
print(values)

# change items

this_dict.update({"year": 1965})
print(this_dict)

# adding items
this_dict["color"] = "red"
print(this_dict)

# remove a specefic item
this_dict.pop("color")
print("after removing color", this_dict)

# remove the last item
this_dict.popitem()
print("after removing last item", this_dict)

# nested dictionary
child1 = {
    "name": "Emil",
    "year": 2004
}
child2 = {
    "name": "Tobias",
    "year": 2007
}
child3 = {
    "name": "Linus",
    "year": 2011
}

my_family = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}
print(my_family)

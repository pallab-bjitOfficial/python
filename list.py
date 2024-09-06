this_list = ["apple", "banana", "cherry", "mango", "orange", "malta"]
print(this_list)

# length
print(len(this_list))

mixed_list = ["apple", 1, 2.0, "banana"]

print(mixed_list)

# accesing list items
first_item = this_list[0]
print(first_item)

last_item = this_list[-1]
print(last_item)

# negetive indexing
neg_last_item = this_list[-1]
print(neg_last_item)

# range indexing

print("range indexing", this_list[1:3])  # from index 1 to index 2

print("range indexing", this_list[1:])  # from index 1 to the end

print("range indexing", this_list[:3])  # from the start to index 3

# append items
this_list.append("pineapple")
print("after append", this_list)

# insert items
this_list.insert(0, "grape")  # insert at the beginning
print("after insert", this_list)

# extend list
tropical = ["coconut", "papaya", "mangosteen"]
this_list.extend(tropical)
print("after extend", this_list)

# add any iterable
this_list.extend(("kiwi", "lemon", "lime"))
print("after extend", this_list)

# remove items
this_list.remove("pineapple")
print("after remove", this_list)
# remove items by index
this_list.pop(1)
print("after pop", this_list)

for x in this_list:
    print("list item", x)

for i in range(len(this_list)):
    print(f"Index {i}", this_list[i])

# sort
sorted_list = sorted(this_list,)
print("ascending sort", sorted_list)

# reverse sort
reversed_list = sorted(this_list, reverse=True)
print("reversed", reversed_list)

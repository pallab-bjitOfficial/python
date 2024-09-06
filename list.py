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

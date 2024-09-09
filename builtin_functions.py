x = abs(-7.45)
print(x)

my_list = [True, True, True]
y = all(my_list)  # Return True if all elements in the list are True
print(y)

my_list_2 = [True, False, True]
z = any(my_list_2)  # Return True if any element in the list is True
print(z)

my_dict = dict(name="Pallab Majumdar", age=25, city="Dhaka")
print(my_dict)

div_mod = divmod(10, 3)
print(div_mod[0], div_mod[1])

ages = [25, 12, 35, 17, 45]


def filter_adults(ages):
    if ages < 18:
        return False
    else:
        return True


adults = list(filter(filter_adults, ages))
print(adults)

float_number = float(3)  # convert number into float
print(float_number)

large_number = max(100, 200, 300)
print(large_number)

small_number = min(100, 200, 300)
print(small_number)

power = pow(2, 3)
print(power)

alph = ['a', 'b', 'c', 'd', 'e']
ralph = list(reversed(alph))
print(ralph)

rounded_number = round(3.14159, 2)
print(rounded_number)

fruits_set = set(('apple', 'banana', 'cherry'))
print(fruits_set)

sliced_list = slice(2, 5)
print(alph[sliced_list])

unsorted_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_list = sorted(unsorted_list)
print(sorted_list)

sum_of_numbers = sum(sorted_list)
print(sum_of_numbers)

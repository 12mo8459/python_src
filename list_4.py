import random
random_numbers = random.sample(range(100), 5)
print(random_numbers)

random_int = random.randint(0, 10)
print(random_int)

random_numbers.append(random_int)
print(random_numbers)

print(50 in random_numbers)
print(random_numbers)

del(random_numbers[0])
print(random_numbers)
removed_number = random_numbers.pop(0)
print(random_numbers)
print(removed_number)
# list_a = [0, 1, 2, 3, 4, 5]
# del list_a[1]
# print(list_a)
# list_a.pop(2)
# print(list_a)
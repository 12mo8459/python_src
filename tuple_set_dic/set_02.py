import random
list_a = random.sample(range(10), 6)
list_b = random.sample(range(10), 4)
find_data = []

for a in list_a:
    for b in list_b:
        if a == b:
            find_data.append(a)
            break

print(f'list_a = {list_a}')
print(f'list_b = {list_b}')
print(f'find_data = {find_data}')
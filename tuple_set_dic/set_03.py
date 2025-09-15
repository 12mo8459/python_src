import random
list_a = random.sample(range(10), 7)
list_b = []
for _ in range(7):
    list_b.append(random.randint(0, 10))

print(f'list_a = {list_a}')
print(f'list_b = {list_b}')

union_set = set(list_a) | set(list_b)
print(f'union_set = {union_set}')
print(f'-' * 20)
list_a = set(list_a)
list_b = set(list_b)
union_set = list_a.union(list_b)
print(f'union_set = {union_set}')

inter_set = set(list_a) & set(list_b)
print(f'inet_set = {inter_set}')
inter_set = list_a.intersection(list_b)
print(f'inet_set = {inter_set}')

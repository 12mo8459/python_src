list_a = [1, 2, 3]
tuple_a = (1, 2, 3)
print(f'list_a = {type(list_a)}')
print(f'tuple_a = {type(tuple_a)}')
print(f'-' * 20)

print(f'list_a = {list_a}')
print(tuple(list_a))
print(type(tuple(list_a)))
list_a = tuple(list_a)
print(f'list_a = {list_a}')
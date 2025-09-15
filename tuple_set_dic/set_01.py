list_a = [100, 500, 10, 500, 100, 50]
set_a = {1, 2, 3, 1, 2, 1}
print(f'set_a = {set_a}')

print(f'list_a = {list_a}')
print(f'list_a = {set(list_a)}')

set_b = {1, 2, 3}
# print(set_b[0])
set_b.add(4)
print(f'set_b = {set_b}')
set_b.remove(2)
print(f'set_b = {set_b}')
set_b.pop()
print(f'set_b = {set_b}')
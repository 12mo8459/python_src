list_a = [1, 2, 3]
list_b = [4, 5, 6]
print("list_a + list_b =", list_a + list_b)
print("list_a * 3 =", list_a * 3)
print(f'list_a + list_b = {list_a + list_b}')
print(f'list_a * 3 = {list_a *3}')

list_a = [1, 2, 3]
list_a.append(4)
list_a.append(5)
print('-' * 30)
list_a.insert(0, 11)
print(list_a)

list_a = [1, 2, 3]
# list_a.append([4, 5, 6])
list_a += [4, 5, 6]
# list_r = list_a.extend([4, 5, 6])
print(list_a)
# print(list_r)
# print(type(list_r))

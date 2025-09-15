def change(obj):
    obj[0] = 100

data = [1, 2, 3]

# change(data)
change(data.copy())
print(data)
print('*'*20)

list_a = [1, 2, 3]
# list_b = list_a 
list_b = list_a.copy()
list_b[0] = 100
print(f'list_a = {list_a}, list_b = {list_b}')

list_a = [1, 1, 1, 2]
# list_a.remove(1)
#print(list_a)

index = 0
for i in list_a:
#    index += 1
    print(index)
    if i == 1:
        del list_a[index]
    else:
        index += 1
print(list_a)

for i in list_a:
    pass
for i in range(len(list_a)):
    pass

list_a = [1, 1, 1, 2, 1, 2]
for i in range(len(list_a)):
    print('*')
    if 1 in list_a:
        list_a.remove(1)
    else:
        break
print(list_a)
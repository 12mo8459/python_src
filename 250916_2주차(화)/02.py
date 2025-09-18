list_1 = []
print([i for i in range(10) if i % 2 ==0])
print([i for i in range(1, 10) if i % 2 ==0])

list_1 = [1, 2, 3, 1, 2, 3, 4, 5]
print([idx for idx, value in enumerate(list_1) if value == 2])

age = 20
if age >= 18:
    result = "성인"
else:
    result = "미성년자"
print(result)

result = "성년" if age >= 18 else "미성년자"
print(result)

list_1 = [10, 20, 30, 15, 25, 35, 40, 55]
print(["성년" if age >= 18 else "미성년자" for age in list_1])

list_1 = [1, 2, 3, 1, 2, 3, 4, 5]
print(["짝수" if i % 2 == 0 else "홀수" for i in list_1])

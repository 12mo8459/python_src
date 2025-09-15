def myAdd(num1=0, num2=0, num3=0):
    return num1 + num2 + num3

result1 = myAdd()
result2 = myAdd(1)
result3 = myAdd(1, 2)
result4 = myAdd(1, 2, 3)
print(f'세 수의 합은 각각: {result1}, {result2}, {result3}, {result4}')
print(f'세 수의 합은 각각: {result1, result2, result3, result4}')

# def myAdd(num1, num2=0, num3):
#     return num1 + num2 + num3

# result = myAdd(10, 20)
# print(f'세 수의 합은: {result}')

# restlt = myAdd(30)
# print(f'두 수의 합은: {result}')

num1,num2 = map(int, input('두개의 숫자 입력: ').split())
calc_lists = [num1 + num2, num1 - num2, num1 * num2, num1 / num2]
print(f'{num1} + {num2} = {calc_lists[0]}')
print(f'{num1} - {num2} = {calc_lists[1]}')
print(f'{num1} * {num2} = {calc_lists[2]}')
print(f'{num1} / {num2} = {calc_lists[3]}')

print(f'1. 덧셈', end = '\t')
print(f'2. 뺄셈', end = '\t')
print(f'3. 곱셈', end = '\t')
print(f'4. 나눗셈')
choice = int(input('입력하세요 '))
print(f'결과는 : {calc_lists[choice]}')

'''number_input_a = int(input("정수 입력 :"))
print("원의 반지름: " number_input_a)
print("원의 둘레: " 2 * 3.14 * number_input_a)
print("원의 넓이: " 3.14 * number_input_a * number_input_a)'''
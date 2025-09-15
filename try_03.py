try:
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
    print(f'결과는 : {calc_lists[choice-1]}')

except ValueError as e:
    print(f'오류발생 {e}')
except IndexError as e:
    print(f'오류발생 {e}')
except Exception as e:
    print(f'기타오류발생 {e.__class__.__name__} \n 설명 : {e}')

print('프로그램종료')
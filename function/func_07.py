def add(op1, op2):
    return op1 + op2

print(add(10, 20))
numbers = [add(10, 20), add(30,40)]

def show_number(data):
#    print(f'numbers = {data}')
    return f'numbers = {data}'

#show_numbers(add(50, 60))
print(show_number(add(50, 60)))

def test(hello):
    return f'"{hello}"의 글자수는 {len(hello)}개 입니다.'

print(test('안녕하세요'))
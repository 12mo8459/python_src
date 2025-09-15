'''def get_data():
    while True:
        try:
            i_human = int(input('정수를 입력하세요.(1~100)'))
            if not 1 <= i_human <= 100:
                raise ValueError('1과 100사이의 값이 아닙니다.')
        except Exception as e:
            print(f'에러가 발생했습니다. {e}')
        else:
            return i_human

o_human = get_data()
print(f'입력값은 : {o_human}')'''
            
start = 0
end = 0

def get_data():
    input_data1, input_data2 = map(int, input(f'시작값 {start}과 끝값 {end}을 입력하세요. '.split()))
    return input_data1, input_data2

output_data1, output_data2 = get_data()

print(f'start= {output_data1}, end= {output_data2}')'''
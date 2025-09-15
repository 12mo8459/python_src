def get_data(start, end, input_str='입력하세요~'):
    while True:
        try:
            i_human = int(input(f'{input_str} {{start} ~ {end}}'))
            if not start <= i_human <= end:
                raise ValueError(f'{start}과 {end}사이의 값이 아닙니다.')
        except Exception as e:
            print(f'에러가 발생했습니다. {e}')
        else:
            return i_human

o_human = get_data()
print(f'입력값은 : {o_human}')

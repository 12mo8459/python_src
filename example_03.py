def get_data(start, end, input_str='입력하세요~'):
    while True:
        try:
            i_human = int(input(f'{input_str} ({start} ~ {end})'))
            if not start <= i_human <= end:
                raise ValueError(f'{start}과 {end}사이의 값이 아닙니다.')
        except Exception as e:
            print(f'에러가 발생했습니다. {e}')
        else:
            return i_human

def check_winner():
    if human > computer:
        print('큰값을 입력하셨네요.')
        game_history.append((human, '큰값'))
    elif human < computer:
        print('작은값을 입력하셨네요.')
        game_history.append((human, '작은값'))
    else:
        print(f'{count}만에 정답을 맞추셨군요.')
        for guess_value, state in game_history:
            print(f'{guess_value}, {state}')
        break

import random
start, end = 1, 100
computer = random.randint(start, end)

count = 1
game_history = []
while True:
    count += 1
    human = get_data(start, end)
    if check_winner(human, computer, count, game_history):
        break

'''    if human > computer:
        print('큰값을 입력하셨네요.')
        game_history.append((human, '큰값'))
    elif human < computer:
        print('작은값을 입력하셨네요.')
        game_history.append((human, '작은값'))
    else:
        print(f'{count}만에 정답을 맞추셨군요.')
        for guess_value, state in game_history:
            print(f'{guess_value}, {state}')
        break'''

import random
def select_random_numbers(total_numbers, count):
    numbers = list(range(1, total_numbers+1))
    select_numbers = random.sample(numbers, count)
    return select_numbers

print(f'6개의 숫자를 골랐습니다 : {select_random_numbers(45, 6)}')


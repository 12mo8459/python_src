import random
numbers = random.sample(range(100), 10)
print(numbers)

import random
lotto = random.sample(range(1, 45), 6)
print(lotto)

even_numbers = []
for i in numbers:
    if i % 2 == 0:
        even_numbers.append(i)
print(f'짝수들의 집합: {even_numbers}, 갯수: {len(even_numbers)}')

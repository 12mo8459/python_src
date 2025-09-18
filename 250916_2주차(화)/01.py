total = []
for i in range(1, 11):
    total.append(i)
print(total)

print([i for i in range(1, 11)])
print()

import random
total = []
for _ in range(5):
    total.append(random.randint(1, 100))
print(total)

print([random.randint(1, 100) for _ in range(5)])
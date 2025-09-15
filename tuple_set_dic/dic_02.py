result = dict([['name', '홍길동'], ['age', 25]])
print(type(result))
print(result)
print(f'-' * 20)

names = ['홍길동', '임꺽정', '전우치']
scores = [ 90, 80, 70]
students = {}
count = 0
for name in names:
    students[name] = scores[count]
    count += 1
# for i in range(len(names)):
#    students[names[i]] = scores[i]
print(f'students = {students}')
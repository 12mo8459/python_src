cadidate = ['이강택', '박정아', '해피', '천둥', '번개']

vote = []
count = 10
user_count1 = 0 
user_count2 = 0
user_count3 = 0
user_count4 = 0
user_count5 = 0
for _ in range(count):
    user_input = int(input('투표를 시작하세요(1~5) : '))
    if user_input == 1:
        user_count1 += 1
    elif user_input == 2:
        user_count2 += 1
    elif user_input == 3:
        user_count3 += 1
    elif user_input == 4:
        user_count4 += 1
    else:
        user_count5 += 1
    count += 1

vote = [user_count1, user_count2, user_count3, user_count4, user_count5]
print(f'투표결과는 {vote}')

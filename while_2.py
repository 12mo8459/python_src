import time

count = 0
is_continue = True
while is_continue:
    count += 1
    print(f'{count}초')
    time.sleep(1)
    if count % 5 == 0:
        user_input = input('To be continue(Y/N)').upper()
#        is_continue = is_continue.upper()
#        if is_continue != 'Y' or is_continue == 'N':
        if not user_input == 'Y':
            is_continue = False
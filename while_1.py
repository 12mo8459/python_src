import time

count = 0
while True:
    count += 1
    print(f'{count}초')
    time.sleep(1)
    if count % 5 == 0:
        is_continue = input('To be continue(Y/N)')
        is_continue = is_continue.upper()
        if is_continue != 'Y' or is_continue == 'N':
            break
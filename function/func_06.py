import time

count = 0
is_continue = True

def display_second(count):
    count += 1
    print(f'{count}초')
    time.sleep(1)
    return count

def is_user_continue(count):
    if count % 5 == 0:
        user_input = input('To be continue(Y/N)').upper()
        if not user_input == 'Y':
            return False
        else:
            return True
    else:
        return True
#            is_continue = False

while is_continue:
    count = display_second(count)
#    count += 1
#    print(f'{count}초')
#    time.sleep(1)

    is_continue = is_user_continue(count)
#    if count % 5 == 0:
#        user_input = input('To be continue(Y/N)').upper()
#        if not user_input == 'Y':
#            is_continue = False
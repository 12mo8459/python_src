import random
#computer_choice = random.randint(1, 3)

def get_computer():
    return random.randint(1,3)

def get_human():
    return int(input('1:가위, 2:바위, 3:보 :'))

def lock(human_choice):
    if human_choice == 1:
        same += 1
    elif human_choice == 2:
        win += 1
    else:
        loss += 1

def paper(human_choice):
    if human_choice == 2:
        same += 1
    elif human_choice == 3:
        win += 1
    else:
        loss += 1

def scissors(human_choice):
    if human_choice == 3:
        same += 1
    elif human_choice == 1:
        win += 1
    else:
        loss += 1

count = 0
same = 0
win = 0
loss = 0
is_continue = True

computer_choice = get_computer()
human_choice = get_human()

while is_continue:
#    human_choice = int(input('1:가위, 2:바위, 3:보 :'))

    if computer_choice == 1:
        rock(human_choice)
#        if human_choice == 1:
#            same += 1
#        elif human_choice == 2:
#            win += 1
#        else:
#            loss += 1
    elif computer_choice == 2:
#    if computer_choice == 2:
        paper(human_choice)
#        if human_choice == 2:
#            same += 1
#        elif human_choice == 3:
#            win += 1
#        else:
#            loss += 1
    else:
#    if computer_choice == 3:
        scissors(human_choice)
#        if human_choice == 3:
#            same += 1
#        elif human_choice == 1:
#            win += 1
#        else:
#            loss += 1

#while is_continue:
    count += 1
    if count % 3 == 0:
        user_input = input('To be continue? (Y/N)').upper()
        if not user_input == 'Y':
            is_continue = False
#    else:
#        is_continue = False
print(f'same: {same}, win: {win}, loss: {loss}')
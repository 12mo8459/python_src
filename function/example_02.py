import random

same = 0
win = 0
loss = 0

def get_computer():
    return random.randint(1,3)

def get_human():
    return int(input('1:가위, 2:바위, 3:보 :'))

def rock(human_choice):
    global same
    global win
    global loss
    if human_choice == 1:
        same += 1
    elif human_choice == 2:
        win += 1
    else:
        loss += 1

def paper(human_choice):
    global same
    global win
    global loss
    if human_choice == 2:
        same += 1
    elif human_choice == 3:
        win += 1
    else:
        loss += 1

def scissors(human_choice):
    global same
    global win
    global loss
    if human_choice == 3:
        same += 1
    elif human_choice == 1:
        win += 1
    else:
        loss += 1

count = 0
is_continue = True

while is_continue:
    computer_choice = get_computer()
    human_choice = get_human()

    if computer_choice == 1:
        rock(human_choice)
    elif computer_choice == 2:
        paper(human_choice)
    else:
        scissors(human_choice)

    count += 1
    if count % 3 == 0:
        user_input = input('To be continue? (Y/N)').upper()
        if not user_input == 'Y':
            is_continue = False

print(f'same: {same}, win: {win}, loss: {loss}')
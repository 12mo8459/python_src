# import random
# print(random.randint(1, 5))
#1
def say_hello():
    print('안녕하세요~')

say_hello()
#2
def say_hello_name(name):
    print(f'{name}님 안녕하세요~')

say_hello_name('리안')
#3
import datetime
def get_current_time():
    return datetime.datetime.now()

print(get_current_time())
#4
def myCalc(num1, num2):
    '''
    # 두 개의 값을 받아서 덧셈을 해 줍니다.
    - num1
    - num2
    '''
    result = num1 + num2
    return result

print(myCalc(1, 2))

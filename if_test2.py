kor = int(input('국어점수 입력'))
eng = int(input('영어점수 입력'))
math = int(input('수학점수 입력'))
ave = (kor + eng + math) / 3
if ave >= 60 and kor >= 40 and eng >= 40 and math >= 40:
    print('합격')
students = []

class StudentMng():
    def __init__(self):
        self.name = ' '
        self.age = 0

    def info_student(self):
        print(f'이름: {self.name} 나이: {self.age}')

s1 = StudentMng()
s1.name = '홍길동'
s1.age = 25
#print(f'이름: {s1.name} 나이: {s1.age}')
s1.info_student()
students.append(s1)

s2 = StudentMng()
s2.name = '임꺽정'
s2.age = 35
#print(f'이름: {s2.name} 나이: {s2.age}')
s2.info_student()
students.append(s2)

# def info_student(student):
#     print(f"이름: {student['name']} 나이: {student['age']}")

# def create_student(name, age):
#     return { 'name' : name, 'age' : age}

# students.append(
#     {'name' : '홍길동', 'age' : 25}
# )
# students.append(
#     {'name' : '임꺼정', 'age' : 35}
# )

# for s in students:
#     info_student(s)

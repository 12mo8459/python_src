students = []
def info_student(student):
    print(f"이름: {student['name']} 나이: {student['age']}")

# def create_student(name, age):
#     return { 'name' : name, 'age' : age}

students.append(
    {'name' : '홍길동', 'age' : 25}
)
students.append(
    {'name' : '임꺼정', 'age' : 35}
)

for s in students:
    info_student(s)

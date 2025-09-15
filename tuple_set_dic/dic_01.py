student = {
    "name" : "홍길동",
    "age" : 25,
    "major" : "컴퓨터"
}

print(f"student['name'] = {student['name']}")

student['name'] = "노리안"
print(f'student = {student}')

del student["name"]
print(f'student = {student}')

student['addr'] = "서울시 강남구 서초동"
print(f'student = {student}')
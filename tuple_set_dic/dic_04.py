#student1 = [68, 78, 88]
#student2 = [79, 89, 99]
student1 = {'국어': 100, '영어':90, '수학': 80}
student2 = {'국어': 99, '영어':89, '수학': 79}
student3 = {'국어': 88, '영어':78, '수학': 68}
element_class = [student1, student2, student3]

total_math = 0
for student in element_class:
    total_math += student['수학']
    print(f"student['수학'] = {student['수학']}")
print(f'-' * 20)
print(f'total_math = {total_math}')
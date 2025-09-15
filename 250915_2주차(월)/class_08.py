class Student:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

    def total(self):
        return self.kor + self.eng + self.math
        
    def average(self):
        return (self.kor + self.eng + self.math) / 3

    def grade(self):
        avg = self.average()
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'F'
        
    def __str__(self):
        return f"Name: {self.name}, Total: {self.total()}, Average: {self.average():.2f}, Grade: {self.grade()}"
    
# 인스턴스 생성
student1 = Student("Alice", 85, 90, 95)
student2 = Student("Bob", 70, 75, 80)

# 정보 출력
print(student1)
print(student2)
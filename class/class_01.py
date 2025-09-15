class StudentMng():
    name = '홍길동'
    def make_instance(self):
        self.age = 0
        self.addr = 0

s1 = StudentMng()
s2 = StudentMng()
s3 = StudentMng()

print(s1.name, s2.name, s3.name)
s1.name = '임꺽정'         #인스턴스변수
StudentMng.name = '전우치' #클래스변수
print(s1.name, s2.name, s3.name)


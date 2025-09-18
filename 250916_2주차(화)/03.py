class Parents():
    def __inint__(self):
        self.p_name = "parents"
        print("parents __init__")
    def parents_method(self):
        print("parents_method")

class Child(Parents):
    def __init__(self, name, age):
        Parents.__init__(self, name, age)
        self.age = age
        print("child __init__")
    def child_method(self):
        print("child_method")

c = Child('홍길동', 20)
print(c.p_name, c.age)
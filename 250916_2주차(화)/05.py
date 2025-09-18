class Employee:
    def __inint__(self, id, name, base_salary):
        self.id = id
        self.name = name
        self.base_salary = base_salary
    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Base Salary: {self.base_salary}"

    @property
    def base_salary(self):
        return self._base_salary
    @base_salary.setter
    def base_salary(self, value):
        if value < 0:
            raise ValueError("Base salary cannot be negative")
        self._base_salary = value
    def employee_type(self):
        return "General Employee"

class FullTimeEmployee(Employee):
    def __init__(self, id, name, base_salary, bonus):
        super().__init__(id, name, base_salary)
        self.bonus = bonus
    def __str__(self):
        return super().__str__() + f", Bonus: {self.bonus}"
    
    @property
    def bonus(self):
        return self._bonus
    @bonus.setter
    def bonus(self, value):
        if value < 0:
            raise ValueError("Bonus cannot be negative")
        self._bonus = value
    def employee_type(self):
        return "Full Time Employee"

class PartTimeEmployee(Employee):
    def __init__(self, id, name, base_salary, hours_worked):
        super().__init__(id, name, 0)
        self.hours_worked = hours_worked
        self.hourly_rate = hours_worked

class Intern(Employee):
    def __init__(self, id, name, fixed_salary):
        super().__init__(id, name, fixed_salary)
        self.fixed_salary = fixed_salary


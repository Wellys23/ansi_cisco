class Employee:
    def __init__(self,first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@com.co"
    def Fullname(self):
        return "{} {}".format(self.first, self.last)
         
emp_a = Employee("John","Vasquez", 50000)
emp_b = Employee("Morom","Tray", 60000)

print(emp_a.email)
print(emp_b.email)
print(emp_a.Fullname())
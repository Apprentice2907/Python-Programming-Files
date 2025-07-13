class Employee:
    company="TCS"
    def show(self):
        print(f"The name of the employee is {self.name} and the company is {self.company}")

# class Programmer:
#     company="Google"
#     def show(self):
#         print(f"the name is{self.name and the company is {self.company}}")
#     def showlang():
#         print(f"the name is {self.name} and he is good in {self.lang} language")


class Programmer(Employee):
    company = "Google"
    def showlang(self):
        print(f"The name is {self.name} and he is good in {self.lang} language")

a= Employee()
b= Programmer()

print(a.company, b.company)
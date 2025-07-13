class Employee:
    name="Hacker"
    company="TCS"
    def show(self):
        print(f"The name of the employee is {self.name} and the company is {self.company}")

class Coder:
    lang ="Python"
    def printlang(self):
        print(f"Out of all the language here is your language: {self.lang}")


class Programmer(Employee, Coder):
    company = "Google"
    def showlang(self):
        print(f"The company is {self.company} and he is good in {self.lang} language")

a= Employee()
b= Programmer()

b.show()
b.printlang()
b.showlang()

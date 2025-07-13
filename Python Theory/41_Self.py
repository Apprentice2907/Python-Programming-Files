class Employee: 
    language = "Python" # This is a class attribute
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")


prince = Employee()
# prince.language = "JavaScript" # This is an instance attribute
# prince.greet()
prince.getInfo() 
# Employee.getInfo(prince)
 
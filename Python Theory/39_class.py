class Employee: 
    language = "Python" # This is a class attribute
    salary = 1200000


prince = Employee()
prince.name = "Prince" # This is an instance attribute
print(prince.name, prince.language, prince.salary)

rahul = Employee()
rahul.name = "Rahul Roto Robinson"
print(rahul.name, rahul.salary, rahul.language)

# Here name is instance attribute and salary and language are class attributes as they directly belong to the class

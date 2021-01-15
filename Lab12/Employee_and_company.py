class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    
    def get_name(self):
        return self.name
    
    def get_salary(self):
        return self.salary
    
    def set_name(self,name):
        self.name = name
    
    def set_salary(self,salary):
        self.salary = salary

class Company:
    def __init__(self):
        self.employee_list = []
    
    def get_employee_list(self):
        return self.employee_list
    
    def set_employee_list(self, employee_list):
        self.employee_list = employee_list
    
    def add_employee(self, new_employee):
        if isinstance(new_employee, Employee):
            self.employee_list.append(new_employee)
    
    def average_salary(self):
        sum = 0
        for employee in self.employee_list:
            sum += employee.get_salary()
        
        average = sum / len(self.employee_list)
        return average
    
    def display(self):
        for employee in self.employee_list:
            print(employee.get_name(), ':', employee.get_salary())
        
System76 = Company()

worker1 = Employee("Metin", 15000)
worker2 = Employee("nurlan", 15)
worker3 = Employee("Nurbala", 30000)

System76.add_employee(worker1)
System76.add_employee(worker2)
System76.add_employee(worker3)

print(System76.average_salary())
System76.display()


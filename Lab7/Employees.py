employees = {}
for _ in range(5):
    name = input("Enter employee's name: ")
    salary = float(input("Enter employee's salary: "))
    employees[name] = salary

print(employees)

best_three_salaries = sorted(employees.values())[-3:]
for name in employees.keys():
    salary = employees[name]
    if salary in best_three_salaries:
        print(name)

    

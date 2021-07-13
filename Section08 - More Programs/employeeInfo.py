number_of_employees = int(input('Enter the number of employees: '))
employees = {}
for i in range(number_of_employees):
    name = input('Enter employee name: ')
    salary = input('Enter employee salary: ')
    employees[name] = salary

while True:
    name = input('Enter employee name: ')
    salary = employees.get(name, -1)
    if salary == -1:
        print('Employee does not exist')
    else: print('The salary of the employee is', salary)

    choice = input('Do you want to continue? [Y/N]')
    if choice == 'N' or choice == 'n':
        break
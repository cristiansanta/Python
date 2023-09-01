

employee_file = open("Employees.txt", "r")
#print(employee_file.read())
#print(employee_file.readlines())
for employee in employee_file.readlines():
    print(employee)
employee_file.close()
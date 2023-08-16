from employeeFactory import EmployeeFactory
aD = EmployeeFactory.create_object('androidDeveloper')
wD = EmployeeFactory.create_object('webDeveloper')
print(aD.salary())
print(wD.salary())
student = {'name': 'John', 'age': 20, 'grade': 'A'}
print(student)
# {'name': 'John', 'age': 20, 'grade': 'A'}

employee = dict(name='Alice', department='Sales', salary=5000)
print(employee)
# {'name': 'Alice', 'department': 'Sales', 'salary': 5000}

print(employee["name"])
# Alice

print(employee.get("name"))
# Alice

employee["name"] = "Mike"
print(employee)
# {'name': 'Mike', 'department': 'Sales', 'salary': 5000}

employee["dob"] = "June 4, 1991"
print(employee)
# {'name': 'Mike', 'department': 'Sales', 'salary': 5000, 'dob': 'June 4, 1991'}

employee.pop("dob")
print(employee)
# {'name': 'Mike', 'department': 'Sales', 'salary': 5000}
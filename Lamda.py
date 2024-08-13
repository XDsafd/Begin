employees = [
    {"name": "Alice", "age": 30, "salary": 50000, "department": "HR"},
    {"name": "Bob", "age": 35, "salary": 60000, "department": "IT"},
    {"name": "Charlie", "age": 28, "salary": 45000, "department": "HR"},
    {"name": "David", "age": 40, "salary": 70000, "department": "IT"},
    {"name": "Eve", "age": 32, "salary": 55000, "department": "Marketing"}
]

# Tasks:

# 1. Use a lambda function with map() to create a list of all employee names.
nameList = list(map(lambda emp : emp['name'] ,employees))
print(nameList)

# 2. Use a lambda function with filter() to create a list of employees who are over 30 years old.
ageList = list(filter(lambda old: old['age'] > 30 , employees))
print("Employee over 30:", [old['name'] for old in ageList])
# 3. Use a lambda function with sorted() to sort the employees by salary in descending order.
salaryOrder= sorted(employees, key = lambda emp : emp["salary"], reverse = True)
print("Employees by salary descending:", [emp['name'] for emp in salaryOrder])

# 4. Use a lambda function with max() to find the employee with the highest salary.
highestSalary = max(employees, key = lambda emp : emp ['salary'])
print("Employee with the highest salary:",  highestSalary['name'])

# 5. Use a lambda function with map() to create a list of tuples containing just the name and department of each employee.
nameDeptList = list (map(lambda emp : (emp['name'], emp['department']), employees))
print("Name and deparment: ", nameDeptList)

# Write your solutions here

# Print the results of each task
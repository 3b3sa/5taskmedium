from dataclasses import dataclass
from functools import wraps

# Использовать dataclass:

# @dataclass
# class Employee:
#     name: str
#     salary: int
#     department: str

# Создать список сотрудников:

# employees = [
#     Employee("Alex", 100000, "IT"),
#     Employee("Bob", 80000, "HR"),
#     Employee("Charlie", 150000, "IT"),
#     Employee("Diana", 120000, "Sales"),
# ]

# Реализовать функцию:

# get_top_employees(employees, department, count)

# Она должна:
# 1. Отфильтровать сотрудников нужного отдела.
# 2. Отсортировать их по зарплате через lambda.
# 3. Вернуть count самых высокооплачиваемых сотрудников.

# Дополнительно написать декоратор log_call, который выводит:

# Calling get_top_employees
# Finished get_top_employees

# И применить его к функции.

# Здесь проверяется связка:
# dataclass → filter → lambda → sorted → decorator.

@dataclass
class Employee:
    name: str
    salary: int
    department: str

    def log_call(func):
        @wraps(func)
        def output():
            print("Calling get_top_employees")
            result = func()
            print("Finished get_top_employees")
            return result

    def employees(department):
        match = filter(key = lambda x: department == department)
        return match

    def department(salary):
        sort = sorted(salary, key=lambda x: x["count"])
        return sort

    def count(salary):
        best_count = sorted(salary)
        return best_count


    def get_top_employees(employees, department, count):
        pass
        # match = filter(key = lambda x: department == department)
        # sort = sorted(count, key=lambda x: x["count"])
        # best_count = sorted(count)


            

employees = [
    Employee("Alex", 100000, "IT"),
    Employee("Bob", 80000, "HR"),
    Employee("Charlie", 150000, "IT"),
    Employee("Diana", 120000, "Sales"),
]


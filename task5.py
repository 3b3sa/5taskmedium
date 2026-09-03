from dataclasses import dataclass
from functools import wraps
@dataclass
class Employee:
    name: str
    salary: int
    department: str

def log_call(func):
    @wraps(func)
    def output(*args, **kwargs):
        print(f"Calling get_top_employees")
        result = func(*args, **kwargs)
        print(f"Finished get_top_employees")
        return result
    return output

@log_call
def get_top_employees(employees, department, count):
    match = filter(lambda x: x.department == department, employees)

    sort = sorted(match, key=lambda x: x.salary, reverse = True)

    return sort[:count]

employees = [
    Employee("Alex", 100000, "IT"),
    Employee("Bob", 80000, "HR"),
    Employee("Charlie", 150000, "IT"),
    Employee("Diana", 120000, "Sales"),
]

test = get_top_employees(employees, "IT", 3)
print(test)
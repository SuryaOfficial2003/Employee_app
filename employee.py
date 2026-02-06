class Employee:
    def __init__(self, emp_id, name, salary, department, is_active=True):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary
        self.department = department
        self.is_active = is_active

    def display(self):
        print("\n--- Employee Details ---")
        print(f"ID         : {self.emp_id}")
        print(f"Name       : {self.name}")
        print(f"Salary     : {self.salary}")
        print(f"Department : {self.department}")
        print(f"Active     : {self.is_active}")

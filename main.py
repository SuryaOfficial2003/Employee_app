from db import get_connection
from employee import Employee
import psycopg2

# ------------------ CRUD Functions ------------------ #

def insert_employee():
    print("\n--- Insert Employee ---")
    emp_id = int(input("Enter Employee ID: "))
    name = input("Enter Name: ")
    salary = float(input("Enter Salary: "))
    department = input("Enter Department: ")

    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute("INSERT INTO employees (emp_id, name, salary, department) VALUES (%s, %s, %s, %s)",
                    (emp_id, name, salary, department))
        conn.commit()
        print("Employee inserted successfully.")
    except psycopg2.Error as e:
        print("Error:", e)
        conn.rollback()
    finally:
        cur.close()
        conn.close()


def display_employee():
    print("\n--- Display All Employees ---")
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT emp_id, name, salary, department, is_active FROM employees")
    rows = cur.fetchall()

    if not rows:
        print("No employees found.")
    else:
        for row in rows:
            emp = Employee(*row)
            emp.display()

    cur.close()
    conn.close()


def update_employee():
    print("\n--- Update Employee ---")
    emp_id = int(input("Enter Employee ID to update: "))
    name = input("Enter New Name: ")
    salary = float(input("Enter New Salary: "))
    department = input("Enter New Department: ")

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE employees SET name=%s, salary=%s, department=%s WHERE emp_id=%s",
                (name, salary, department, emp_id))

    if cur.rowcount == 0:
        print("Employee not found!")
    else:
        conn.commit()
        print("Employee updated successfully.")

    cur.close()
    conn.close()


def delete_employee():
    print("\n--- Delete Employee ---")
    emp_id = int(input("Enter Employee ID to delete: "))

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM employees WHERE emp_id=%s", (emp_id,))

    if cur.rowcount == 0:
        print("Employee not found!")
    else:
        conn.commit()
        print("Employee deleted successfully.")

    cur.close()
    conn.close()


def search_employee():
    print("\n--- Search Employee ---")
    emp_id = int(input("Enter Employee ID to search: "))

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT emp_id, name, salary, department, is_active FROM employees WHERE emp_id=%s", (emp_id,))
    row = cur.fetchone()

    if row:
        emp = Employee(*row)
        emp.display()
    else:
        print("Employee not found!")

    cur.close()
    conn.close()


# ------------------ Menu ------------------ #
def menu():
    while True:
        print("\n===== Employee Management Menu =====")
        print("1. Insert Employee")
        print("2. Display Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Search Employee")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            insert_employee()
        elif choice == "2":
            display_employee()
        elif choice == "3":
            update_employee()
        elif choice == "4":
            delete_employee()
        elif choice == "5":
            search_employee()
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    menu()

from models import Category, Customer, Employee, Salary
from tabulate import tabulate

def category_ui():
    obj = Category()
    text = """
                        1) Add Category
                        2) Update Category
                        3) Delete Category
                        4) Show Category
                        5) Exit
                           >>>>"""
    key = int(input(text))
    match key:
        case 1:
            obj.add_category()
        case 2:
            obj.update_category()
        case 3:
            obj.delete_category()
        case 4:
            print(tabulate(obj.show_category(), ('Id', 'Category', 'Created Time'), 'rounded_grid'))
        case 5:
            UI()
    category_ui()


def emplotee_ui():
    obj = Employee()
    text = """
                        1) Add Employee
                        2) Update Employee
                        3) Delete Employee
                        4) Show Employee
                        5) Exit
                           >>>>"""
    key = int(input(text))
    match key:
        case 1:
            obj.add_employee()
        case 2:
            obj.update_employee()
        case 3:
            obj.delete_employee()
        case 4:
            headers = ('ID', 'Name', 'Category_id', 'Work Time', 'Worker Salary', 'Worker Info', 'Created Time')
            print(tabulate(obj.show_employee(), headers, 'rounded_grid'))
        case 5:
            UI()
    emplotee_ui()


def customer_ui():
    obj = Customer()
    text = """
                        1) Add Customer
                        2) Update Customer
                        3) Delete Customer
                        4) Show Customer
                        5) Exit
                           >>>>"""
    key = int(input(text))
    match key:
        case 1:
            obj.add_customer()
        case 2:
            obj.update_customer()
        case 3:
            obj.delete_customer()
        case 4:
            headers = ('ID', 'Fullname', 'Diagnosis', 'Doctor Id', 'Ifno', 'Created Time')
            print(tabulate(obj.show_customer(), headers, 'rounded_grid'))
        case 5:
            UI()
    customer_ui()


def salary_ui():
    obj = Salary()
    text = """
                        1) Add Salary
                        2) Update Salary
                        3) Delete Salary
                        4) Show Salary
                        5) Exit
                           >>>>"""
    key = int(input(text))
    match key:
        case 1:
            obj.add_salary()
        case 2:
            obj.update_salary()
        case 3:
            obj.delete_salary()
        case 4:
            headers = ('ID', 'User Id', 'Payment', 'Created Time')
            print(tabulate(obj.show_salary(), headers, 'rounded_grid'))
        case 5:
            UI()
    salary_ui()


def UI():
    text = """
           1)Category
           2)Employee
           3)Customer
           4)Salary
           5)Break
                >>>>"""
    while True:
        key = int(input(text))

        match key:
            case 1:
                category_ui()
            case 2:
                emplotee_ui()
            case 3:
                customer_ui()
            case 4:
                salary_ui()
            case 5:
                break

UI()
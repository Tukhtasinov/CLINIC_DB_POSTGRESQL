from DB import DB
from tabulate import tabulate

# class CRUD(DB):
#     def __init__(self, **kwargs):
#         self.kwargs = kwargs
#
#
#
#     def add_data(self):
#         query = f"""SELECT column_name FROM information_schema.columns WHERE table_name = '{self.kwargs.get('table_name')}';"""
#         self.cur.execute(query)
#         columns = self.cur.fetchall()
#
#         cols = ''
#         add_data = dict()
#         for i, v in enumerate(columns):
#             if v[0] == 'id' or v[0] == 'created_at':
#                 continue
#             cols += ',' + v[0]
#
#             item = input(f'Enter {v[0]}:')
#             add_data.update({f'{v[0]}': f'{item}'})
#         param = ''
#         for i in add_data.values():
#             param += i + ','
#         param = param.strip(',')
#         cols = cols.strip(',')
#         query_insert = f"""insert into {self.kwargs.get('table_name')}({cols})
#         values('{param}')"""
#         self.cur.execute(query_insert)
#         self.con.commit()
# dic = {
#     'table_name': 'employees'
# }
# obj = CRUD(**dic)
# obj.add_data()


class Category(DB):

    def add_category(self):
        category_name = input('Enter category_name:')
        query_add = f"""insert into categorys(category_name) values ('{category_name}');"""
        param = (category_name,)
        self.cur.execute(query_add, param)
        self.con.commit()

    def update_category(self):

        print(tabulate(self.show_category(), ('Id', 'Category', 'Created Time'), 'rounded_grid'))
        select_id = int(input('Choose Id from table:'))
        new_cate_name = input('Yangi category_name kirit:')
        query_update = """update categorys set category_name = %s where id = %s;"""
        param = (new_cate_name, select_id)
        self.cur.execute(query_update, param)
        self.con.commit()

    def delete_category(self):
        print(tabulate(self.show_category(), ('Id', 'Category', 'Created Time'), 'rounded_grid'))
        select_id = int(input("O'chirmoqchi bo'lgan Id kirit:"))
        query_delete = """delete from categorys where id = %s;"""
        param = (select_id,)
        self.cur.execute(query_delete, param)
        self.con.commit()


class Employee(DB):

    def add_employee(self):
        worker_name = str(input('Enter worker name:'))
        print(tabulate(self.show_category(), ('Id', 'Category' , 'Created Time'), 'rounded_grid'))
        category_id = int(input('Select Id:'))
        work_time = str(input('Enter work Time(00:00 to 00:00):'))
        worker_salary = int(input('Oylik maoshni kiriting:'))
        worker_info = str(input('Enter worker info:'))
        query_add = """insert into employees(worker_name, category_id, work_time, worker_salary, worker_info) values(%s, %s, %s, %s, %s)"""
        param = (worker_name,category_id, work_time,worker_salary, worker_info)
        self.cur.execute(query_add, param)
        self.con.commit()

    def update_employee(self):
        headers = ('ID', 'Name', 'Category_id', 'Work Time', 'Worker Salary', 'Worker Info', 'Created Time')
        print(tabulate(self.show_employee(), headers, 'rounded_grid'))
        select_id = int(input('Select Id that you should update:'))
        query_col = """SELECT column_name FROM information_schema.columns WHERE table_name = 'employees';"""
        self.cur.execute(query_col)
        cols = self.cur.fetchall()
        for i, v in enumerate(cols):
            print(f'{i+1}) {v[0]}')

        old_item_type = cols[int(input('Select N:')) - 1][0]
        new_data = input('Enter new item:')
        if ('id' in old_item_type) or ('salary' in old_item_type):
            new_data = int(new_data)
        query_update = f"""update employees set {old_item_type} = %s where worker_id = %s;"""
        param = (new_data, select_id)
        self.cur.execute(query_update, param)
        self.con.commit()

    def delete_employee(self):
        headers = ('ID', 'Name', 'Category_id', 'Work Time', 'Worker Salary', 'Worker Info', 'Created Time')
        print(tabulate(self.show_employee(), headers, 'rounded_grid'))
        select_id = int(input('Select Id that you should delete:'))
        query_delete = """delete from employees where worker_id = %s;"""
        param = (select_id,)
        self.cur.execute(query_delete, param)
        self.con.commit()


class Customer(DB):

    def add_customer(self):
        fullname = input('Enter User Fullname:')
        user_dia = input('Enter User diagnosis:')
        headers = ('ID', 'Name', 'Category_id', 'Work Time', 'Worker Salary', 'Worker Info', 'Created Time')
        print(tabulate(self.show_employee(), headers, 'rounded_grid'))
        doctor_id = int(input('Select Id that Doctor Id:'))
        user_info = input('Enter User info:')
        query_add = """insert into customers(fullname, user_diagnosis, doctor_id, user_info) values (%s, %s, %s, %s);"""
        param = (fullname, user_dia, doctor_id, user_info)
        self.cur.execute(query_add, param)
        self.con.commit()

    def update_customer(self):
        headers = ('ID', 'Fullname', 'Diagnosis', 'Doctor Id', 'Ifno', 'Created Time')
        print(tabulate(self.show_customer(), headers, 'rounded_grid'))
        select_id = int(input('Select Id that you should update:'))
        query_col = """SELECT column_name FROM information_schema.columns WHERE table_name = 'customers';"""
        self.cur.execute(query_col)
        cols = self.cur.fetchall()
        for i, v in enumerate(cols):
            print(f'{i + 1}) {v[0]}')

        old_item_type = cols[int(input('Select N:')) - 1][0]
        new_data = input('Enter new item:')
        if 'id' in old_item_type:
            new_data = int(new_data)
        query_update = f"""update customers set {old_item_type} = %s where user_id = %s;"""
        param = (new_data, select_id)
        self.cur.execute(query_update, param)
        self.con.commit()

    def delete_customer(self):
        headers = ('ID', 'Fullname', 'Diagnosis', 'Doctor Id', 'Ifno', 'Created Time')
        print(tabulate(self.show_customer(), headers, 'rounded_grid'))
        select_id = int(input('Select Id that Delete:'))
        query_delete = """delete from customers where user_id = %s"""
        param = (select_id, )
        self.cur.execute(query_delete, param)
        self.con.commit()


class Salary(DB):

    def add_salary(self):
        headers = ('ID', 'Fullname', 'Diagnosis', 'Doctor Id', 'Ifno', 'Created Time')
        print(tabulate(self.show_customer(), headers, 'rounded_grid'))
        user_id = int(input('Select Id that you should update:'))
        pay = int(input('Enter payment:'))
        query_add = """insert into salaries(user_id, pay) values (%s, %s);"""
        param = (user_id, pay)
        self.cur.execute(query_add, param)
        self.con.commit()

    def update_salary(self):
        headers = ('ID', 'User Id', 'Payment', 'Created Time')
        print(tabulate(self.show_salary(), headers, 'rounded_grid'))
        select_id = int(input('Select Id that you should update:'))
        query_col = """SELECT column_name FROM information_schema.columns WHERE table_name = 'salaries';"""
        self.cur.execute(query_col)
        cols = self.cur.fetchall()
        for i, v in enumerate(cols):
            print(f'{i + 1}) {v[0]}')

        old_item_type = cols[int(input('Select N:')) - 1][0]
        new_data = int(input('Enter new item:'))
        query_update = f"""update salaries set {old_item_type} = %s where user_id = %s;"""
        param = (new_data, select_id)
        self.cur.execute(query_update, param)
        self.con.commit()

    def delete_salary(self):
        headers = ('ID', 'User Id', 'Payment', 'Created Time')
        print(tabulate(self.show_salary(), headers, 'rounded_grid'))
        select_id = int(input('Select Id that you should update:'))
        query_delete = f"""delete from salaries where id = {select_id}"""
        self.cur.execute(query_delete)
        self.con.commit()

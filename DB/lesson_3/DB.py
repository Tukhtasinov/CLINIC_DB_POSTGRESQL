from dataclasses import dataclass
import psycopg2

@dataclass
class DB():
    con = psycopg2.connect(
        dbname="postgres",
        user='postgres',
        password='doni',
        host='localhost',
        port=5432
    )

    cur = con.cursor()
    def show_category(self):
        query_show = """select * from categorys"""
        self.cur.execute(query_show)
        show_data = self.cur.fetchall()
        return show_data
    def show_employee(self):
        query_show = """select * from employees"""
        self.cur.execute(query_show)
        show_data = self.cur.fetchall()
        return show_data
    def show_customer(self):
        query_show = """select * from customers"""
        self.cur.execute(query_show)
        show_data = self.cur.fetchall()
        return show_data

    def show_salary(self):
        query_show = """select * from salaries"""
        self.cur.execute(query_show)
        show_data = self.cur.fetchall()
        return show_data
    query_categorys = """
            create table if not exists Categorys(
               id serial primary key,
               category_name varchar(255),
               created_at timestamp default current_timestamp not null
            );
            """
    query_employees = """
    create table if not exists Employees(
    worker_id serial primary key,
    worker_name varchar(255),
    category_id integer not null,
    work_time varchar(200),
    worker_salary int ,
    worker_info text,
    created_at timestamp default current_timestamp not null
    );
            """
    query_customers = """create table if not exists Customers(
    user_id serial primary key,
    fullname varchar(255),
    user_diagnosis varchar(255),
    doctor_id int not null,
    user_info text,
    created_at timestamp default current_timestamp not null
    );"""
    query_salaries = """create table if not exists Salaries(
    salery_id serial primary key,
    user_id int,
    pay int,
    created_at timestamp default current_timestamp not null
                 );"""

    cur.execute(query_categorys)
    cur.execute(query_employees)
    cur.execute(query_salaries)
    cur.execute(query_customers)
    con.commit()
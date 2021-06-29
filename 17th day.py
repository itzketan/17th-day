import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@mysqlketangurav22"
)
print(mydb)

import mysql.connector
db_connection = mysql.connector.connect(
  host= "localhost",
  user= "root",
  passwd= "@mysqlketangurav22"
  )
# creating database_cursor to perform SQL operation
db_cursor = db_connection.cursor()
# executing cursor with execute method and pass SQL query
db_cursor.execute("CREATE DATABASE my_first_db")
# get list of all databases
db_cursor.execute("SHOW DATABASES")
#print all databases
for db in db_cursor:
	print(db)


import mysql.connector
db_connection = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="@mysqlketangurav22",
  database="my_first_db"
  )
db_cursor = db_connection.cursor()
#Here creating database table as student'
db_cursor.execute("CREATE TABLE student (id INT, name VARCHAR(255))")
#Get database table'
db_cursor.execute("SHOW TABLES")
for table in db_cursor:
    print(table)

import mysql.connector


con = mysql.connector.connect(
	host="localhost", user="root", password="@mysqlketangurav22", database="emp")


# Function To Check if Employee with
# given Id Exist or Not

def check_employee(employee_id):
    # Query to select all Rows f
    # rom employee Table
    sql = 'select * from empd where id=%s'

    # making cursor buffered to make
    # rowcount method work properly
    c = con.cursor(buffered=True)
    data = (employee_id,)

    # Executing the SQL Query
    c.execute(sql, data)

    # rowcount method to find
    # number of rows with given values
    r = c.rowcount

    if r == 1:
        return True
    else:
        return False


# Function to mAdd_Employee

def Add_Employ():
    Id = input("Enter Employ Id : ")

    # Checking if Employee with given Id
    # Already Exist or Not
    if (check_employee(Id) == True):
        print("Employee aready exists\nTry Again\n")
        menu()

    else:
        Name = input("Enter Employ Name : ")
        Post = input("Enter Employ Post : ")
        Salary = input("Enter Employ Salary : ")
        data = (Id, Name, Post, Salary)

        # Inserting Employee details in the Employee
        # Table
        sql = 'insert into empd values(%s,%s,%s,%s)'
        c = con.cursor()

        # Executing the SQL Query
        c.execute(sql, data)

        # commit() method to make changes in the table
        con.commit()
        print("Employ Added Successfully ")
        menu()


# Function to Display All Employees
# from Employee Table

def Display_Employees():
    # query to select all rows from
    # Employee Table
    sql = 'select * from empd'
    c = con.cursor()

    # Executing the SQL Query
    c.execute(sql)

    # Fetching all details of all the
    # Employees
    r = c.fetchall()
    for i in r:
        print("Employ Id : ", i[0])
        print("Employ Name : ", i[1])
        print("Employ Post : ", i[2])
        print("Employ Salary : ", i[3])
        print("-----------------------------\
		-------------------------------------\
		-----------------------------------")
    menu()


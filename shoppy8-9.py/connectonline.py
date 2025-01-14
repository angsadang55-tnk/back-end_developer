import mysql.connector as mysqlcon
mydb = mysqlcon.connect(
    host="localhost",
    user='root',
    password="1111",
    database='shopping'
    )
print(mydb)
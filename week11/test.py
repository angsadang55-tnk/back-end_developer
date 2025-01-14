import database

def select_all():
    table=input('ป้อนวิชาที่ต้องการค้นหา')
    mycursor = database.mydb.cursor()
    mycursor.execute(f"SELECT * FROM {table}")
    myresulf = mycursor.fetchall()
    for i in myresulf:
        print(i)

def select_students(table):

    mycursor = database.mydb.cursor()
    name = input('ป้อนชื่อที่ต้องการค้นหา')
    mycursor.execute(f"SELECT * FROM {table} where name like '%{name}%' ")
    myresulf = mycursor.fetchall()
    for i in myresulf:
        print(i)
table ="subject"
select_all()
select_students(table)
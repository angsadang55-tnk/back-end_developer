import database
mycursor = database.mydb.cursor() 

def all(table):
    mycursor.execute(f"SELECT * FROM {table}")
    myresulf = mycursor.fetchall()
    for i in myresulf:
        print(i)

def subject(table):
    sql = "INSERT INTO subject VALUES (%s, %s)"
    a = int(input("id_subject : "))
    b = str(input("name : "))
    val = (a,b)
    mycursor.execute(sql,val)
    database.mydb.commit() 
subject(table)                                                                                                                                                                                                                                                                                 


ของshopping2

import connectonline
import online
mycursor = connectonline.mydb.cursor()

def select_all():   
    show_table()
    table = input('ใส่หัวข้อที่ต้องการเพิ่มข้อมูล')
    mycursor.execute(f"SELECT * FROM {table}")
    myresulf = mycursor.fetchall()
    for i in myresulf:
        print(i)

def cat(): 
    print('เพิ่มข้อมูล')
    id = input('ID :')
    name = input('name :')
    val = (id,name)
    sql = "INSERT INTO subject VALUES (%s, %s)"
    mycursor.execute(sql,val)
    connectonline.mydb.commit() 
    print('เพิ่มข้อมูลสำเร็จ')
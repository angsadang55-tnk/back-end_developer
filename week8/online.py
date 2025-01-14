import connectonline
mycursor = connectonline.mydb.cursor()

def show_table():
    mycursor.execute("SHOW TABLES")
    table = mycursor.fetchall()
    print('หัวข้อทั้งหมด')
    for i in table:
        print(i)

def select_all():   
    show_table()
    table = input('ใส่หัวข้อที่ต้องการค้นหา')
    mycursor.execute(f"SELECT * FROM {table}")
    myresulf = mycursor.fetchall()
    for i in myresulf:
        print(i)

def select_catagory():
    name = input('ป้อนชื่อที่ต้องการค้นหา')
    mycursor.execute(f"SELECT * FROM catagories where namecatagory like '%{name}%' ")
    myresulf = mycursor.fetchall()
    for i in myresulf:
        print(i)

def select_order():
    id = input('ป้อนชื่อที่ต้องการค้นหา')
    mycursor.execute(f"SELECT * FROM orders where order_id like '%{id}%' ")
    myresulf = mycursor.fetchall()
    for i in myresulf:
        print(i)

def select_product():
    name = input('ป้อนชื่อที่ต้องการค้นหา')
    mycursor.execute(f"SELECT * FROM products where nameproduct like '%{name}%' ")
    myresulf = mycursor.fetchall()
    for i in myresulf:
        print(i)

def select_users():
    name = input('ป้อนชื่อที่ต้องการค้นหา')
    mycursor.execute(f"SELECT * FROM users where nameusers like '%{name}%' ")
    myresulf = mycursor.fetchall()
    for i in myresulf:
        print(i)

select_all()



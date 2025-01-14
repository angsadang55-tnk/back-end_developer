import connectonline
import datetime

mycursor = connectonline.mydb.cursor()

def cat():
    print("เพิ่มข้อมูลในตาราง categories:")
    id = int(input("ID: "))
    name = str(input("Name: "))
    val = (id, name)
    sql = "INSERT INTO categories (id, name) VALUES (%s, %s)"
    mycursor.execute(sql, val)
    connectonline.mydb.commit()
    print("เพิ่มข้อมูลสำเร็จใน categories")

def order():
    print("เพิ่มข้อมูลในตาราง orders:")
    id = int(input("Order ID: "))
    iduser = int(input("User ID: "))
    time = datetime.datetime.now()
    total = float(input("Total Amount: "))
    status = str(input("Status (รอดำเนินการ, กำลังจัดส่ง, จัดส่งสำเร็จ, ยกเลิกรายการ): "))
    product_id = int(input("Product ID: "))
    val = (id, iduser, time, total, status, product_id)
    sql = """INSERT INTO orders (id, user_id, order_time, total, status, product_id)
             VALUES (%s, %s, %s, %s, %s, %s)"""
    mycursor.execute(sql, val)
    connectonline.mydb.commit()
    print("เพิ่มข้อมูลสำเร็จใน orders")

def product():
    print("เพิ่มข้อมูลในตาราง products:")
    id = int(input("Product ID: "))
    name = str(input("Name: "))
    description = str(input("Description: "))
    price = float(input("Price: "))
    stock = int(input("Stock: "))
    category_id = int(input("Category ID: "))
    val = (id, name, description, price, stock, category_id)
    sql = """INSERT INTO products (id, name, description, price, stock, category_id)
             VALUES (%s, %s, %s, %s, %s, %s)"""
    mycursor.execute(sql, val)
    connectonline.mydb.commit()
    print("เพิ่มข้อมูลสำเร็จใน products")

def user():
    print("เพิ่มข้อมูลในตาราง users:")
    id = int(input("User ID: "))
    name = str(input("Name: "))
    password = str(input("Password: "))
    email = str(input("Email: "))
    role = str(input("Role (admin/user): "))
    val = (id, name, password, email, role)
    sql = """INSERT INTO users (id, name, password, email, role)
             VALUES (%s, %s, %s, %s, %s)"""
    mycursor.execute(sql, val)
    connectonline.mydb.commit()
    print("เพิ่มข้อมูลสำเร็จใน users")

def add():
    # Assume `online.show_table()` displays available tables and returns their names as a list
    tables = ['categories', 'orders', 'products', 'users']  # ตัวอย่าง
    print("ตารางที่มีให้เลือก:", ", ".join(tables))
    c = input("เลือกตารางที่ต้องการเพิ่มข้อมูล: ").strip().lower()

    if c == "categories":
        cat()
    elif c == "orders":
        order()
    elif c == "products":
        product()
    elif c == "users":
        user()
    else:
        print("ไม่พบตารางที่เลือก")

add()

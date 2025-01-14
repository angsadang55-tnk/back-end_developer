import connectonline
import online
import datetime
mycursor = connectonline.mydb.cursor()

def cat(): 
    print('เพิ่มข้อมูล')
    id = int(input('ID :'))
    name = str(input('name :'))
    val = (id,name)
    sql = "INSERT INTO categories VALUES (%s, %s)"
    mycursor.execute(sql,val)
    connectonline.mydb.commit() 
    print('เพิ่มข้อมูลสำเร็จ')

# cat()

def order(): 
    print('เพิ่มข้อมูล')
    id = int(input('ID :'))
    iduser = int(input('IDusers :'))
    time = datetime.datetime.todayorders()
    print(time.strftime("%d/m/%y %H:%M:%S"))
    ottal = float(input('total amont :'))
    sta = str(input("status(รอดำเนินการ,กำลังจัดส่ง,จัดส่งสำเร็จ,ยกเลิกรายการ :)"))
    product = int(input('IDproduct :'))
    val = (id,iduser,time,)
    sql = "INSERT INTO orders VALUES (%s, %s, %s, %s, %s)"
    mycursor.execute(sql,val,ottal,sta,product)
    connectonline.mydb.commit() 
    print('เพิ่มข้อมูลสำเร็จ')

order()

def product(): 
    print('เพิ่มข้อมูล')
    id = int(input('ID :'))
    name = str(input('name :'))
    des = str(input('description :'))
    price = float(input('price :'))
    stock = int(input('stock :'))
    idcat = int(input('category_id :'))
    val = (id,name,des,price,stock,idcat)
    sql = "INSERT INTO products VALUES (%s, %s, %s, %s, %s, %s)"
    mycursor.execute(sql,val)
    connectonline.mydb.commit() 
    print('เพิ่มข้อมูลสำเร็จ')

product()

def user(): 
    print('เพิ่มข้อมูล')
    id = int(input('ID :'))
    name = str(input('name :'))
    pas = str(input('password :'))
    email = float(input('email :'))
    role = str(input('role :'))
    val = (id,name,pas,email,role)
    sql = "INSERT INTO users VALUES (%s, %s, %s, %s, %s,)"
    mycursor.execute(sql,val)
    connectonline.mydb.commit() 
    print('เพิ่มข้อมูลสำเร็จ')

user()
def add():
    online.show_table()
    c = input('เลือกข้อมูลที่ต้องการเพิ่มข้อมูล : ')
    if c == 'categories' :
        cat()
    elif c == 'orders' :
        order()
    elif c == 'products' :
        product()
    elif c == 'users' :
        user()
add()
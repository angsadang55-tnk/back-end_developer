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

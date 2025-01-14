import database
mycursor = database.mydb.cursor
def editdb(table):
    if table == "student":
        id = int(input('ใส่เลขไอดีที่ต้องการจะเปลี่ยน'))
        call = input('ใส่คอรัมที่ต้องการจะเปลี่ยน')
        vall = input('ใส่ค่าที่ต้องการจะเปลี่ยน')
        sql = f"UPDATE student SET{call}= %s WHERE id = %s"
        val = (call,vall,id)
        mycursor.execute(sql,val)
        database.mydb.commit()

    editdb("student")

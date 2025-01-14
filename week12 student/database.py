import database
mycursor = database.mydb.cursor() #เก็บการทำงานของmysq)
mycursor. execute("INSERT INTO subject VALUES ('7', 'Test2')")
database.mydb.comnit() # ปืนยันการเปลี่ยนแปลงในdb
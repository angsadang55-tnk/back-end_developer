print("ตรวจสอบเกรดเฉลี่ย")
g = int(input("โปรดใส่เลข0-100 = "))
if g < 0 or g > 100 :
    print("ใส่เลข0-100")
elif g >= 80:
    print("คุณได้เกรด4")
elif g >= 70:
    print("คุณได้เกรด3")
elif g >= 60:
    print("คุณได้เกรด2")
elif g >= 50:
    print("คุณได้เกรด1")
else :
    print("ป้อนเลขไม่ถูกต้อง")


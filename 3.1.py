while(True):
    num = int(input())
    if(num == -1):
        print("Tq")
        break
    if(num>100):
        print("คะแนนของคุณไม่อยู่ในช่วงที่ถูกต้อง")
    elif(num>= 80):
        print("คุณได้เกรด A")
    elif(num>= 70):
        print("คุณได้เกรด B")
    elif(num>= 60):
        print("คุณได้เกรด C")
    elif(num>= 50):
        print("คุณได้เกรด D")
    elif(num>= 0 and num <50):
        print("เสียใจด้วยนะครับ  คุณได้เกรด F")
    else:
        print("คะแนนของคุณไม่อยู่ในช่วงที่ถูกต้อง")



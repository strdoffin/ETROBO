from turtle import *

t = Turtle()
t.color("blue")
t.shape("turtle")
t.speed(10)
t.pensize(4)


n = int(input())
if(n >=3 and n<=6):
    for i in range(0,n):
        t.forward(50)
        t.left(360/n)
    mainloop()
else:
    print("ไม่สามารถวาดรูปสามเหลี่ยมได้ เพราะความยาวติดลบ")

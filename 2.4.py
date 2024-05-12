from turtle import *

t = Turtle()
t.color("blue")
t.shape("turtle")
t.speed(10)
t.pensize(4)


w = int(input())
if(w>=0):
    for i in range(0,3):
        t.forward(w)
        t.left(120)
    mainloop()
else:
    print("ไม่สามารถวาดรูปสามเหลี่ยมได้ เพราะความยาวติดลบ")


from turtle import *
t= Turtle()
t.color("blue")
t.shape("turtle")
t.pensize(3)
t.speed(100)
def vshape():
    t.left(25)
    t.forward(25)
    t.left(180)
    t.forward(25)
    t.left(130)
    t.forward(25)
    t.left(180)
    t.forward(25)
    t.left(205)

def branch():
    t.forward(40)
    vshape()
    t.forward(20)
    vshape()
    t.forward(20)
    vshape()
    t.forward(20)
    vshape()
    t.left(180)
    t.forward(100)


def main():
    for i in range(0,3):
        t.left(60)
        branch() 
        branch() 
  


main()
mainloop()
import turtle
bob = turtle.Turtle()
print(bob)
#turtle.mainloop()
#for i in range(4):
 #   bob.fd(100)
  #  bob.lt(90)
def square(t,length):
    for i in range (4):
        t.fd(length)
        t.lt(90)

def polygon(t,length,n):
    for i in range (n):
        t.fd(length)
        t.lt(360/n)
#polygon(bob,2,100)


def circle(t,r):
    polygon(t,1,int(2*3.14*r))
import math
def circle1(t,r):
    circumference = 2*math.pi*r
    n = 50
    length = circumference / n
    polygon(t,length,n)
def circle2(t,r):
    circumference = 2*math.pi*r
    n = int(circumference / 3)+3
    length = circumference / n
    polygon(t,length,n)
#circle2(bob,100)
#circle(bob,100)
#circle(bob,30)

def arc(t,r,angle):
    for i in range (int(2*3.14*r*(angle
                                  /360))):
        t.fd(1)
        t.lt(360/(2*3.14*r))
#arc(bob,100,270)
def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)
def arc1(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)
arc1(bob,100,90)

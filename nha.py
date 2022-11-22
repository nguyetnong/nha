import turtle


def draw_hcn(h,toado,dai,rong,mau):
    h.penup()
    h.goto(toado)
    h.pendown()
    h.begin_fill()
    h.color(mau)
    
    
    for i in range(2):
        h.forward(dai)
        h.left(90)
        h.forward(rong)
        h.left(90)
    h.end_fill()
    
t=turtle.Turtle()
t.pensize(3)

def dagiac(h,toado,n,canh,mau):
    h.penup()
    h.goto(toado)
    h.pendown()
    h.begin_fill()
    h.color(mau)
    angle=(n-2)*180/n
    
    h.left(180-angle)
    h.circle(-canh,steps=n)
    h.end_fill()
    
def hinhthangcan(h,toado1,toado2,toado3,toado4,toado5,mau="brown"):
    
    h.penup()
    h.goto(toado1)
    h.pendown()
    h.begin_fill()
    h.color(mau)
    h.goto(toado2)
    h.goto(toado3)
    h.goto(toado4)
    h.goto(toado5)
    h.end_fill()

draw_hcn(t,(0,0),200,150,"yellow")
draw_hcn(t,(60,0),70,90,"blue")
draw_hcn(t,(100,150),15,90,"brown")
dagiac(t,(0,150),3,85,"orange")
dagiac(t,(-100,-100),3,80,"green")
dagiac(t,(-165,110),3,60,"green")
dagiac(t,(-200,110),3,40,"green")
t.right(120)
hinhthangcan(t,(-190,-100),(-160,-100),(-150,-200),(-200,-200),(-190,-100))

turtle.done()
         
         
         
         
         
         
         
         
         
         
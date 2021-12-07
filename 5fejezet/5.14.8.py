import turtle
def oszlopok(t, magassag):
    if (magassag<100):
        t.color("green")
    elif(magassag<200):
        t.color("yellow")
    else:
        t.color("red")

    t.begin_fill()           
    t.left(90)
    t.forward(magassag)
    t.write("  "+ str(magassag))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(magassag)
    t.left(90)
    t.penup()
    t.end_fill()             
    t.forward(10)
    t.pendown()


a = turtle.Screen()         
a.bgcolor("lightblue")

Eszti = turtle.Turtle()      

Eszti.speed(100)  
Eszti.color("blue", "red")



xs = [48,117,200,240,160,260,220]

for S in xs:
    oszlopok(Eszti, S)
    
a.mainloop()
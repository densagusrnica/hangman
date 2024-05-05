from turtle import *

Screen().setup(1000, 800)

shape("turtle")
showturtle()
goto(0,0)
goto(100, 0)
penup()
goto(100, 100)
pendown()
goto(200, 100)
dot(200, "green")

pensize(7)
pencolor("blue")
goto(200, -200)

mainloop()
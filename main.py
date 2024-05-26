from turtle import *

def draw_square(topleftpoint, lenedge):

    x = topleftpoint[0]
    y = topleftpoint[1]
    points = [
        [x,y],
        [x + lenedge, y],
        [x + lenedge, y - lenedge],
        [x,y - lenedge]
    ]
    draw_line(points[0], points[1])
    draw_line(points[1], points[2])
    draw_line(points[2], points[3])
    draw_line(points[3], points[0])

def draw_secret(word):
    lenedge = 100
    interval = 20
    wordwidth = len(word) * lenedge + interval * (len(word) - 1)
    startpoint = [ -wordwidth // 2, -250]
    for x in range (len(word)):
        draw_square(startpoint, lenedge)
        startpoint[0] += interval + lenedge

def draw_alphabet():
    global alphabetDict
    alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
    x = 100
    y = 250
    fontSize = 40
    for k in range(len(alphabet)):
        goto(x, y)
        char = alphabet[k]
        write(char, align = 'center', font = ("Comic Sans MS", fontSize, "bold"))
        alphabetDict[char] = (x, y + fontSize // 2)
        x += 100
        if x >= 500:
            x = 100
            y -= fontSize * 2

def draw_line(point1, point2):
    penup()
    goto(point1[0], point1[1])
    pendown()
    goto(point2[0], point2[1])
    penup()


def draw_circle(point1, radius):
    penup()
    goto(point1[0], point1[1])
    pendown()
    circle(-radius)
    penup()
    goto(point1[0], point1[1]-radius * 2)

Screen().setup(1000, 800)

alphabetDict = {}
shape("classic")
showturtle()

pensize(5)
draw_line((-400, -180),(-70, -180))
draw_line((-100, -180),(-100, 280))
draw_line((-100, 280),(-270, 280))
draw_line((-270, 280),(-270, 220))
draw_circle((-270, 220), 50)
draw_line((-270, 120),(-270, -40))
draw_line((-270, 100),(-330, 30))
draw_line((-270, 100),(-210, 30))
draw_line((-270, -40),(-330, -150))
draw_line((-270, -40),(-210, -150))
draw_secret("f")
draw_alphabet()
mainloop()
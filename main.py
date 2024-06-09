from turtle import *

def draw_square(topleftpoint, lenedge):

    x = topleftpoint[0]
    y = topleftpoint[1]
    size = 5
    points = [
        [x,y],
        [x + lenedge, y],
        [x + lenedge, y - lenedge],
        [x,y - lenedge]
    ]
    draw_line(points[0], points[1], size)
    draw_line(points[1], points[2], size)
    draw_line(points[2], points[3], size)
    draw_line(points[3], points[0], size)

def draw_error(num_error):
    match num_error:
        case 1:
            draw_line((-400, -180), (-70, -180))
        case 2:
            draw_line((-100, -180), (-100, 280))
        case 3:
            draw_line((-100, 280), (-270, 280))
        case 4:
            draw_line((-270, 280), (-270, 220))
        case 5:
            draw_circle((-270, 220), 50)
        case 6:
            draw_line((-270, 120), (-270, -40))
        case 7:
            draw_line((-270, 100), (-330, 30))
        case 8:
            draw_line((-270, 100), (-210, 30))
        case 9:
            draw_line((-270, -40), (-330, -150))
        case 10:
            draw_line((-270, -40), (-210, -150))

def draw_secret(word):
    global secretCoords
    lenEdge = 100
    interval = 20
    wordWidth = len(word) * lenEdge + interval * (len(word) - 1)
    startpoint = [-wordWidth // 2, -250]
    for x in range(len(word)):
        draw_square(startpoint, lenEdge)
        secretCoords.append([startpoint[0] + lenEdge // 2, startpoint[1] - lenEdge])
        startpoint[0] += interval + lenEdge
    print(secretCoords)

def draw_letter(coord, char, fontSize, fontColor = "black"):
    goto(coord)

    oldColor = pen()["pencolor"]
    oldFillColor = pen()["fillcolor"]

    pencolor(fontColor)
    fillcolor(oldFillColor)
    write(char, align='center', font=("Comic Sans MS", fontSize, "bold"))

    pencolor(oldColor)
    pencolor(oldFillColor)

def draw_alphabet():
    global alphabetDict
    alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
    x = 100
    y = 250
    fontSize = 40
    for k in range(len(alphabet)):
        char = alphabet[k]
        draw_letter((x, y), char, fontSize)
        alphabetDict[char] = (x, y)
        x += 100
        if x >= 500:
            x = 100
            y -= fontSize * 2
    print()

def draw_line(point1, point2, penSize = 7):
    oldSize = pen()["pensize"]
    pensize(penSize)
    penup()
    goto(point1[0], point1[1])
    pendown()
    goto(point2[0], point2[1])
    penup()
    pensize(oldSize)


def draw_circle(point1, radius, penSize = 7):
    oldSize = pen()["pensize"]
    pensize(penSize)
    penup()
    goto(point1[0], point1[1])
    pendown()
    circle(-radius)
    penup()
    goto(point1[0], point1[1]-radius * 2)
    pensize(oldSize)


def get_letter_on_click(x,y):
    print(pen())
    for key, value in alphabetDict.items():
        charX = value[0]
        charY = value[1]
        if abs(charX - x) < 50 and 0 <= (y - charY) < 100:
            # print(key)
            check_letter(key)
            coord = alphabetDict.pop(key)
            draw_letter(coord, key, 40, "lightgrey")
            break

def check_letter(letter):
    global countCorrectLetter
    global numError
    lettersNums = []
    for x in range(len(secret)):
        if secret[x] == letter:
            lettersNums.append(x)
    if lettersNums:
        for index in lettersNums:
            countCorrectLetter += 1
            draw_letter(secretCoords[index], letter.upper(), 60)
    else:
        numError += 1
        draw_error(numError)

Screen().setup(1000, 800)

alphabetDict = {}
secretCoords = []
numError = 0
countCorrectLetter = 0
secret = "hangman"
shape("classic")
showturtle()

pensize(5)
speed(0)

draw_secret(secret)
draw_alphabet()
onscreenclick(get_letter_on_click)



mainloop()
import random
import sys
from turtle import *


def end_screen(text, color):
    global alphabetDict, buttonsDict
    buttonsDict = {
        "YES": (200, -250),
        "NO": (-200, -250)
    }
    alphabetDict.clear()
    clear()
    draw_letter((0, 250), text, 50)
    draw_letter((0, 150), "word was:", 30)
    draw_letter((0, 100), secret, 30, color)
    draw_letter((0, -100), "RESTART?", 60, )
    draw_letter(buttonsDict["YES"], "YES", 60, "green")
    draw_letter(buttonsDict["NO"], "NO", 60, "red")


def draw_square(topleftpoint, lenedge):
    x = topleftpoint[0]
    y = topleftpoint[1]
    size = 5
    points = [
        [x, y],
        [x + lenedge, y],
        [x + lenedge, y - lenedge],
        [x, y - lenedge]
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
            end_screen("GAME OVER", "red")


words = ['alligator', 'pizza', 'pie', 'gusenitsa', 'ronaldo', 'alabama', 'rizz', 'sigma', 'metal pipe', 'messi',
         'mbappe', 'cactus', 'takis', 'chess', 'beetlejuice', 'coldpalmer', 'realmadrid', 'mrbeast', 'nickeh30',
         'goose', 'cheburashka', 'tyson', 'greenfn', 'peter', 'benzema', 'sunshine', 'lightbulb', 'Alarm', 'Charger',
         'Origami', 'Pulse', 'Sport', 'Robe', 'Maneuver', 'Matrix', 'Splinter', 'Bubble', 'Composer', 'Joke', 'Toffee',
         'Bacterium', 'Dumplings', 'Pass', 'Certificate', 'Graduate', 'Expressions', 'rolling pin', 'Reaction', 'Reed',
         'Bottom', 'Assistant', 'Experience', 'Atmosphere', 'Butt', 'Package', 'Scientist', 'Pressure', 'Consistency',
         'Illuminations', 'Spinning', 'Treasure hunter', 'Badger', 'Rally', 'Fan', 'Dispenser', 'Flash drive',
         'Docking', 'Bath', 'Cache', 'Uniqueness', 'Device', 'Flash', 'Operator', 'Goalkeeper', 'Simulation',
         'Duplicate', 'Dandruff', 'Karma', 'Panacea', 'Limit', 'Increase', 'Parrot', 'plunger', 'Servant', 'Gardener',
         'Liquid', 'Mail', 'Dancer', 'Commander', 'Alley', 'Cookie', 'Chihuahua', 'Sloth', 'Chinchilla', 'Volunteer',
         'Welder', 'Drawing', 'Greetings', 'Jedi', 'Moss', 'Epiphany', 'Capture', 'Carapace', 'Climbing',
         'Turbulence', 'Rose', 'Slime']


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


def draw_letter(coord, char, fontSize, fontColor="black"):
    goto(coord)

    oldColor = pen()["pencolor"]
    oldFillColor = pen()["fillcolor"]

    pencolor(fontColor)
    fillcolor(oldFillColor)
    write(char, align='center', font=("Comic Sans MS", fontSize, "bold"))

    pencolor(oldColor)
    pencolor(oldFillColor)


def draw_alphabet():
    global alphabetDict, wait
    wait = True
    alphabet = (
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w',
        'x', 'y', 'z')
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
    wait = False


def draw_line(point1, point2, penSize=7):
    oldSize = pen()["pensize"]
    pensize(penSize)
    penup()
    goto(point1[0], point1[1])
    pendown()
    goto(point2[0], point2[1])
    penup()
    pensize(oldSize)


def draw_circle(point1, radius, penSize=7):
    oldSize = pen()["pensize"]
    pensize(penSize)
    penup()
    goto(point1[0], point1[1])
    pendown()
    circle(-radius)
    penup()
    goto(point1[0], point1[1] - radius * 2)
    pensize(oldSize)


def get_letter_on_click(x, y):
    for key, value in alphabetDict.items():
        charX = value[0]
        charY = value[1]
        if abs(charX - x) < 50 and 0 <= (y - charY) < 100:
            coord = alphabetDict.pop(key)
            draw_letter(coord, key, 40, "lightgrey")
            check_letter(key)
            break
    for key, value in buttonsDict.items():
        charX = value[0]
        charY = value[1]
        if abs(charX - x) < 90 and 0 <= (y - charY) < 100:
            if key == "YES":
                start_game()
            else:
                sys.exit()
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
        if countCorrectLetter == len(secret):
            end_screen("YOU WIN", 'green')
    else:
        numError += 1
        draw_error(numError)


Screen().setup(1000, 800)


def start_game():
    global alphabetDict, buttonsDict, secretCoords, numError, countCorrectLetter, secret, wait
    clear()
    alphabetDict = {}
    buttonsDict = {}
    secretCoords = []
    numError = 0
    countCorrectLetter = 0
    secret = random.choice(words).lower()
    wait = False
    hideturtle()

    pensize(5)
    speed(0)

    draw_secret(secret)
    draw_alphabet()


alphabetDict = {}
buttonsDict = {}
secretCoords = []
numError = 0
countCorrectLetter = 0
secret = ""
wait = False

start_game()

if not wait:
    onscreenclick(get_letter_on_click)

mainloop()

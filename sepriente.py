import random
from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0) 
snake = [vector(10, 0)]
aim = vector(0, -10)
cb = random.choice(["black", "green", "blue", "magenta", "cyan"])

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)
    
    
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)
        rn=randrange(7)
        if rn == 0 and food.x <= 190:
            food.x == food.x +10
            food.y = food.y
        if rn ==1 and food.x <= 190 and food.y <= 190:
            food.x == food.x +10
            food.y = food.y + 10
        if rn == 2 and food.x >= -190 and food.y <= 190:
            food.x == food.x -10
            food.y = food.y + 10
        if rn == 3 and food.x >= -190:
            food.x == food.x - 10
            food.y = food.y
        if rn == 4 and food.y <= 190:
            food.x == food.x 
            food.y = food.y + 10
        if rn == 5 and food.x >= -190 and food.y >= -190:
            food.x == food.x - 10
            food.y = food.y - 10
        if rn == 6 and food.y >= -190:
            food.x == food.x
            food.y = food.y -10
        if rn == 7 and food.x <= 190 and food.y >= -190:
            food.x == food.x +10
            food.y == food.y -10

    clear()

    for body in snake:
        
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
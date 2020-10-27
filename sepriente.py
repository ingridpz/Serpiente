# Llamar funciones necesarias para el código
from turtle import *
from random import randrange, choice
from freegames import square, vector

# Definir la serpiente y comida como vectores de cierta longitud
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
# Función que elije el color del cuerpo de la serpiente
cb = choice(["black", "green", "blue", "magenta", "cyan"])
# Función que elije el color de la comida (diferente serpiente usando if's)
if  cb == 'black':
    cc = choice(["green", "blue", "magenta", "cyan"])
elif  cb == 'green':
    cc = choice(["black", "blue", "magenta", "cyan"])
elif  cb == 'blue':
    cc = choice(["black", "green", "magenta", "cyan"])
elif  cb == 'magenta':
    cc = choice(["black", "blue", "green", "cyan"])
else:
    cc = choice(["black", "blue", "green", "magenta"])

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

# Condición que termina el juego en caso de comerse a sí mismo
# Es decir, que la serpiente retroceda por donde viene
def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
    #Verificar que la serpiente no se choque o se salga de la ventana
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        #posición nueva de la comida
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)
        #Movimiento aleatorio de la comida
        #Verificar que la comida no se salga de la ventana
        rn=randrange(7)
        if rn == 0 and food.x <= 180:
            #Movimiento a la derecha
            food.x == food.x +10
            food.y = food.y
        if rn ==1 and food.x <= 180 and food.y <= 180:
            #Movimiento en digonal
            food.x == food.x +10
            food.y = food.y + 10
        if rn == 2 and food.x >= -180 and food.y <= 180:
            #Movimiento en diagonal
            food.x == food.x -10
            food.y = food.y + 10
        if rn == 3 and food.x >= -180:
            #Movimiento a la izquierda
            food.x == food.x - 10
            food.y = food.y
        if rn == 4 and food.y <= 180:
            #Movimiento hacia arriba
            food.x == food.x 
            food.y = food.y + 10
        if rn == 5 and food.x >= -180 and food.y >= -180:
            #Movimiento en diagonal
            food.x == food.x - 10
            food.y = food.y - 10
        if rn == 6 and food.y >= -180:
            #Movimiento hacia abajo
            food.x == food.x
            food.y = food.y -10
        if rn == 7 and food.x <= 180 and food.y >= -180:
            #Movimiento en diagonal
            food.x == food.x +10
            food.y == food.y -10 

    clear()

    for body in snake:
        square(body.x, body.y, 9, cb)

    square(food.x, food.y, 9, cc)
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
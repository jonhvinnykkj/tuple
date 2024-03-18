import turtle

# Configuração inicial
screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.title("Minha Casa")

# Função para desenhar um retângulo
def draw_rectangle(turtle_obj, width, height, color):
    turtle_obj.begin_fill()
    turtle_obj.fillcolor(color)
    for _ in range(2):
        turtle_obj.forward(width)
        turtle_obj.left(90)
        turtle_obj.forward(height)
        turtle_obj.left(90)
    turtle_obj.end_fill()

# Função para desenhar um triângulo
def draw_triangle(turtle_obj, length, color):
    turtle_obj.begin_fill()
    turtle_obj.fillcolor(color)
    for _ in range(3):
        turtle_obj.forward(length)
        turtle_obj.left(120)
    turtle_obj.end_fill()

# Desenhar o telhado
roof_turtle = turtle.Turtle()
roof_turtle.penup()
roof_turtle.goto(-100, 100)
roof_turtle.pendown()
draw_triangle(roof_turtle, 200, "red")

# Desenhar as paredes
walls_turtle = turtle.Turtle()
walls_turtle.penup()
walls_turtle.goto(-100, -100)
walls_turtle.pendown()
draw_rectangle(walls_turtle, 200, 200, "yellow")

# Adicionar porta
door_turtle = turtle.Turtle()
door_turtle.penup()
door_turtle.goto(-30, -100)
door_turtle.pendown()
draw_rectangle(door_turtle, 60, 100, "brown")

# Adicionar maçaneta da porta
knob_turtle = turtle.Turtle()
knob_turtle.penup()
knob_turtle.goto(15, -100)
knob_turtle.pendown()
knob_turtle.dot(10, "black")

# Desenhar o jardim
garden_turtle = turtle.Turtle()
garden_turtle.penup()
garden_turtle.goto(-200, -200)  # Posição ajustada para o fundo da casa
garden_turtle.pendown()
garden_turtle.begin_fill()
garden_turtle.fillcolor("green")
draw_rectangle(garden_turtle, 500, 100, "green")  # Aumentei a largura do jardim
garden_turtle.end_fill()

# Adicionar flores no jardim
flower_turtle = turtle.Turtle()
flower_turtle.penup()
flower_turtle.goto(-170, -180)  # Posições ajustadas para o fundo da casa
flower_turtle.pendown()
flower_turtle.dot(20, "red")
flower_turtle.penup()
flower_turtle.goto(-140, -170)
flower_turtle.pendown()
flower_turtle.dot(20, "yellow")
flower_turtle.penup()
flower_turtle.goto(-110, -180)
flower_turtle.pendown()
flower_turtle.dot(20, "purple")

# Adicionar árvore no canto direito do jardim
tree_turtle = turtle.Turtle()
tree_turtle.penup()
tree_turtle.goto(175, -150)
tree_turtle.pendown()
tree_turtle.begin_fill()
tree_turtle.fillcolor("brown")
draw_rectangle(tree_turtle, 20, 50, "brown")
tree_turtle.end_fill()
tree_turtle.penup()
tree_turtle.goto(175, -100)
tree_turtle.pendown()
tree_turtle.begin_fill()
tree_turtle.fillcolor("green")
tree_turtle.circle(30)
tree_turtle.end_fill()
tree_turtle.penup()
tree_turtle.goto(200, -70)
tree_turtle.pendown()
tree_turtle.begin_fill()
tree_turtle.fillcolor("green")
tree_turtle.circle(25)
tree_turtle.end_fill()

# Adicionar terceira bola (folha) abaixo da menor
tree_turtle.penup()
tree_turtle.goto(200, -100)
tree_turtle.pendown()
tree_turtle.begin_fill()
tree_turtle.fillcolor("green")
tree_turtle.circle(25)
tree_turtle.end_fill()

# Ocultar tartarugas
roof_turtle.hideturtle()
walls_turtle.hideturtle()
door_turtle.hideturtle()
knob_turtle.hideturtle()
garden_turtle.hideturtle()
flower_turtle.hideturtle()
tree_turtle.hideturtle()

# Finalizar
screen.mainloop()

import turtle

# Configurações iniciais
t = turtle.Turtle()

# Desenhar o telhado
t.fillcolor("red")
t.begin_fill()
t.goto(0, 100)
t.goto(-100, 0)
t.goto(100, 0)
t.goto(0, 100)
t.end_fill()

# Desenhar as paredes
t.fillcolor("yellow")
t.begin_fill()
t.goto(-100, 0)
t.goto(-100, -100)
t.goto(100, -100)
t.goto(100, 0)
t.goto(-100, 0)
t.end_fill()

# Desenhar a porta
t.penup()
t.goto(-30, -100)
t.pendown()
t.color("brown")
t.goto(-30, -60)
t.right(90)
t.forward(20)
t.right(90)
t.forward(40)
t.right(90)
t.forward(20)

# Desenhar a janela
t.penup()
t.goto(30, -80)
t.pendown()
t.color("blue")
t.goto(30, -60)
t.right(90)
t.forward(20)
t.right(90)
t.forward(20)
t.right(90)
t.forward(20)

# Desenhar o sol
t.penup()
t.goto(-80, 80)
t.pendown()
t.color("yellow")
t.begin_fill()
t.circle(30)
t.end_fill()

# Desenhar a grama
t.penup()
t.goto(-100, -100)
t.pendown()
t.color("green")
t.begin_fill()
t.goto(-100, -200)
t.goto(100, -200)
t.goto(100, -100)
t.goto(-100, -100)
t.end_fill()

# Esconder a tartaruga
t.hideturtle()

# Finalizar
turtle.done()
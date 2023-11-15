import turtle


# This function draws one petal
def draw_petal():
    turtle.pendown()
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(30)
    turtle.right(135)
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(30)
    turtle.right(135)
    turtle.penup()

# this function uses draw_patel and draws a flower by itself
def draw_flower():
    turtle.left(45)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(135)
    turtle.pendown()
    turtle.forward(150)
    turtle.penup()

# this function uses draw_flower and advances by itself
def draw_flower_and_advance():
    draw_flower()
    turtle.right(90)
    turtle.penup()
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(150)
    turtle.left(90)
    turtle.pendown()

# this function uses draw_flower_and_advance and draws bed by itself
def draw_flower_bed():
    turtle.penup()
    turtle.forward(200)
    turtle.left(180)
    turtle.pendown()
    draw_flower_and_advance()
    draw_flower_and_advance()
    draw_flower_and_advance()

# The main program
if __name__ == "__main__":
    draw_flower_bed()
    turtle.done()







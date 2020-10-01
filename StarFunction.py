import turtle

star = turtle.Turtle()
star.color("pink")

star2 = turtle.Turtle()
star2.color("blue")

SIDES = 5   # number of sides on a star, a constant

#-------------------------------------------------

def draw_star(the_turtle):
    the_turtle.penup()
    the_turtle.forward(350)
    the_turtle.pendown()
    the_turtle.right(144)
    the_turtle.begin_fill()
    for i in range(SIDES):
        the_turtle.forward(100)
        the_turtle.right(180 - 180/SIDES)     # caclulate the turn angle
    the_turtle.end_fill()

#--------------------------------------------------
        
def main():
    star = turtle.Turtle()
    star.color("pink")
    window = turtle.Screen()
    window.bgcolor("lightgreen")
    star.penup()
    star.goto(-175, 0)
    star.pendown()

    for i in range(5):
        draw_star(star)

#--------------------------------------------------

main()

##draw_star(star, 0 , 200)
##draw_star(star2, 0, 0)

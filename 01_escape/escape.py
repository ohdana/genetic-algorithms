import turtle
import argparse
import inspect

def escaped(position):
    x = int(position[0])
    y = int(position[1])

    return x < -35 or x > 35 or y < -35 or y > 35

def draw_line():
    angle = 0
    step = 5
    t = turtle.Turtle()

    while not escaped(t.position()):
        t.left(angle)
        t.forward(step)

def draw_bag():
    turtle.shape('turtle')
    turtle.pen(pencolor='brown', pensize=5)
    turtle.penup()
    turtle.goto(-35, 35)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(70)
    turtle.left(90)
    turtle.forward(70)
    turtle.left(90)
    turtle.forward(70)

if __name__ == '__main__':
    fns = { "line": draw_line }
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--function",
        choices = fns,
        help = "One of " + ', '.join(fns.keys()))
    parser.add_argument("-n", "--number", default=50, type=int, help="How many?")
    args = parser.parse_args()

    try:
        f = fns[args.function]
        turtle.setworldcoordinates(-70., -70., 70., 70.)
        draw_bag()
        turtle.hideturtle()
        if len(inspect.getfullargspec(f).args) == 1:
            f(args.number)
        else:
            f()
        turtle.mainloop()
    except KeyError:
        parser.print_help()

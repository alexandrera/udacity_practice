import os
import turtle


def draw_square_circle_and_triangle():
    window = turtle.Screen()
    window.bgcolor("black")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("white")
    brad.speed(2)

    count = 0
    while count < 4:
        count += 1
        brad.forward(100)
        brad.right(90)

    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("yellow")
    angie.circle(100)

    felix = turtle.Turtle()
    felix.shape("turtle")
    felix.color("blue")

    number = 0
    while number < 3:
        number += 1
        felix.forward(100)
        felix.right(120)

    window.exitonclick()


draw_square_circle_and_triangle()

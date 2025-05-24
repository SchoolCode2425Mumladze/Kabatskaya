import turtle
import lab_buttons
import draw_lab

screen = turtle.Screen()
screen.title("Лабиринт")

lab_buttons.paint_tbleft()
lab_buttons.paint_tbright()
lab_buttons.paint_tbup()
lab_buttons.paint_tbdown()
lab_buttons.click(screen, turtle)

draw_lab.drawing_lab_1()

turtle.penup()
turtle.speed(0)
turtle.goto(340, 114)
turtle.right(180)
turtle.shape("square")
turtle.color("orange")

turtle.done()

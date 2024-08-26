import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Python Turtle")

turtle_instance = turtle.Turtle()
#turtle_instance.speed(50)

def turtle_forward():
    turtle_instance.forward(30)

def rotate_angle_right():
    turtle_instance.setheading(turtle_instance.heading()-10)
   # turtle_instance.right(10)

def rotate_angle_left():
    turtle_instance.setheading(turtle_instance.heading() +10)
  #  turtle_instance.left(10)

def clear_screen():
    turtle_instance.clear()

def turtle_instance_home():
    turtle_instance_pen_up()
    turtle_instance.home()
    turtle_instance_pen_down()

def turtle_instance_pen_up():
    turtle_instance.penup()

def turtle_instance_pen_down():
    turtle_instance.pendown()

drawing_board.listen()
drawing_board.onkey(fun=turtle_forward, key="w")
drawing_board.onkey(fun=rotate_angle_left, key="a")
drawing_board.onkey(fun=rotate_angle_right, key="d")
drawing_board.onkey(fun=turtle_instance.clear, key="c")
drawing_board.onkey(fun=turtle_instance_home, key="h")

turtle.mainloop()
import turtle


class Paddle:
    dy = 20

    def __init__(self, position):
        self.paddle = turtle.Turtle()
        self.paddle.speed(0)
        self.paddle.goto(position[0], position[1])
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.penup()

    def move_up(self):
        self.paddle.sety(self.paddle.ycor() + self.dy)

    def move_down(self):
        self.paddle.sety(self.paddle.ycor() - self.dy)

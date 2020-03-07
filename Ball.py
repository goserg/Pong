import turtle


class Ball:
    dx = 5
    dy = 5

    def __init__(self, score_board):
        self.ball = turtle.Turtle()
        self.ball.speed(0)
        self.ball.shape("square")
        self.ball.color("white")
        self.ball.penup()
        self.score_board = score_board

    def move(self):
        self.ball.setx(self.ball.xcor() + self.dx)
        self.ball.sety(self.ball.ycor() + self.dy)

    def border_check(self):
        if self.ball.ycor() > 290:
            self.ball.sety(290)
            self.dy = -self.dy

        if self.ball.ycor() < -290:
            self.ball.sety(-290)
            self.dy = -self.dy

        if self.ball.xcor() < -390:
            self.ball.goto(0, 0)
            self.dx *= -1
            self.score_board.update(0, 1)

        if self.ball.xcor() > 390:
            self.ball.goto(0, 0)
            self.dx *= -1
            self.score_board.update(1, 0)

    def paddle_check(self, paddle):
        if paddle.paddle.ycor() + 60 > self.ball.ycor() > paddle.paddle.ycor() - 60:
            if self.dx > 0 and paddle.paddle.xcor() - 20 < self.ball.xcor() < paddle.paddle.xcor():
                self.ball.setx(paddle.paddle.xcor() - 20)
                self.dx *= -1
            elif self.dx < 0 and paddle.paddle.xcor() < self.ball.xcor() < paddle.paddle.xcor() + 20:
                self.ball.setx(paddle.paddle.xcor() + 20)
                self.dx *= -1

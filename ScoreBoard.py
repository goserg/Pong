import turtle


class ScoreBoard:
    score_a = 0
    score_b = 0

    def __init__(self):
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(0, 260)
        self.pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

    def update(self, score_a, score_b):
        self.score_a += score_a
        self.score_b += score_b
        self.pen.clear()
        self.pen.write("Player A: {}  Player B: {}".format(self.score_a, self.score_b),
                       align="center", font=("Courier", 24, "normal"))

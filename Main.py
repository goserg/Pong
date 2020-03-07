from Paddle import Paddle
from Ball import Ball
from ScoreBoard import ScoreBoard
import turtle

screen_width = 800
screen_height = 600

window = turtle.Screen()
window.title("Serg's pong learning project")
window.bgcolor("black")
window.setup(width=screen_width, height=screen_height)
window.tracer()

left_paddle = Paddle((-screen_width/2+30, 0))
right_paddle = Paddle((screen_width/2-30, 0))
score_board = ScoreBoard()
ball = Ball(score_board)


# Keyboard binding
window.listen()
window.onkeypress(left_paddle.move_up, "w")
window.onkeypress(left_paddle.move_down, "s")
window.onkeypress(right_paddle.move_up, "Up")
window.onkeypress(right_paddle.move_down, "Down")

# Main loop
while True:
    window.update()

    ball.move()
    ball.border_check()
    ball.paddle_check(left_paddle)
    ball.paddle_check(right_paddle)

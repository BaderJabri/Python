
import turtle
import time
from pygame import mixer

mixer.init()
PaddleBounce = mixer.Sound("PongPaddleBounce.wav")
WallBounce = mixer.Sound("PongWallBounce.wav")
PongScore = mixer.Sound("PongScore.wav")
Won = mixer.Sound("ArcadeWinning.wav")


wn = turtle.Screen()
wn.title("Pong Game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)


player_a = 0
player_b = 0

pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(-400, 260)
pen.pendown()
pen.goto(400, 260)
pen.penup()
pen.goto(-400, -280)
pen.pendown()
pen.goto(400, -280)
pen.penup()
pen.goto(0, 255)
pen.pendown()
pen.write("PONG!", font=("Courier", 30), align="Center")

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-370,0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(370,0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = .3
ball.dy = -.3

text_a = turtle.Turtle()
text_a.speed(0)
text_a.color("white")
text_a.hideturtle()
text_a.penup()
text_a.goto(-370, 260)
text_a.write("Player A: {}".format(player_a), font=("Courier", 15), align="Left")

text_b = turtle.Turtle()
text_b.speed(0)
text_b.color("white")
text_b.hideturtle()
text_b.penup()
text_b.goto(370, 260)
text_b.write("Player B: {}".format(player_b), font=("Courier", 15), align="Right")


def paddle_a_up():
    if (paddle_a.ycor() != 200):
        y = paddle_a.ycor()
        y += 20
        paddle_a.sety(y)
    
def paddle_a_down():
    if (paddle_a.ycor() != -220):
        y = paddle_a.ycor()
        y -= 20
        paddle_a.sety(y)
    
def paddle_b_up():
    if (paddle_b.ycor() != 200):
        y = paddle_b.ycor()
        y += 20
        paddle_b.sety(y)
    
def paddle_b_down():
    if (paddle_b.ycor() != -220):
        y = paddle_b.ycor()
        y -= 20
        paddle_b.sety(y)



#keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


#main game
while True:
    wn.update()
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # Border checking
    if ball.ycor() > 250:
        mixer.Sound.play(WallBounce)
        ball.dy *= -1
    if ball.ycor() < -270:
        mixer.Sound.play(WallBounce)
        ball.dy *= -1
        
    if ball.xcor() > 380:
        mixer.Sound.play(PongScore)
        ball.goto(0,0)
        time.sleep(.1)
        ball.dx *= -1
        player_a += 1
        text_a.clear()
        text_a.write("Player A: {}".format(player_a), font=("Courier", 15), align="Left")
        if (player_a == 2):
            won = turtle.Turtle()
            won.penup()
            won.color("White")
            won.speed(0)
            won.hideturtle()
            won.write("Player A WON!", font= ("Arial", 50), align = "Center")
            time.sleep(.25)
            mixer.Sound.play(Won)
            time.sleep(2.5)
            break
        
    if ball.xcor() < -380:
        mixer.Sound.play(PongScore)
        ball.goto(0,0)
        time.sleep(.3)
        ball.dx *= -1
        player_b += 1
        text_b.clear()
        text_b.write("Player B: {}".format(player_b), font=("Courier", 15), align="Right")
        if (player_b == 10):
            won = turtle.Turtle()
            won.penup()
            won.color("White")
            won.speed(0)
            won.hideturtle()
            time.sleep(.25)
            won.write("Player B WON!", font= ("Arial", 50), align = "Center")
            mixer.Sound.play(Won)
            time.sleep(2.5)
            break
        
    
    # Paddle and ball collisions
    if ball.xcor() < -340 and (ball.ycor() > paddle_a.ycor() -50 and ball.ycor() < paddle_a.ycor() + 50):
        mixer.Sound.play(PaddleBounce)
        ball.setx(-340)
        ball.dx *= -1
        
    if ball.xcor() > 340 and (ball.ycor() > paddle_b.ycor() - 50 and ball.ycor() < paddle_b.ycor() + 50):
        mixer.Sound.play(PaddleBounce)
        ball.setx(340)
        ball.dx *= -1
import turtle as tl

class PONG:
    def __init__(self):
        self.create_window()
        self.leftpaddle()
        self.rightpaddle()
        self.create_ball()
        self.keys()
        self.game()

    def create_window(self):
        self.root = tl.Screen()
        self.root.title('THE PONG GAME')
        self.root.bgcolor('black')
        self.root.setup(width=800, height=500)
        self.root.tracer(0)

    def leftpaddle(self):
        self.left_paddle = tl.Turtle()
        self.left_paddle.speed(0)
        self.left_paddle.shape("square")
        self.left_paddle.color("red")
        self.left_paddle.shapesize(stretch_wid=7, stretch_len=1)
        self.left_paddle.penup()
        self.left_paddle.goto(-390, 0)

    def rightpaddle(self):
        self.right_paddle = tl.Turtle()
        self.right_paddle.speed(0)
        self.right_paddle.shape('square')
        self.right_paddle.color('blue')
        self.right_paddle.shapesize(stretch_wid=7, stretch_len=1)
        self.right_paddle.penup()
        self.right_paddle.goto(380, 0)

    def left_paddle_up(self):
        y = self.left_paddle.ycor()
        y = y + 25
        self.left_paddle.sety(y)

    def left_paddle_down(self):
        y = self.left_paddle.ycor()
        y = y - 25
        self.left_paddle.sety(y)

    
    def right_paddle_up(self):
        y = self.right_paddle.ycor()
        y = y + 25
        self.right_paddle.sety(y)

    def right_paddle_down(self):
        y = self.right_paddle.ycor()
        y = y - 25
        self.right_paddle.sety(y)

    def create_ball(self):
        self.ball = tl.Turtle()
        self.ball.speed(0)
        self.ball.shape('circle')
        self.ball.color('yellow')
        self.ball.penup()
        self.ball.goto(0,0)
        self.ball_direction_x = 0.3
        self.ball_direction_y = 0.3

    def keys(self):
        self.root.listen()
        self.root.onkeypress(self.left_paddle_up, 'w')
        self.root.onkeypress(self.left_paddle_down, 's')
        
        self.root.onkeypress(self.right_paddle_up, 'Up')
        self.root.onkeypress(self.right_paddle_down, 'Down')
        

    def game(self):
        while True:
            self.root.update()

            self.ball.setx(self.ball.xcor() + self.ball_direction_x)
            self.ball.sety(self.ball.ycor() + self.ball_direction_y)

            # Move the ball
            if self.ball.ycor() > 240:
                self.ball.sety(240)
                self.ball_direction_y *= -1
            
            if self.ball.ycor() < -240:
                self.ball.sety(-240)
                self.ball_direction_y *= -1

            if self.ball.xcor() > 390:
                self.ball.setx(390)
                self.ball_direction_x *= -1
            
            if self.ball.xcor() < -390:
                self.ball.setx(-390)
                self.ball_direction_x *= -1


            #Collission detection with paddles
            if (380 > self.ball.xcor() > 360) and (self.right_paddle.ycor() + 70 > self.ball.ycor() > self.right_paddle.ycor() - 70):
                self.ball.setx(360)
                self.ball_direction_x *= -1

            if (-390 < self.ball.xcor() < -370) and (self.left_paddle.ycor() + 70 > self.ball.ycor() > self.left_paddle.ycor() - 70):
                self.ball.setx(-370)
                self.ball_direction_x *= -1

            
            


def main():
    PONG()

if __name__ == '__main__':
    main()
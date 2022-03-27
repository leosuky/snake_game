from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,265)
        self.score = 0
        self.write(f"Score: {self.score}", align="center", font=("Courier", 24, "normal"))


    def increment(self):
        self.score +=1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Courier", 24, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Courier", 24, "bold"))

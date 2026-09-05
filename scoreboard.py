from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.score = 0
        with open("data.txt","r") as f:

            self.high_score = int(f.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score :{self.score} High Score :{self.high_score}", align="center", font=("Courier", 24, "normal"))

    def reset_score(self):
        if self.score >self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as f:
                f.write(str(self.score))
        self.score = 0
        self.update_scoreboard()


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over", align="center", font=("Courier", 24, "normal"))
from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 15, 'normal')
class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0,270)
        with open("data.txt", "r") as file:
            self.high_score = int(file.read())
        self.score = 0
        self.write(f"Score: {self.score} High Score: {self.high_score}",align="center", font= ('Courier', 15, 'normal'))
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}",align="center", font= FONT)


    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align=ALIGNMENT, font= FONT)

    def reset(self):
        if self.score > self.high_score:
           self.high_score = self.score
           with open("data.txt","w") as file:
            file.write(str(self.high_score))
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()


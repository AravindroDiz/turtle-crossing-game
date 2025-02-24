from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 1
        self.goto(-280,250)
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.write(f'LEVEL: {self.score}',align="left",font=FONT)
    
    def increase_level(self):
        self.score += 1
        self.update_scoreboard()


    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align='center',font=("Arial",20,'bold'))
        
        



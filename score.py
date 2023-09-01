from turtle import Turtle
points = 'center'
Font1 = ('Courier', 15, 'bold')
Font2 = ('Arial', 80, 'bold')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('brown')
        self.penup()
        self.goto(-540, -390)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f'Score : {self.score}', align=points, font=Font1)

    def game_over(self):
        self.goto(0, 0)
        self.write('Game Over !', align=points, font=Font2)



    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()



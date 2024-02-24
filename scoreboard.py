from food import Food


class Scoreboard(Food):

    def __init__(self):
        super().__init__()
        points = 0
        self.points = points
        self.teleport(-70, 230)
        self.color("white")
        self.shapesize(stretch_len=0.01, stretch_wid=0.01)
        self.write("Score = ", True, align="center", font=('Arial', 25, 'normal'))

    def game_over(self):
        self.teleport(0, 0)
        self.write("Game Over", True, align="center", font=('Arial', 30, 'normal'))

    def track_score(self):
        self.points += 1
        self.clear()
        self.write(f"Score = {self.points}", False, align="center", font=('Arial', 25, 'normal'))





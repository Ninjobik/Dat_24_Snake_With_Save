from turtle import Turtle


class Score:
    def __init__(self):
        self.points = 0
        self.address = "/Users/ninjobik/downloads/"
        self.highscore = self.load_score()
        self.scores = Turtle()
        self.scores.setposition(-220, 230)
        self.scores.color("white")
        self.scores.hideturtle()
        self.scores.penup()
        self.update_score()

    def update_score(self):
        self.scores.clear()
        if self.points > self.highscore:
            self.highscore = self.points
        self.scores.write(f"Score: {self.points}. Highscore: {self.highscore}", False, "left", ("Ariel", 14, "normal"))

    def add_point(self):
        self.points += 1
        self.update_score()

    def restart_game(self):
        with open(f"{self.address}data.txt", "w") as file:
            file.write(str(self.highscore))
        self.points = 0
        self.update_score()

    def load_score(self):
        with open(f"{self.address}data.txt") as file:
            return int(file.read())

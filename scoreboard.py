
class Scoreboard:

    def __init__(self, name) -> None:
        self.name = name
        self.score = 0
        self.high_score = 0

    def update_score(self):
        self.score += 1

    def save_score(self):
        pass

    def top_5(self, file):
        pass

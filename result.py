class Result:
    def __init__(self, row):
        self.Date = row[0]

        self.Balls = []
        for b in row[1:8]:
            self.Balls.append(b)

    def get_date(self):
        return self.Date

    def get_balls6(self):
        return self.Balls[0:6]

    def get_balls7(self):
        return self.Balls[0:7]

    def get_powerball(self):
        return self.Balls[6]


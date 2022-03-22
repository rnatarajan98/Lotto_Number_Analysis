class Result:
    def __init__(self, row):
        self.Date = row[0]

        self.Balls = []
        for b in row[1:8]:
            self.Balls.append(int(b))

    def get_date(self):
        return self.Date

    def get_ball(self, index):
        if index >= 0 and index <= 6:
            return self.Balls[index]
        else:
            return None

    def get_balls6(self):
        return self.Balls[0:6]

    def get_balls7(self):
        return self.Balls[0:7]

    def get_powerball(self):
        return self.Balls[6]

    def as_dict(self):
        return {'Date': self.Date, 'Ball1': self.Balls[0], 'Ball2': self.Balls[1], 'Ball3': self.Balls[2], 'Ball4': self.Balls[3], 'Ball5': self.Balls[4], 'Ball6': self.Balls[5], 'Ball7': self.Balls[6]}
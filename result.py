class Result:
    def __init__(self, row):
        self.Date = row[0]

        self.Balls = []
        for b in row[1:8]:
            self.Balls.append(b)


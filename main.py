from result import Result
import csv

f = open('lotto_history.csv')
csv_reader = csv.reader(f)
next(csv_reader)                #Skip Title
for line in csv_reader:
    result = Result(line)
    print(line)
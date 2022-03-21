from result import Result
import csv

f = open('lotto_history.csv')
csv_reader = csv.reader(f)
next(csv_reader)                #Skip Title
data = []
for line in csv_reader:
    result = Result(line)
    results.append(result)


test_data = results[:279]
train_data = results[279:]


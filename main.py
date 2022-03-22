from result import Result
import csv
import pandas as pd
import matplotlib.pyplot as plt 

f = open('lotto_history.csv')
csv_reader = csv.reader(f)
next(csv_reader)                #Skip Title
data = []
for line in csv_reader:
    result = Result(line)
    data.append(result)

df = pd.DataFrame([x.as_dict() for x in data])
print(df)

titles = ['Ball1', 'Ball2', 'Ball3', 'Ball4', 'Ball5', 'Ball6', 'Ball7']

plt.figure(figsize=(18, 6), dpi=40)
for t in titles:
    plt.plot(df[t], label=t)
plt.legend()

plt.figure(figsize=(18, 6), dpi=40)
for i, t in enumerate(titles):
    ax = plt.subplot(1, 8, i+1)
    plt.hist(df[t])
    plt.ylim([0, 140])
    plt.xlim([0, 60])
    ax.set_xlabel(t)

plt.figure(figsize=(18, 6), dpi=40)
plt.hist(df[titles], 59 , density=False, histtype='bar', stacked=True)
plt.legend(titles)


plt.show()

plt.figure(figsize=(18, 12), dpi=40)

test_data = data[:279]
train_data = data[279:]


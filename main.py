from result import Result
import csv
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import seaborn as sns
import numpy as np

f = open('lotto_history.csv')
csv_reader = csv.reader(f)
next(csv_reader)  # Skip Title
data = []
for line in csv_reader:
    result = Result(line)
    data.append(result)

df = pd.DataFrame([x.as_dict() for x in data])
print(df)

titles = ['Ball1', 'Ball2', 'Ball3', 'Ball4', 'Ball5', 'Ball6', 'Ball7']
fig1 = plt.figure(constrained_layout=True, figsize=(18, 6), dpi=40)
gs = GridSpec(4, 7, figure=fig1)

ax1 = fig1.add_subplot(gs[0, :])
for t in titles:
    sns.scatterplot(data=df[t], ax=ax1, label=t, s=10)
    # ax1.plot(df[t], label=t)0

ax2 = fig1.add_subplot(gs[1, :])
sns.boxplot(data=df[titles], ax=ax2)

for i, t in enumerate(titles):
    ax = fig1.add_subplot(gs[2, i])
    sns.histplot(df[t], bins=59, discrete=True, ax=ax)
    ax.set_ylim([0, 65])
    ax.set_xlim([0, 60])
    ax.set_xlabel(t)

ax3 = fig1.add_subplot(gs[3, :])
# sns.histplot(df[titles], bins=59, discrete=True, ax=ax3, multiple="stack", stacked=True)
ax3.hist(df[titles], 59, density=False, histtype='bar', stacked=True)
plt.legend(titles)

fig2 = plt.figure(constrained_layout=True, figsize=(6, 6), dpi=40)
ax2_1 = fig2.add_subplot(111)
cv = np.zeros([7, 7])
for i, t1 in enumerate(titles):
    for j, t2 in enumerate(titles):
        cv[i, j] = np.corrcoef(df[t1], df[t2])[0, 1]
sns.heatmap(cv, xticklabels=[1, 2, 3, 4, 5, 6, 7], yticklabels=[1, 2, 3, 4, 5, 6, 7], ax=ax2_1,  annot=True)
ax2_1.set_aspect('equal')


fig3 = plt.figure(constrained_layout=True, figsize=(42, 42), dpi=40)
gs = GridSpec(7, 7, figure=fig3)
for i, t1 in enumerate(titles):
    for j, t2 in enumerate(titles):
        ax = fig3.add_subplot(gs[i, j])
        sns.scatterplot(data=df, x=t1, y=t2, ax=ax, s=10)










plt.show()

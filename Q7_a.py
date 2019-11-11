import csv
import statistics
import matplotlib.pyplot as plt
import numpy as np

data = []
with open('first_half_logs.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            data.append(row)
            line_count += 1
players = []
for i in range(16):
    players.append([])
for d in data:
    players[int(d[1])].append([float(d[2]),float(d[3])])

id_player = []
x_mean = []
y_mean = []
counter_player = 0
for p in players:
    if p:
        x_mean.append(statistics.mean(np.array(p)[:,0]))
        y_mean.append(statistics.mean(np.array(p)[:,1]))
        id_player.append(counter_player)
        counter_player += 1

print(x_mean)
print(y_mean)
print(id_player)
plt.xlim([0,105])
plt.ylim([0,75])
plt.scatter(x_mean, y_mean,c=id_player, s=40)
plt.show()

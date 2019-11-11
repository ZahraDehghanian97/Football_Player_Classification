import csv
import matplotlib.pyplot as plt
import statistics
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
    temp = [float(d[2]), float(d[3])]
    players[int(d[1])].append(temp)

mean = []
cov = []
number =[]


for player in players :
    if len(player) > 1:
        mean.append([statistics.mean(np.array(player)[:,0]),statistics.mean(np.array(player)[:,1])])
        number.append(player)
        cov.append(np.cov(np.array(player)[:,0],np.array(player)[:,1]))


counter =0
N_bins = 100
for player in range(len(mean)) :
    x, y = np.random.multivariate_normal(mean[player], cov[player], 5000).T
    # plt.figure(counter)
    plt.figure(figsize=(1, 2))
    plt.hist2d(x, y, bins=N_bins, normed=False, cmap='plasma')
    counter += 1

print(cov)
# Show the plot.
plt.show()
import csv
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
total = []
label = []
player = []
for i in range(16):
    total.append([52.5,68])
    label.append(i)
    player.append([[52.5,68]])
for d in data:
    temp = [float(d[2]), float(d[3])]
    player[int(d[1])].append(temp)
    total.append(temp)
    label.append(int(d[1]))

# print(total[1][0])
for i in range (16) :
    plt.figure(i)
    plt.xlim([-10, 120])
    plt.ylim([-10, 75])
    plt.scatter(np.array(player[i])[:,0],np.array(player[i])[:,1], s=2)
plt.show()

import pandas as pd
import json
import time
from datetime import datetime as d
import matplotlib.pylab as plt
import seaborn as sns
import pprint

file_path=['worker1.log','worker2.log','worker3.log']

counts = dict()
counts['random'] = [0, 0, 0]
counts['round-robin'] = [0, 0, 0]
counts['least-loaded'] = [0, 0, 0]

for path in file_path:
	file = open(path, "r")
	for line in file.readlines():
		temp = line.split(";")
		if (temp[1].split()[0] == 'Started'):
			counts[temp[2]][int(path[-5]) - 1] += 1

counts['workers'] = ['worker1', 'worker2', 'worker3']

new = pd.DataFrame.from_dict(counts)
new.set_index("workers", inplace = True)


plt.figure(figsize=(14,7))
plt.title("Number of tasks scheduled per worker, algorithm wise")
sns.heatmap(data=new, annot=True)
plt.xlabel("Algorithm")
plt.show()

from datetime import datetime
import statistics
import sys



#n = int(sys.argv[1]) #Number of worker

final_dict=dict()
final_dict['random']=list((0.0,0.0,0.0,0.0))
final_dict['round-robin']=list((0.0,0.0,0.0,0.0))
final_dict['least-loaded']=list((0.0,0.0,0.0,0.0))

tempList1=[]
tempList2=[]
tempList3=[]

file=open("master.log","r")
for line in file.readlines():
  temp=line.split(";")
  algo=temp[1]
  temp1=temp[2].split()
  if(temp1[1]=="task"):
    if(temp[1]=="random"):
    	tempList1.append(float(temp1[7]))
    elif(temp[1]=="round-robin"):
    	tempList2.append(float(temp1[7]))
    elif(temp[1]=='least-loaded'):
    	tempList3.append(float(temp1[7]))
file.close()
if (tempList1):
	final_dict['random'][0] = (float(sum(tempList1))/len(tempList1))
	final_dict['random'][1] = (statistics.median(tempList1))
if (tempList2):
	final_dict['round-robin'][0] = (float(sum(tempList2))/len(tempList2))
	final_dict['round-robin'][1] = (statistics.median(tempList2))
if (tempList3):
	final_dict['least-loaded'][0] = (float(sum(tempList3))/len(tempList3))
	final_dict['least-loaded'][1] = (statistics.median(tempList3))
'''
for i in range(1, n + 1):
	file = open("worker" + str(i) + ".log", "r")
	for line in file.readlines():
		temp = line.split(";")
		algo = temp[2]
		if (temp[1].split()[0] == "Started"):
			d[temp[1].split()[2]] = datetime.strptime(temp[3][:-2],'%Y-%m-%d %H:%M:%S,%f')
		else:
			time_elapsed = datetime.strptime(temp[3][:-2], '%Y-%m-%d %H:%M:%S,%f') - d[temp[1].split()[2]]
			if (algo == 'random'):
				tempList1.append(float(str(time_elapsed).split(":")[-1]))
			elif (algo == 'round-robin'):
				tempList2.append(float(str(time_elapsed).split(":")[-1]))
			else:
				tempList3.append(float(str(time_elapsed).split(":")[-1]))
	file.close()




if (tempList1):
	final_dict['random'][0] = (float(sum(tempList1))/len(tempList1))
	final_dict['random'][1] = (statistics.median(tempList1))
if (tempList2):
	final_dict['round-robin'][0] = (float(sum(tempList2))/len(tempList2))
	final_dict['round-robin'][1] = (statistics.median(tempList2))
if (tempList3):
	final_dict['least'][0] = (float(sum(tempList3))/len(tempList3))
	final_dict['least'][1] = (statistics.median(tempList3))


'''

#------------------------------------------------------------------------

start_times = dict()
end_times = dict()
algos = dict()
per_algos = dict()

file = open("master.log", "r")

lines = file.readlines()
file.close()

for line in lines:
	temp = line.split(";")
	a = temp[2].split()
	if (a[0] == 'Completed'):
		if (a[1] == 'task'):
			job_id = a[2][0]
			if (a[2][2] == 'R'):
				b = a[4] + " " + a[5]
				end_times[job_id] = datetime.strptime(b,'%Y-%m-%d %H:%M:%S.%f')
	elif (a[0] == 'Started'):
		job_id = a[-1]
		start_times[job_id] = datetime.strptime(temp[3][:-2],'%Y-%m-%d %H:%M:%S,%f')
		algos[job_id] = temp[1]


jobs = start_times.keys()
for job in start_times:
	if algos[job] not in per_algos:
		per_algos[algos[job]] = []
		per_algos[algos[job]].append((end_times[job] - start_times[job]).total_seconds())
	else:
		per_algos[algos[job]].append((end_times[job] - start_times[job]).total_seconds())

for algo in per_algos:
	# print(algo, float(sum(per_algos[algo]))/len(per_algos[algo]), statistics.median(per_algos[algo]))
	final_dict[algo][2] = float(sum(per_algos[algo]))/len(per_algos[algo])
	final_dict[algo][3] = statistics.median(per_algos[algo])



for i in final_dict:
	print(i,final_dict[i])


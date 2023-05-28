n = 5  
jobs = [['a', 2, 100],  
           ['b', 1, 19],
           ['c', 2, 27],
           ['d', 1, 25],
           ['e', 3, 15]]
sorter = lambda job: int(job[2])
jobs = sorted(jobs, key=sorter, reverse=True)
scheduled = []
time = 0
for i in jobs:
    deadline =int(i[1])
    jobId=i[0]
    if time <=deadline :
        scheduled.append(jobId)
        time += 1

print("Jobs are scheduled as:")
print(scheduled)
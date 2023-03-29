from heapq import heappush, heappop
q_jobs = []

jobs = [[1,7],[2,9],[3,4],[4,2]]

cur_time = 3

for item in jobs:
    start, time = item
    if start <=cur_time:
        heappush(q_jobs, ((cur_time + time - start), start, time))

print(q_jobs)


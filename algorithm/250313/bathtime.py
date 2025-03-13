time = [15, 30, 50, 10]
n = len(time)

total_time = 0
time.sort()
for i in range(n) :
    total_time += time[i] * (n-i-1)
print(total_time)
from collections import defaultdict


with open('C:\Program Files (x86)\AdventOfCode\AoC_day6_test_File.txt') as f:
   lines = [int(x) for x in f.readline().split(',')]

days = defaultdict(int)

for line in lines:
    if line not in days:
        days[line] = 0
    days[line] += 1




for day in range(256):
    futuredays = defaultdict(int)
    for i, j in days.items():
        if i == 0:
           futuredays[6] += j
           futuredays[8] += j
        else:
            futuredays[i-1] += j
    days = futuredays        

print(sum(days.values()))
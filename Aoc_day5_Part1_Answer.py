from typing import DefaultDict

with open('C:\Program Files (x86)\AdventOfCode\AoC_day5_File.txt') as f:
   lines = f.readlines()


grid = DefaultDict(int)

for line in lines:
    point1, point2 = line.split(' -> ')
    point1 = tuple(map(int, point1.split(',')))
    point2 = tuple(map(int, point2.split(',')))
   
    point1, point2 = sorted([point1, point2])
    if point1[0] == point2[0] or point1[1] == point2[1]:
        for i in range(point1[0], point2[0]+1):
            for j in range(point1[1], point2[1]+1):
                grid[(i,j)] += 1
              
            

    else:
        slope = (point2[1] - point1[1]) / (point2[0] - point1[0])
        startofslope = point1[1]
        for i in range(point1[0], point2[0]+1):
            grid[(i,startofslope)] += 1
            startofslope += slope

   




print(f'part 1: {len([point for point, num in grid.items() if num > 1])}')





with open('C:\Program Files (x86)\AdventOfCode\AoC_day6_test_File.txt') as f:
   lines = [int(x) for x in f.readline().split(',')]
   
for days in range(80):
    index = 0
    for i in range(len(lines)):
        if lines[index] == 0:
            lines[index] = 6
            lines.append(8)
        else:
            lines[index] -= 1

        index += 1

print(len(lines))



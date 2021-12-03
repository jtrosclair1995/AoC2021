with open('C:\Program Files (x86)\AdventOfCode\AoC_day3_File.txt') as f:
    values = [f.read().split()]

gamma = ''
epsilon = ''
print(len(values[0]))

for i in range(0, len(values[0])):
    zero = 0
    one = 0
    for j in range(0, len(values)):
        if values[j][i] == 0:
            zero += 1
        else:
            one += 1
        if zero > one:
            gamma = '0'
            epsilon = '1'
        else:
            gamma = '1'
            epsilon = '0'
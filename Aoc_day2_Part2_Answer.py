with open('C:\Program Files (x86)\AdventOfCode\AoC_day2_File.txt') as values1:
    values = values1.readlines()



x = 0
y = 0
z = 0



for i in values:
   i = i.split()
   if i[0] == 'forward':
     x += int(i[1])
     y += z * int(i[1])
   elif i[0] == 'down':
        z += int(i[1])
   else:
        z -= int(i[1])

print(x*y)
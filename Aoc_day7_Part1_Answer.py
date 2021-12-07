with open('C:\Program Files (x86)\AdventOfCode\AoC_day7_File.txt') as f:
   lines = [int(x) for x in f.readline().split(',')]




def subtractvalues(nums):
    sum1 = 0
    sum2 = 0
    sumtotal = 10000000
    for i in range(len(lines)):
        sum1 = nums - lines[i]
        if sum1 < 0:
            sum1 *= -1

        sum2 += sum1
    
    if sum2 < sumtotal:
        sumtotal = sum2
    return sumtotal
    
deftotal = 10000000000000000
for i in range(len(lines)):
    x = subtractvalues(lines[i])  
    if deftotal > x:
        deftotal = x
print(deftotal)
    


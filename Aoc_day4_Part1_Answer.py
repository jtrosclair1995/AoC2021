with open('C:\Program Files (x86)\AdventOfCode\AoC_day4_File.txt') as f:
    numstodraw = [int(x) for x in f.readline().strip('\n').split(',')]
    bingocards = []
    while f.readline():
        bingocard = []
        for i in range(5):
            bingocard.extend([int(x) for x in f.readline().strip('\n').split(' ') if x != ''])
        bingocards.append(bingocard)



def winner(bingocard):
    start = 0
    for i in range(5):
        if (bingocard[start] + bingocard[start + 1] + bingocard[start + 2] + bingocard[start + 3] + bingocard[start + 4] == -5):
            return True
        start += 5

    start = 0
    for i in range(5):    
        if (bingocard[start] + bingocard[start + 5] + bingocard[start + 10] + bingocard[start + 15] + bingocard[start + 20] == -5):
            return True
        start += 1
        
    return False


DefWinner = False
while DefWinner == False:
    number = numstodraw[0]
    numstodraw = numstodraw[1:]
    for bingocard in bingocards:
        for i in range(len(bingocard)):
            if bingocard[i] == number:
                bingocard[i] = -1

    index = 0
    while index < len(bingocards):
        if winner(bingocards[index]):
            if len(bingocards) > 1:
                bingocards.pop(index)
            else:
                DefWinner = True
                break
        else:
            index += 1
print(number * sum([x for x in bingocard if x != -1]))


        
        

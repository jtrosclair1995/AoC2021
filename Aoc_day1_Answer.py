f = open("AoC_day1_File.txt", "r")
lines = f.readlines()
nums = [int(line.strip()) for line in lines]

count = 0

prevsum = 20000
firstsum = sum(nums[:3])

for i in range(len(nums) - 3):
    if firstsum > prevsum:
        count += 1

    prevsum = firstsum

    firstsum -= nums[i]
    firstsum += nums[i + 3]


if firstsum > prevsum:
    count += 1
print(count)


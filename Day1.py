target = 2020
big_nums = []
lil_nums = []

with open('./input/day1.txt') as f:
    lines = [line.rstrip() for line in f]

for line in lines:
    if((2020 / 2) > int(line)):
        big_nums.append(int(line))
    else:
        lil_nums.append(int(line))

for lil in lil_nums:
    for big in big_nums:
        value = big + lil
        if value == target:
            print(lil)
            print(big)
            print(big * lil)

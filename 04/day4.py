def part1(data: list):
    ctr = 0
    for item in data:
        curr = [[int(_) for _ in i.split('-')] for i in item]
        if (curr[0][0] <= curr[1][0] and curr[0][1] >= curr[1][1]) or \
                (curr[1][0] <= curr[0][0] and curr[1][1] >= curr[0][1]):
            ctr += 1
    print(ctr)


def part2(data: list):
    for item in data:
        curr = [[int(_) for _ in i.split('-')] for i in item]


with open('day4_input.txt', 'r') as f:
    items = [line.strip() for line in f.readlines()]
    data = [item.split(',') for item in items]
    # part1(data)
    part2(data)

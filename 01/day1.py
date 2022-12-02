def part1(lines):
    maxelf = 0
    currval = 0
    for v in lines:
        if v == '':
            maxelf = max(currval, maxelf)
            currval = 0
        else:
            currval += int(v)
    print(maxelf)


def part2(lines):
    top = [0, 0, 0]
    currval = 0
    for v in lines:
        if v == '':
            if any(currval > elf for elf in top):
                top[top.index(min(top))] = currval
                top.sort()
            currval = 0
        else:
            currval += int(v)
    print(sum(top))


with open('day1_input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    part1(lines)
    part2(lines)

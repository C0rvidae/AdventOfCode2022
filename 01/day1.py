def part1(data):
    maxelf = 0
    currval = 0
    for v in data:
        if v == '':
            maxelf = max(currval, maxelf)
            currval = 0
        else:
            currval += int(v)
    print(maxelf)


def part2(data):
    top = [0, 0, 0]
    currval = 0
    for v in data:
        if v == '':
            if any(currval > elf for elf in top):
                top[top.index(min(top))] = currval
                top.sort()
            currval = 0
        else:
            currval += int(v)
    print(sum(top))


def better(data):
    print(sorted([sum([int(number) for number in item.split()]) for item in " ".join(data).split('  ')])[-3:])


with open('day1_input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    # part1(lines)
    # part2(lines)
    better(lines)

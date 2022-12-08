def part1(data: list):
    print(sum([1 for _ in data
               if (_[0][0] <= _[1][0] and _[0][1] >= _[1][1]) or (_[1][0] <= _[0][0] and _[1][1] >= _[0][1])]))


def part2(data: list):
    print(sum([1 for _ in data
               if any(a == b for a in range(_[0][0], _[0][1] + 1) for b in range(_[1][0], _[1][1] + 1))]))


with open('day4_input.txt', 'r') as f:
    items = [_.strip() for _ in f.readlines()]
    data = [[[int(_) for _ in _.split('-')] for _ in _.split(',')] for _ in items]
    part1(data)
    part2(data)

def get_priority(letter):
    return ord(letter) + 1 - (ord('a') if letter.islower() else ord('A') - 26)


def part1(data):
    total_value = 0
    for item in data:
        total_value += get_priority(set(item[0]).intersection(item[1]).pop())
    print(total_value)


def part2(data):
    total_value = 0
    for items in data:
        total_value += get_priority(set(items[0]).intersection(set(items[1])).intersection(set(items[2])).pop())
    print(total_value)


with open('day3_input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    items = [(item[:len(item)//2], item[len(item)//2:]) for item in lines]
    part1(items)
    items = [lines[i:i + 3] for i in range(0, len(lines), 3)]
    part2(items)

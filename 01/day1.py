def better(data):
    print(sorted([sum([int(number) for number in item.split()]) for item in " ".join(data).split('  ')])[-3:])


with open('day1_input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    better(lines)

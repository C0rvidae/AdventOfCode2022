import pprint
import re


# --- --- #
#  Part 1 #
# --- --- #
def extract_data(items):
    stacks = t_instructions = []
    numbers = ""
    for item in items:
        if '[' not in item:
            numbers = item.strip()
            t_instructions = items[items.index(item)+2:]
            break
        stacks.append(item)
    instructions = [[int(_) for _ in re.findall(r'\d+', instr)] for instr in t_instructions]
    return stacks, numbers, instructions


def fill_stacks(stacks, boxes, size):
    for box in boxes:
        box = box.replace('  ', '!').replace('[', '').replace(']', '').replace('!!', '!').replace(' ', '')
        if len(box) <= size:
            box += '!' * (size - len(box))
        for idx, c in enumerate(box):
            stacks[idx].append(c)
    stacks = [_[::-1] for _ in stacks]
    stacks = [_[:_.index('!')] if '!' in _ else _ for _ in stacks]
    return stacks


def parse_instructions(stacks, instructions):
    for instruction in instructions:
        for _ in range(instruction[0]):
            stacks[instruction[2] - 1].append(stacks[instruction[1] - 1].pop())
    print("".join([_[-1] for _ in stacks]))


def parse_instructions2(stacks, instructions):
    for instruction in instructions:
        stacks[instruction[2] - 1] += stacks[instruction[1] - 1][0 - instruction[0]:]
        stacks[instruction[1] - 1] = stacks[instruction[1] - 1][:0 - instruction[0]]
    print("".join([_[-1] for _ in stacks]))


with open('day5_input.txt', 'r') as f:
    data = [_[:-1] for _ in f.readlines()]
    boxes, numbers, instructions = extract_data(data)
    stack_amount = int(numbers[-1:])
    stacks = [[] for _ in range(stack_amount)]
    nstacks = fill_stacks(stacks, boxes, stack_amount)
    # Part 1
    # parse_instructions(nstacks, instructions)
    parse_instructions2(nstacks, instructions)
    # part2(data)

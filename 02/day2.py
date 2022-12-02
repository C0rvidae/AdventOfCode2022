def part1(games):
    plays = {'X': 1, 'Y': 2, 'Z': 3}
    tie = {'A': 'X', 'B': 'Y', 'C': 'Z'}
    answr = {'A': 'Y', 'B': 'Z', 'C': 'X'}
    score = 0
    for game in games:
        score += plays[game[1]]
        if answr[game[0]] == game[1]:
            score += 6
        elif tie[game[0]] == game[1]:
            score += 3
    print(score)


def part2(games):
    score = 0
    corrptie = {'A': 1, 'B': 2, 'C': 3}
    corrplos = {'A': 3, 'B': 1, 'C': 2}
    corrpwin = {'A': 2, 'B': 3, 'C': 1}
    for game in games:
        match game[1]:
            case 'X':
                score += corrplos[game[0]]
            case 'Y':
                score += 3 + corrptie[game[0]]
            case 'Z':
                score += 6 + corrpwin[game[0]]
    print(score)


# A/X = Rock, B/Y = Paper, C/Z = Scissors
with open('day2_input.txt') as src:
    games = [l.strip().split() for l in src.readlines()]
    part1(games)
    part2(games)


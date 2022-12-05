def get_win_score(opponent, self):
    if opponent == self:
        # draw
        return 3

    if self == opponent + 1 or self == opponent - 2:
        # self wins
        return 6

    # self looses
    return 0

def get_round_score(round):
    opponent = ord(round[0]) - 64
    self = ord(round[2]) - 87

    win_score = get_win_score(opponent, self)
    self_score = self
    # print(self_score, win_score)
    return self_score + win_score


def get_tournament_score(tournament):
    total_score = 0
    for round in tournament:
        round_score = get_round_score(round)
        total_score += round_score

    return total_score


def main():
    with open('02input.txt') as f:
        lines = f.readlines()
    score = get_tournament_score(lines)
    print(score)

if __name__ == '__main__':
    main()

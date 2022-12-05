def choose_move(round):
    opponent = ord(round[0]) - 64
    win_score = (ord(round[2]) - 88) * 3
    scores = [3, 1, 2, 3, 1]

    if win_score == 3:
        self_score = opponent
        return (opponent, win_score)

    if win_score == 6:
        pass
        return (scores[opponent + 1], win_score)

    return (scores[opponent - 1], win_score)


def get_round_score(round):
    (self_score, win_score) = choose_move(round)
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

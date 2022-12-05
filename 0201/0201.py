def get_score(tournament):
    for round in tournament:
        opponent = tournament[0]
        self = tournamet[2]
        print(opponent, self)

def main():
    with open('02input.txt') as f:
        lines = f.readlines()

    score = get_score(lines)


if __name__ == '__main__':
    main()

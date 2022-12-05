def get_repeat(comp_1, comp_2):
    for item in comp_1:
        if item in comp_2:
            return item

    return 0


def priority(item):
    hex = ord(item)
    if hex >= 97:
        # lowercase
        return hex - 96

    # uppercase
    return hex - 38


def get_score(line):
    items = len(line) - 1
    comp_1 = line[:(items//2)]
    comp_2 = line[(items//2):-1]

    item_priority = priority(get_repeat(comp_1, comp_2))
    return item_priority


def priority_sum(packs):
    sum = 0
    for pack in packs:
        sum += get_score(pack)

    return sum


def main():
    with open('03input.txt') as f:
        lines = f.readlines()
    score = priority_sum(lines)
    print(score)


if __name__ == '__main__':
    main()

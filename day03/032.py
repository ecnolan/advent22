def get_badge(line1, line2, line3):
    for item in line1:
        if item in line2 and item in line3:
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
    n_groups = len(packs)//3
    print(n_groups)
    sum = 0
    for g_num in range(n_groups):
        badge = get_badge(packs[g_num * 3], packs[(g_num * 3) + 1],
                          packs[(g_num * 3) + 2])
        sum += priority(badge)
    return sum


def main():
    with open('03input.txt') as f:
        lines = f.readlines()
    score = priority_sum(lines)
    print(score)


if __name__ == '__main__':
    main()

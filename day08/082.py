def left(r,c,lines):
    count = 0
    for nc in reversed(range(c)):
        count += 1
        if int(lines[r][nc]) >= int(lines[r][c]):
            return count
    return count


def right(r,c,lines):
    ncols = len(lines)
    count = 0
    for nc in range(c+1,ncols):
        count += 1
        if int(lines[r][nc]) >= int(lines[r][c]):
            return count
    return count


def top(r,c,lines):
    count = 0
    for nr in reversed(range(r)):
        count += 1
        if int(lines[nr][c]) >= int(lines[r][c]):
            return count
    return count


def bottom(r, c, lines):
    count = 0
    nrows = len(lines[0])-1
    for nr in range(r+1,nrows):
        count += 1
        if int(lines[nr][c]) >= int(lines[r][c]):
            return count
    return count


def get_scenic_score(r,c,lines):
    (lv, rv) = (left(r,c, lines), right(r,c, lines))
    (tv, bv) = (top(r,c, lines), bottom(r,c, lines))
    return (lv * rv * tv * bv)


def main():
    with open('08input.txt') as f:
        lines = f.readlines()

    nrows = len(lines[0])-1
    ncols = len(lines)
    highestscore = 0

    for r in range(nrows):
        for c in range(ncols):
            newscore = get_scenic_score(r,c,lines)
            if newscore > highestscore:
                highestscore = newscore
    print(highestscore)


if __name__ == '__main__':
    main()

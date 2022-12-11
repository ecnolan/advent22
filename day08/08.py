def left(r,c,lines):
    for nc in range(c):
        if int(lines[r][nc]) >= int(lines[r][c]):
            return False
    return True


def right(r,c,lines):
    ncols = len(lines)
    for nc in range(c+1,ncols):
        if int(lines[r][nc]) >= int(lines[r][c]):
            return False
    return True


def top(r,c,lines):
    for nr in range(r):
        if int(lines[nr][c]) >= int(lines[r][c]):
            return False
    return True


def bottom(r, c, lines):
    nrows = len(lines[0])-1
    for nr in range(r+1,nrows):
        if int(lines[nr][c]) >= int(lines[r][c]):
            return False
    return True


def main():
    with open('08input.txt') as f:
        lines = f.readlines()

    nrows = len(lines[0])-1
    ncols = len(lines)
    sum = 2*len(lines) + 2*(len(lines[0])-3)

    for r in range(1,nrows-1):
        for c in range(1,ncols-1):
            (lv, rv) = (left(r,c, lines), right(r,c, lines))
            (tv, bv) = (top(r,c, lines), bottom(r,c, lines))
            if lv or rv or tv or bv:
                sum += 1

    print(sum)


if __name__ == '__main__':
    main()

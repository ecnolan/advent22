from statistics import mean

def updatehead(pos, dir):
    (r,c) = pos
    if dir == 'U':
        return (r+1, c)
    if dir == 'D':
        return (r-1, c)
    if dir == 'L':
        return (r, c-1)
    if dir == 'R':
        return (r, c+1)


def updatetail(hpos, tpos):
    (hr, hc) = hpos
    (tr, tc) = tpos
    if hr == tr:
        # same row, change column:
        if abs(hc - tc) == 2:
            newc = mean([hc, tc])
            return(tr, newc)
        return (tr, tc)
    if hc == tc:
        # same col, change row
        if abs(hr - tr) == 2:
            newr = mean([hr, tr])
            return(newr, tc)
        return (tr, tc)
    if abs(hc-tc)==1 and abs(hr-tr)==1:
        return (tr, tc)
    if abs(hc-tc)==2 and abs(hr-tr)==1:
        # change column to avg(tc, hc)
        return (hr, mean([tc, hc]))
    if abs(hc-tc)==1 and abs(hr-tr)==2:
        return (mean([tr, hr]), hc)
    if abs(hc-tc)==2 and abs(hr-tr)==2:
        # added for part 2 possibilities
        return (mean([tr, hr]), mean([tc, hc]))


def strip(list):
    """ removes consecutive duplicates from list """
    new = [list[0]]
    while len(list) != 0:
        if list[0] != new[-1]:
            new.append(list[0])
        list = list[1:]

    return new


def main():
    with open('09input.txt') as f:
        lines = f.readlines()

    hpos = (0,0)
    visited = [(0,0)]
    allheads = []

    for line in lines:
        moves = int(line[line.find(' ')+1:-1])
        dir = line[0]
        print(moves, dir)
        for move in range(moves):
            hpos = updatehead(hpos, dir)
            allheads.append(hpos)

    stripped_visited = [*set(allheads)]
    print(len(stripped_visited))

    prev_moves = allheads
    curr_moves = []
    tpos = (0,0)
    visited = []
    for i in range(9):
        for move in prev_moves:
            tpos = updatetail(move, tpos)
            curr_moves.append(tpos)
            if tpos not in visited:
                visited.append(tpos)
        print(len(visited))
        prev_moves = curr_moves
        curr_moves = []
        tpos = (0,0)
        visited = []


if __name__ == '__main__':
    main()

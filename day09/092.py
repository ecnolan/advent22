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


def updatetail(hpos, pos1):
    (hr, hc) = hpos
    (tr, tc) = pos1
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


def main():
    with open('09input.txt') as f:
        lines = f.readlines()

    ropes = []
    # hpos = (0,0)
    for i in range(9+1):
        ropes.append((0,0))

    visited = [(0,0)]

    for line in lines:
        moves = int(line[line.find(' ')+1:-1])
        dir = line[0]
        print(moves, dir)
        for move in range(moves):
            hpos = updatehead(ropes[0], dir)
            ropes[0] = hpos
            for i in range(len(ropes)-1):
                pos = updatetail(ropes[i], ropes[i+1])
                ropes[i+1] = pos
            print(ropes)
            if pos not in visited:
                visited.append(pos1)
    # print(visited)
    print(len(visited))






if __name__ == '__main__':
    main()

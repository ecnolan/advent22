def get_n_stacks(lines):
    for line in lines:
        if line[1] == '1':
             # this is the line that counts the number of stacks
             count = line[-2:-1]
             # print(line[-3:])
             return int(count)

def create_empty_stacks(lines):
    """ create correct number of empty stacks """
    n_stacks = get_n_stacks(lines)
    print("n stacks", n_stacks)
    stacks = []
    for n in range(n_stacks):
        stacks.append([])
    return stacks

def fill_stacks(lines):
    """ given input, create a nested list. stacks[0] is the first stack.
    stacks[0][0] is the bottom item of the first stack
    stacks[0][-1] is the top item of the first stack """

    stacks = create_empty_stacks(lines)
    print(stacks)

    for line in lines:
        if '[' not in line:
            # done inputting stacks into grid
            for stack in stacks:
                stack = stack.reverse()
            return stacks
        count = 0
        for char in line:
            if char >= 'A' and char <= 'Z':
                index = int((count-1)/4)
                # print(index)
                stacks[index].append(char)
            count += 1

def create_move_list(lines):
    """ organize lines into a list of moves. Each move will be a tuple (x,y,z)
    which indicates move x from y to z """
    moves = []
    for line in lines:
        if 'move' in line:
            # is a move line.
            i1 = (line.find('move'))
            i2 = (line.find('from'))
            i3 = (line.find('to'))
            # print(i1, i2, i3)
            move = (line[i1+5 : i2], line[i2+5], line[i3 + 3])
            moves.append(move)
    return moves

def execute(moves, stacks):
    for move in moves:
        print(" -------- new move --------")
        n_items = int(move[0])
        origin = stacks[int(move[1])-1]
        dest = stacks[int(move[2])-1]

        # print(n_items, origin, dest)

        for n in range(n_items-1):
            obj = origin.pop()
            dest.append(obj)
            print(stacks)

    return stacks


def main():
    with open('05test.txt') as f:
    # with open('05input.txt') as f:
        lines = f.readlines()
    # print(lines)

    stacks = fill_stacks(lines)
    print(stacks)

    moves = create_move_list(lines)
    print(moves)

    result = execute(moves, stacks)






if __name__ == '__main__':
    main()

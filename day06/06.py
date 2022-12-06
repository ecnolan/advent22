def update_recent(recent, data):
    next = data.pop(0)
    new_recent = recent[1:]
    new_recent.append(next)
    return(new_recent, data)


def unique(list):
    listlen = len(list)
    setlen = len(set(list))
    if setlen == listlen:
        return True
    return False


def create_recent(data):
    recent = []
    # for i in range(4):
    for i in range(14):
        recent.append(data[0])
    print(len(recent))
    return recent



def find_4(data):
    recent = create_recent(data)
    count = 0
    while True:
        print(recent, data[0])
        (recent, data) = update_recent(recent, data)
        count += 1

        if unique(recent):
            return count


def makedata(line):
    list = []
    for char in line:
        list.append(char)
    return list


def main():
    with open('06input.txt') as f:
        lines = f.readlines()
    data = makedata(lines[0])

    print(find_4(data))


if __name__ == '__main__':
    main()

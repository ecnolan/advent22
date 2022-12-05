def ch_to_int(chars):
    sum = 0
    num_len = len(chars)
    for n in range(num_len):
        num = int(chars[n])
        pwr = num_len - n - 1
        sum += num * (10 ** pwr)
    return sum


def get_elf_zone(alpha_zone):
    """ convert text zone into numerical range.
    ie: get_elf_zone("10 - 100") returns (10, 100) """
    start = ch_to_int(alpha_zone[:alpha_zone.find('-')])
    end = ch_to_int(alpha_zone[alpha_zone.find('-')+1:])
    return(start, end)


def fully_contains(z1, z2):
    """ returns true if z1 is entirely contained in z2 or vice versa """
    if z1[0] >= z2[0] and z1[1] <= z2[1]:
        # zone 2 contains zone 1
        return True
    if z1[0] <= z2[0] and z1[1] >= z2[1]:
        # zone 1 contains zone 2
        return True
    return False


def overlap(z1, z2):
    """ returns true if z1 and z2 overlap at all """
    for n1 in range(z1[0], z1[1]+1):
        if n1 in range(z2[0], z2[1]+1):
            return True
    return False


def get_zones(pair):
    z1 = get_elf_zone(pair[:pair.find(',')])
    z2 = get_elf_zone(pair[pair.find(',') + 1:-1])

    return(z1, z2)


def main():
    with open('04input.txt') as f:
        lines = f.readlines()
    sum = 0
    sum2 = 0
    for pair in lines:
        zones = get_zones(pair)
        if fully_contains(zones[0], zones[1]):
            sum += 1
        if overlap(zones[0], zones[1]):
            sum2 += 1

    print("part1", sum)
    print("part2", sum2)

if __name__ == '__main__':
    main()

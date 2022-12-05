def sumlist(list):
    sum = 0
    for item in list:
        sum += item
    return sum

def main():
    with open('01input.txt') as f:
        lines = f.readlines()

    cal_list = []
    elf_sum = 0
    for line in lines:
        chline = line[:-1]
        sum = 0
        num_len = len(chline)
        for n in range(num_len):
            num = int(chline[n])
            pwr = num_len - n - 1
            sum += num * (10 ** pwr)

        elf_sum += sum
        if sum == 0:
            # new elf
            cal_list.append(elf_sum)
            elf_sum = 0

    cal_list.append(elf_sum)
    cal_list.sort(reverse = True)
    # solution 1
    print(cal_list[0])
    # solution 2
    print(sumlist(cal_list[:3]))


if __name__ == '__main__':
    main()

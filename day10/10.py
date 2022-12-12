"""
noop   takes 1 cycle
addx v   2 cycles, the X register is increased by the value V. (V can be negative.)
addx -5
"""

def main():
    with open('10input.txt') as f:
        lines = f.readlines()

    x = 1
    cycle = 0
    sum = 0
    locations = []
    for line in lines:
        cycle += 1
        locations.append(x)
        if (cycle - 20) % 40 == 0:
            print(cycle, x, "     ", cycle*x)
            sum += (cycle*x)
        if 'addx' in line:
            cycle += 1
            locations.append(x)
            if (cycle - 20) % 40 == 0:
                print(cycle, x, "     ", cycle*x)
                sum += (cycle*x)
            add = int(line[line.find(' ')+1:-1])
            x += add

    for i in range(len(locations)):
        x = locations[i]
        if i%40 in [x-1, x, x+1]:
            print('#', end = '')
        else:
            print('.', end = '')
        if (i+1) % 40 == 0:
            print('')

    print(sum)

if __name__ == '__main__':
    main()

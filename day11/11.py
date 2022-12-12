class Monkey:
    def __init__(self, num, items = [], operation = '', test = '', truedest = None, falsedest = None, inspections = 0):
        self.num = num
        self.items = items
        self.operation = operation
        self.test = test
        self.truedest = truedest
        self.falsedest = falsedest
        self.inspections = inspections


    def inspect(self, item):
        self.inspections += 1
        old = item
        # x = (eval(self.operation)) // 3
        x = (eval(self.operation))
        t = eval(self.test)

        if t:
            return (self.truedest, x)
        return (self.falsedest, x)


    def monkey_print(self):
        print('Monkey', self.num, end = '')
        print('      items:', self.items)
        print('              operation:', self.operation)
        print('              test:', self.test)
        print('              t/f throw to:', self.truedest, self.falsedest)
        print('')
        print('              inspections:', self.inspections)
        print('')

"""
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3
"""

def generate_monkeys(lines):
    monkeys = []
    curr_monkey = None
    for line in lines:
        if 'Monkey' in line:
            curr_monkey = Monkey(int(line[-3]))
            monkeys.append(curr_monkey)
        if 'Starting items:' in line:
            rest = line[line.find(':')+2 : -1]
            list = rest.split(", ")
            for i in range(len(list)):
                list[i] = int(list[i])
            curr_monkey.items = list
        if 'Operation' in line:
            op = line[line.find('=') + 2:-1]
            curr_monkey.operation = op
        if 'Test' in line:
            num = line[line.find('y ')+2:-1]
            curr_monkey.test = ('x % ' + num + ' == 0')
        if 'true' in line:
            curr_monkey.truedest = int(line[-2])
        if 'false' in line:
            curr_monkey.falsedest = int(line[-2])

    return monkeys


def main():
    with open('11input.txt') as f:
        lines = f.readlines()

    rounds = 10000

    monkeys = generate_monkeys(lines)
    for round in range(rounds):
        print(round)
        for monkey in monkeys:
            for item in monkey.items:
                (recip_index, newitem) = monkey.inspect(item)
                recipient = monkeys[recip_index]
                recipient.items.append(newitem)
            monkey.items = []

    inspections = []
    for monkey in monkeys:
        # monkey.monkey_print()
        # print(monkey.num, ":", monkey.items, monkey.inspections)
        print(monkey.num, ":", monkey.inspections)
        inspections.append(monkey.inspections)

    max1 = max(inspections)
    inspections.remove(max1)
    max2 = max(inspections)

    print(max1 * max2)


if __name__ == '__main__':
    main()

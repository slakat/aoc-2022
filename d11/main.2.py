import numpy as np


class Monkey():
    input_data = list
    monkey_id = int
    items: list
    a: int  # in formula = a*x**2 + b*x + c
    b: int  # in formula = a*x**2 + b*x + c
    c: int  # in formula = a*x**2 + b*x + c
    divisibility_test: int
    true_target: int
    false_target: int
    inspection_count: int

    def __init__(self, input_data):
        self.monkey_id = int(input_data[0][7])
        self.items = list(map(np.int64, input_data[1][18:].split(', ')))
        self.a = np.int64(1 if input_data[2][-3:] == 'old' else 0)
        self.b = np.int64(input_data[2][25:] if (input_data[2][23] == '*' and self.a == 0) else 0)
        self.b = np.int64(1 if input_data[2][23] == '+' else self.b)
        self.c = np.int64(input_data[2][25:] if input_data[2][23] == '+' else 0)
        self.divisibility_test = np.int64(input_data[3][21:])
        self.true_target = int(input_data[4][29:])
        self.false_target = int(input_data[5][30:])
        self.inspection_count = 0


raw_data = [monkey.split("\n") for monkey in open("input.txt").read().split("\n\n")]
monkeys = [Monkey(monkey) for monkey in raw_data]
HCF = 1
for m in monkeys:
    HCF *= m.divisibility_test
for round_count in range(10000):
    for m in monkeys:
        while m.items != []:
            m.inspection_count += 1
            val = m.items.pop(0)
            val = np.mod(val, HCF)
            val = (m.a * val ** 2) + (m.b * val) + m.c
            # val = int(np.floor(val/3))  #only in part 1
            if np.mod(val, m.divisibility_test) == 0:
                monkeys[m.true_target].items.append(val)
            else:
                monkeys[m.false_target].items.append(val)
inspections = sorted(m.inspection_count for m in monkeys)
print('Answer:', inspections[-1] * inspections[-2])

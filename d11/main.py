# day 11

from collections import deque
import numpy as np

op = {'+': lambda x, y: np.sum([x, y], dtype=np.int64),
      '-': lambda x, y: x - y,
      '*': lambda x, y: np.multiply(x,y),
      '/': lambda x, y: x / y
      }

file = "input.txt"
with open(file) as f:
    lines = f.readlines()

monkeys = []
rounds = 10000
inspections = []

# each monkey has {items,operation,test}
monkey = 0
for e,line in enumerate(lines):
    line = line.strip()
    if line.startswith("Monkey"):
        monkeys.append({'items': deque()})
        inspections.append(0)
        if e == 0: continue 
        else : monkey +=1
    if line.startswith('Starting'):
        items = list(map(np.int64, line.split(':')[1].split(', ')))
        for t in items : monkeys[monkey]['items'].append(t)
    if line.startswith('Operation'):
        operation = line.split('=')[1].strip().split(' ')
        monkeys[monkey]['operation'] = operation
    if line.startswith('Test'):
        monkeys[monkey]['test'] = [np.int64(line.split(' ')[3])]
    if line.startswith('If'):
        next_monkey = np.int64(line.split(' ')[5])
        monkeys[monkey]['test'].append(np.int64(next_monkey))

for i in range(rounds):
    for e,m in enumerate(monkeys):
        #print('Monkey ',e)
        for i in range(len(m['items'])):
            item = m['items'].popleft()
            #print('Monkey inspects an item with a worry level of', item)
            inspections[e] += 1 
            first = m['operation'][0]
            second = m['operation'][2]
            if first == 'old': first = item
            else : first = np.int64(first)
            if second == 'old' :  second = item
            else : second = np.int64(second)
            new_worry = np.int64(op[m['operation'][1]](first,second))
            #print('Worry level is now ',new_worry)
            # pt2 new_worry = int(new_worry / 3)
            #print('Monkey gets bored with item. Worry level is divided by 3 to ',new_worry)
            if np.mod(new_worry,m['test'][0]) == 0 :
                monkeys[m['test'][1]]['items'].append(int(new_worry))
                #print('Item with worry level 500 is thrown to monkey ',m['test'][1])
            else : 
                monkeys[m['test'][2]]['items'].append(int(new_worry))
                #print('Item with worry level 500 is thrown to monkey ',m['test'][2])
        #print('\n')

for e,i in enumerate(inspections):
    print('Monkey ',e,' inspected items ',i,' times')
        
inspections_copy = inspections[:]
largest_integer = max(inspections_copy)  
inspections_copy.remove(largest_integer)
second_largest_integer = max(inspections_copy)  # 26
monkey_business = np.int64(largest_integer)*np.int64(second_largest_integer)

print('monkey business: ',monkey_business)
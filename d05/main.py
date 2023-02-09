# Day 05
from collections import deque


def moves1(queues,moves):
    #moving
    for i in moves:
         move = [int(s) for s in i.split() if s.isdigit()]
         for j in range(move[0]):
            element = queues[move[1]-1].pop()
            queues[move[2]-1].append(element)
    return queues

def moves2(queues,moves):
    #moving
    for i in moves:
         move = [int(s) for s in i.split() if s.isdigit()]
         save = deque()
         for j in range(move[0]):
            element = queues[move[1]-1].pop()
            save.appendleft(element)
        
         for e in save:
            queues[move[2]-1].append(e)
    return queues

file = "input.txt"

with open(file) as f:
    lines = f.readlines()


stacks, moves = [],[]
for i in lines:
    if (len(i.strip()) > 0 and 'move' not  in i):
        stacks.append(i)
    elif ('move' in i):
        moves.append(i)

#delete column numbers
stacks = stacks[:-1]

# Declaring dequeues
longitude = len(lines[0])
columns = int((longitude - ((longitude-1)/2))/2)
queues = [deque() for _ in range(columns)]

#filling stacks
for i in stacks:
    tmp = i
    col = 0
    for pos in range(columns-1):
        x = tmp[0:3]
        if(x[1]!=' '):
            queues[col].appendleft(x[1])
        tmp = tmp[4:]
        col = col + 1
    if(tmp[1]!=' '):
        queues[col].appendleft(tmp[1])    

queues = moves2(queues,moves)

top = ''
for i in queues:
    top = top + str(i[-1])

print(top)
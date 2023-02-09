#day 09

import numpy 

def check_touching(head,tail):
    distance = (abs(head[0] - tail[0]),abs(head[1] - tail[1]))
    rsquared = pow(distance[0], 2) + pow(distance[1], 2)
    if(rsquared < 3):
        return True
    else:
        return False

def move_tail(head,tail):
    x = tail[0]+numpy.sign(head[0]-tail[0])
    y = tail[1]+numpy.sign(head[1]-tail[1])
    return [x,y]

file = "input.txt"
with open(file) as f:
    lines = f.readlines()

start,head = [0,0],[0,0]
tails = [[0,0]] * 9
visited_pos_tails = [{(0,0)},{(0,0)},{(0,0)},{(0,0)},{(0,0)},{(0,0)},{(0,0)},{(0,0)},{(0,0)}]

for i in lines:
    moves = i.replace('\n','').split(' ')
    for r in range(int(moves[1])):
        if('U' == moves[0]):
            head[0] = head[0]+1
        elif('R' == moves[0]):
            head[1] = head[1]+1
        elif('D' == moves[0]):
            head[0] = head[0]-1
        elif('L' == moves[0]):
            head[1] = head[1]-1

        tmp_head = [head[0],head[1]]
        for t in range(0,len(tails)):
            if(not check_touching(tmp_head,tails[t])):
                new_tail = move_tail(tmp_head,tails[t])
                tails[t] = new_tail
                visited_pos_tails[t].add((new_tail[0],new_tail[1]))
                tmp_head = [tails[t][0],tails[t][1]]
            else:
                break
                
print('Tail position for 2 knots',len(visited_pos_tails[0]))
print('Tail position for 10 knots',len(visited_pos_tails[8]))

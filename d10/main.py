# day 10


file = "input.txt"
with open(file) as f:
    lines = f.readlines()

cycle = 1
x_register = []
current_x = 1
drawing = [[] for i in range(6)]

for i in range(6):
    for j in range(40):
        drawing[i].append('')

for i in lines:
    i = i.replace('\n','')
    command = i.split(' ')
    if (command[0]=='noop'):
        cycle += 1
        x_register.append(current_x)
    if (command[0]=='addx'):
        for r in range(2) : x_register.append(current_x)
        cycle +=2
        current_x+= int(command[1])
       
cycles_sum = 0
for e,x in enumerate(x_register):
    if((e%40) in [x-1,x,x+1]):
        pixel = '#'
    else:
        pixel = '.' 
    drawing[int(e/40)][e%40] = pixel
    if((e+1) in [20,60,100,140,180,220] ):
        value = (e+1) * x
        cycles_sum +=value
        print((e+1),x,value)
print('sum',cycles_sum)

for i in drawing:
    print(''.join(i))

import numpy as np
forest = np.genfromtxt('input.txt', delimiter=1)
# part 1
len_x = forest.shape[0]
len_y = forest.shape[1]
inner = np.array([[ (forest[0:x,y].max() < forest[x,y]) or
            (forest[x+1:len_x,y].max() < forest[x,y]) or
            (forest[x,0:y].max() < forest[x,y]) or
            (forest[x,y+1:len_y].max() < forest[x,y])
            for x in range(1,len_x-1) ] for y in range(1,len_y-1) ])
sol_1 = inner.sum().sum()+len_x*2+len_y*2-4
print(sol_1)
# part 2
trees = np.array([[((forest[0:x,y][::-1] >= forest[x,y]).argmax() + 1 +
                   int(forest[0:x,y].max() < forest[x,y])*(forest[0:x,y].shape[0]-1))*
                   
                   ((forest[x+1:len_x,y] >= forest[x,y]).argmax() + 1 +
                   int(forest[x+1:len_x,y].max() < forest[x,y])*(forest[x+1:len_x,y].shape[0]-1))*
                   
                   ((forest[x,0:y][::-1] >= forest[x,y]).argmax() + 1 +
                   int(forest[x,0:y].max() < forest[x,y])*(forest[x,0:y].shape[0]-1))*
                   
                   ((forest[x,y+1:len_y] >= forest[x,y]).argmax() + 1 +
                   int(forest[x,y+1:len_y].max() < forest[x,y])*(forest[x,y+1:len_y].shape[0]-1))
                   
            for x in range(1,len_x-1) ] for y in range(1,len_y-1) ])
sol_2 = trees.max()
print(sol_2)
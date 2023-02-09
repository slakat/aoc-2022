# day 08

def argmax(a):
    return max(range(len(a)), key=lambda x : a[x])

def scenic_score(row, column, posr, posc):
	print(posc)
	top = len(column[:posc]) - argmax(column[:posc])
	right = argmax(row[posr:])
	bottom = argmax(column[posc:][::-1])
	left = len(row[:posr]) - argmax(row[:posr])
	print('bottom',bottom,len(column[posc:][::-1]))
	if(right==0): right = len(row[:posr])
	if(bottom==0): bottom = len(column[posc:])
	if(left==0): left = len(row[posr:])-1

	return [[top,right,bottom,left],top*right*bottom*left]

def column(matrix, i):
    return [row[i] for row in matrix]

def is_visible(tree, row, column, posr, posc):
	top,right,bottom,left = True,True,True,True
	st,sr,sb,sl = posc,len(row)-posr-1,len(column)-posc-1,posr
	for i, e in enumerate(column):
		if(i<posc and e>=tree):
			top=False
			break
	for i, e in enumerate(row):
		if(i<posr and e>=tree):
			left=False
			break
	for i, e in reversed(list(enumerate(row))):
		if(i>posr and e>=tree):
			right=False
			break
	for i, e in reversed(list(enumerate(column))):
		if(i>posc and e>=tree):
			bottom=False
			break
	# t,r,b,l
	return [top,right,bottom,left]

file = "test.txt"

with open(file) as f:
    lines = f.readlines()

board = []
visibles_trees = 0
for x in lines:
	row = list(x.replace('\n',''))
	board.append(row)
width = len(board[0])
height = len(board)
print('Board:',width,'x',height)

border_trees = 2*(width+height)-4
interior_trees = width*height-border_trees
visible_trees = border_trees
max_scenic_score = 0

for i in range(interior_trees):
	col = i%(height-2)+1
	row = int(i/(width-2)+1)
	column_values = column(board,col)
	tree = is_visible(board[row][col], board[row], column_values, col, row)
	if sum(tree) > 0:
		visible_trees = visible_trees + 1
	tree_sc = scenic_score(board[row], column_values, col, row)
	print(board[row][col],tree_sc[0])
	max_scenic_score = max(max_scenic_score,  tree_sc[1])
print('visible trees:',visible_trees)
print('Max Scenic Score:', max_scenic_score)

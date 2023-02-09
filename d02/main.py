# Day 02

'''
Rules

Ties
A = X -> Rock
B = Y -> Paper
C = Z -> scissor

Wins
A < Y
B < Z
C < X

loses
X < B
Y < C
Z < A  
'''

def calculate(lines):
	rules = {
	'AX': 3, 'BY': 3, 'CZ': 3,
	'AY': 6,'BZ': 6,'CX': 6,
	'BX': 0,'CY': 0,'AZ': 0,
	'X': 1, 'Y': 2, 'Z': 3
	}

	rules2 = {
	'AX': 0, 'BY': 3, 'CZ': 6,
	'AY': 3,'BZ': 6,'CX': 0,
	'BX': 0,'CY': 3,'AZ': 6,
	'XA': 3, 'YA': 1, 'ZA': 2,
	'XB': 1, 'YB': 2, 'ZB': 3,
	'XC': 2, 'YC': 3, 'ZC': 1
	}

	score = 0
	score2 = 0
	for i in lines:
		shapes = i.strip().split()
		round = "".join(shapes)
		score = score + rules[round] + rules[shapes[1]]
		score2 = score2 + rules2[round] + rules2[str(shapes[1])+str(shapes[0])]
	return [score,score2]

file = "input.txt"

with open(file) as f:
    lines = f.readlines()

round_score = calculate(lines)

print('score_1: '+ str(round_score[0]))
print('score_2: '+ str(round_score[1]))



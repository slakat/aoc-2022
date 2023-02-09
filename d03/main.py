# Day 03
import string

file = "input.txt"

with open(file) as f:
    lines = f.readlines()

dil=dict(zip(string.ascii_lowercase,[ord(c)-96 for c in string.ascii_lowercase]))
diu=dict(zip(string.ascii_uppercase,[ord(c)-38 for c in string.ascii_uppercase]))
di = {**dil, **diu}


priorities = 0
for i in lines:
	half = int(len(i)/2)
	groups = list(map(''.join, zip(*[iter(i)]*half)))

	duplicates = list(set(groups[0]).intersection(set(groups[1])))
	for d in duplicates:
		priorities = priorities + di[d]

print('priorities:'+ str(priorities))


elves = list(zip(*[iter(lines)]*3))
elves_priorities = 0
for e in elves:
	duplicates_0 = list(set(e[0]).intersection(set(e[1])).intersection(set(e[2])))
	for d in duplicates_0:
		if(d != '\n'):
			elves_priorities = elves_priorities + di[d]

print('elves priorities:'+str(elves_priorities))
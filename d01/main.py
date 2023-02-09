# Day 01

import heapq

file = "input.txt"

with open(file) as f:
    lines = f.readlines()

elves_resume = []
elves = []

index_elf = 0
for i in lines:
	if len(i.strip()) == 0 :
		index_elf = index_elf + 1
	else:
		if(len(elves_resume) > index_elf):
			elves_resume[index_elf] = elves_resume[index_elf] + int(i)
			elves[index_elf].append(int(i))
		else:
			elves_resume.append(int(i))
			elves.append([int(i)])

richest_elf = (max(elves_resume))
richest_elves =  heapq.nlargest(3, elves_resume)
print('-Elves # ------')
print(len(elves_resume))
print('- Max calories (elf)  ------')
print(richest_elf)
print('- Top 3 Max calories (elves)  ------')
print(sum(richest_elves))
print('------')

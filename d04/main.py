# Day 04

file = "input.txt"

with open(file) as f:
    lines = f.readlines()

pairs = []

for i in lines:
	elves = i.split(',')
	pair = []
	for e in elves:
		sections = e.split('-')
		all_sections = []
		for x in range(int(sections[0]), int(sections[1])+1):
			all_sections.append(x)
		pair.append(all_sections)
	pairs.append(pair)

fully = []
at_all = []

for p in pairs:
	check1 =  all(item in p[0] for item in p[1])
	check2 =  all(item in p[1] for item in p[0])
	check3 =  any(item in p[0] for item in p[1])
	check4 =  any(item in p[1] for item in p[0])
	if check1 or check2:
		fully.append(list(set(p[0]).intersection(set(p[1]))))
	if check3 or check4:
		at_all.append(list(set(p[0]).intersection(set(p[1]))))

print(len(fully))
print(len(at_all))
# day 06

file = "input.txt"

with open(file) as f:
    lines = f.read()

# pt1- 4 | pt2- 14
message_long = 14

tmp = lines
marker_found = False
marker = ''
pos = message_long
while(not marker_found):
	marker = tmp[0:message_long]
	tmp = tmp[1:]
	result = "".join(dict.fromkeys(marker))
	if(len(result)==message_long):
		marker_found = True
	else:
		pos = pos + 1
	if(len(tmp)<message_long):
		pos = None
		marker = None
		print(tmp,len(tmp))
		break
print('Found? :' + str(marker_found) )
print(marker)
print(pos)

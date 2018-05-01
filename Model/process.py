output_file = open("output.txt", "r")

for i in range(41):
	output_file.readline()

while 1:
	line = output_file.readline()
	if not line:
		break
	line = output_file.readline()
	words = line.split(' ')
	if len(words) == 1:
		print words[0]
		break
	val_acc = words[-1]
	val_loss = words[-4]
	acc = words[-7]
	loss = words[-10]
	print loss, acc, val_loss, val_acc

def fibonnaci(until):
	sequence = []
	next = 0
	for i in range(0,until):
		if sequence[i] != until:
			next = i + i+1
			sequence.append(next)
	return sequence
print(fibonnaci(5))


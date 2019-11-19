def abrir_csv(arquivo):
	with open(arquivo, 'r') as f:
	results = []
		for line in f:
			words = line.split(',')
			results.append((words[0], words[1:]))
	return results

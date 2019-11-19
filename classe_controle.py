def abrir_csv(arquivo):
	with open(arquivo, 'rt', encoding='latin-1') as f:
		results = []
		for linha in f:
			palavras = linha.split(';')
			results.append((palavras[0], palavras[1:]))

	return results

print(abrir_csv('./consulta_cand_2014/consulta_cand_2014_AC.csv'))
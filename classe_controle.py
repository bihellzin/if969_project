class Controle:
	def __init__(self, arquivo=None):
		self.arquivo = arquivo

	def abrir_csv(self):
		with open(self.arquivo, 'rt', encoding='latin-1') as f:
			results = []
			for linha in f:
				palavras = linha.split(';')
				results.append(palavras)

		return results

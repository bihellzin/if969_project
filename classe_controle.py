import time
from classe_candidato import *
from classe_lista import *


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

	def abrir_csv_novo(self):
		lista_candidatos = Lista()
		with open(self.arquivo, 'rt', encoding='latin-1') as f:
			results = []
			for linha in f:
				palavras = linha.split(';')
				results.append(palavras)

		for i in range(1, len(results)):
			candidato = Candidato()
			candidato.ano_eleicao = int(results[i][2][1:-1])
			candidato.sigla_uf = results[i][10][1:-1]
			candidato.codigo_cargo = int(results[i][13][1:-1])
			candidato.descricao_cargo = results[i][14][1:-1]
			candidato.nome = results[i][17][1:-1]
			candidato.id_candidato = int(results[i][15][1:-1])
			candidato.numero_urna = int(results[i][16][1:-1])
			candidato.cpf = int(results[i][20][1:-1])
			candidato.nome_urna = results[i][18][1:-1]
			candidato.numero_partido = int(results[i][27][1:-1])
			candidato.nome_partido = results[i][29][1:-1]
			candidato.sigla_partido = results[i][28][1:-1]
			candidato.codigo_ocupacao_candidato = int(results[i][49][1:-1])
			candidato.descricao_ocupacao = results[i][50][1:-1]
			candidato.data_nascimento = results[i][38][1:-1]
			candidato.sexo_candidato = results[i][42][1:-1]
			candidato.grau_instrucao = results[i][43][1:-1]
			candidato.estado_civil = results[i][46][1:-1]
			candidato.uf_nascimento = results[i][34][1:-1]
			candidato.nome_municipio_nascimento = results[i][37][1:-1]
			candidato.situacao_candidato_pos_pleito = results[i][53][1:-1]
			candidato.situacao_candidatura = results[i][53][1:-1]
			candidato.lista_bens = Lista()

			lista_candidatos.inserirOrdenado(No(candidato))
			#lista_candidatos.inserirComeco(No(candidato))
		return lista_candidatos


if __name__ == '__main__':
	inicio = time.time()
	candidatos = Controle('./consulta_cand_2014/consulta_cand_2014_BRASIL.csv').abrir_csv_novo()

	print(time.time() - inicio, 'segundos')
	print(candidatos[0].id_candidato)
	print(candidatos[2].id_candidato)
	print(candidatos[3].id_candidato)
	print(candidatos[4].id_candidato)
	print(candidatos[5].id_candidato)
	print(candidatos[6].id_candidato)
	print(candidatos[7].id_candidato)
	print(candidatos[8].id_candidato)
	print(candidatos[9].id_candidato)
	print(candidatos[10].id_candidato)

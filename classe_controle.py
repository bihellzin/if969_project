from classe_lista import *
from classe_candidato import *
from classe_lista_bem import *
from classe_bem import *


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
        lista_candidatos = ListaCandidato()
        with open(self.arquivo, 'rt', encoding='latin-1') as f:
            results = []
            for linha in f:
                palavras = linha.split(';')
                results.append(palavras)

        for i in range(1, 5):
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
            candidato.lista_bens = ListaBem()

            lista_candidatos.inserirComeco(NoCandidato(candidato))

        return lista_candidatos

    def abrir_csv_bens(self):
        lista_bens = ListaBem()
        with open(self.arquivo, 'rt', encoding='latin-1') as f:
            results = []
            for linha in f:
                palavras = linha.split(';')
                results.append(palavras)

        for i in range(1, len(results)):
            bem = Bem()
            bem.codigo_bem = int(results[i][13][1:-1])
            bem.descricao_tipo_bem = results[i][14][1:-1]
            bem.descricao_detalhada_bem = results[i][15][1:-1]
            bem.valor_bem = int(results[i][14][1:-1])

            lista_bens.inserirComeco(NoBem(bem))

        return lista_bens


def shellSort(array):
    n = len(array)
    gap = n // 2
    while gap > 0:

        for i in range(gap, n):
            temp = array[i]
            j = i
            while j >= gap and array[j - gap] < temp:
                array[j] = array[j - gap]
                j -= gap
            array[j] = temp
        gap //= 2

    return array


def algumaCoisa(lista):
    arr = []
    for i in lista:
        arr.append(i)

    return arr


def ListaCandidatosFinal():
    candidatos = Controle('./consulta_cand_2014/consulta_cand_2014_BRASIL.csv').abrir_csv_novo()
    arr = algumaCoisa(candidatos)
    arr = shellSort(arr)
    nova_lista = ListaCandidato()
    for i in arr:
        nova_lista.inserirComeco(NoCandidato(i))

    return nova_lista

import time
from classe_lista import *
from classe_candidato import *
from classe_lista_bem import *
from classe_bem import *


class Controle:
    def __init__(self):
        self.estados = ['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MS', 'MT', 'PA', 'PB', 'PE',
                        'PI', 'PR', 'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO']

    def abrir_csv(self, arquivo):
        with open(arquivo, 'rt', encoding='latin-1') as f:
            results = []
            for linha in f:
                palavras = linha.split(';')
                results.append(palavras)

        return results

    def abrir_csv_novo(self, arquivo):
        lista_candidatos = ListaCandidato()
        with open(arquivo, 'rt', encoding='latin-1') as f:
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

            lista_candidatos.inserirComeco(NoCandidato(candidato))

        return lista_candidatos

    def abrir_csv_bens(self, arquivo):
        colecaoBens = {}
        with open(arquivo, 'rt', encoding='latin-1') as f:
            for linha in f:
                palavras = linha.split(';')
                if '"DT_GERACAO"' not in palavras:
                    bem = Bem()
                    bem.codigo_bem = int(palavras[13][1:-1])
                    bem.descricao_tipo_bem = palavras[14][1:-1]
                    bem.descricao_detalhada_bem = palavras[15][1:-1]
                    bem.valor_bem = float(palavras[16][1:-4]) + float(palavras[16][-3:-1])/100
                    bem.id_candidato = int(palavras[11][1:-1])
                    if bem.id_candidato not in colecaoBens:
                        colecaoBens[bem.id_candidato] = ListaBem()
                        colecaoBens[bem.id_candidato].inserirComeco(NoBem(bem))

                    else:
                        colecaoBens[bem.id_candidato].inserirComeco(NoBem(bem))


        return colecaoBens


    def retornaCandidatosDeterminadaCaracteristica(self, caracteristica):
        lista_candidatos = ListaCandidato()
        with open('./consulta_cand_2014/consulta_cand_2014_BRASIL.csv', 'rt', encoding='latin-1') as f:
            results = []
            for linha in f:
                palavras = linha.split(';')
                results.append(palavras)

        for i in range(1, len(results)):
            if caracteristica in results[i]:
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

                lista_candidatos.inserirComeco(NoCandidato(candidato))

        return lista_candidatos


    def retornaCandidatosComBensMaiorQueN(self, valorDosBens):
        todosCandidatos = ListaFinal()
        nova_lista = ListaCandidato()

        for i in todosCandidatos:
            if i.lista_bens.total >= valorDosBens:
                nova_lista.inserirComeco(NoCandidato(i))

        return nova_lista


    def mostrarMediaPorCargo(self, cargo):
        todosCandidatos = ListaFinal()
        nova_lista = ListaCandidato()
        total = 0

        for i in todosCandidatos:
            if i.descricao_cargo == cargo:
                total += i.lista_bens.total

        return total/nova_lista.size


    def mostrarMediaPorUF(self, UF):
        todosCandidatos = ListaFinal()
        nova_lista = ListaCandidato()
        total = 0

        for i in todosCandidatos:
            if i.sigla_uf == UF:
                nova_lista.inserirComeco(NoCandidato(i))
                total += i.lista_bens.total

        return total/nova_lista.size


    def mostrarMediaPorPartido(self, partido):
        todosCandidatos = ListaFinal()
        nova_lista = ListaCandidato()
        total = 0

        for i in todosCandidatos:
            if i.sigla_partido == partido:
                nova_lista.inserirComeco(NoCandidato(i))
                total += i.lista_bens.total

        return total/nova_lista.size


    def mostrarMediaPorOcupacao(self, ocupacao):
        todosCandidatos = ListaFinal()
        nova_lista = ListaCandidato()
        total = 0

        for i in todosCandidatos:
            if i.descricao_ocupacao == ocupacao:
                nova_lista.inserirComeco(NoCandidato(i))
                total += i.lista_bens.total

        return total/nova_lista.size


    def mostrarMediaPorAnoNascimento(self, ano_nascimento):
        todosCandidatos = ListaFinal()
        nova_lista = ListaCandidato()
        total = 0

        for i in todosCandidatos:
            if int(i.data_nascimento[-4]) == ano_nascimento or i.data_nascimento[-4] == ano_nascimento:
                nova_lista.inserirComeco(NoCandidato(i))
                total += i.lista_bens.total

        return total/nova_lista.size


    def removerCandidatoComCaracteristica(self, caracteristica):
        lista_candidatos = ListaCandidato()
        with open('./consulta_cand_2014/consulta_cand_2014_BRASIL.csv', 'rt', encoding='latin-1') as f:
            results = []
            for linha in f:
                palavras = linha.split(';')
                results.append(palavras)

        for i in range(1, len(results)):
            if caracteristica in results[i]:
                continue
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

            lista_candidatos.inserirComeco(NoCandidato(candidato))

        return lista_candidatos


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


def shellSortBens(array):
    n = len(array)
    gap = n // 2
    while gap > 0:

        for i in range(gap, n):
            temp = array[i]
            j = i
            while j >= gap and array[j - gap].id_candidato < temp.id_candidato:
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
    candidatos = Controle().abrir_csv_novo('./consulta_cand_2014/consulta_cand_2014_BRASIL.csv')
    arr = algumaCoisa(candidatos)
    arr = shellSort(arr)
    nova_lista = ListaCandidato()
    for i in arr:
        nova_lista.inserirComeco(NoCandidato(i))

    return nova_lista


def ListaBensFinal():
    inicio = time.time()
    bens = Controle().abrir_csv_bens('./bem_candidato_2014/bem_candidato_2014_BRASIL.csv')
    arr = algumaCoisa(bens)
    arr = shellSortBens(arr)
    for i in bens:
        nova_lista.inserirComeco(NoBem(i))

    print(time.time() - inicio, 'segundos')

    return nova_lista


def ListaFinal():
    inicio = time.time()
    candidatos = ListaCandidatosFinal()
    bens = ListaBensFinal()

    for candidato in candidatos:

        for bem in bens:
            if candidato.id_candidato == bem.id_candidato:
                candidato.incluirBem(bem)
    print(time.time() - inicio)
    return candidatos


'''if __name__ == '__main__':
    a = ListaBensFinal()

    print(a.size)
    bens_desordenados = Controle().abrir_csv_bens('./bem_candidato_2014/bem_candidato_2014_BRASIL.csv')
    print(bens_desordenados.size)'''

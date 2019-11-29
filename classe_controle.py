from classe_lista import *
from classe_candidato import *
from classe_lista_bem import *
from classe_bem import *


class Controle:
    def __init__(self):
        self.estados = ['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MS', 'MT', 'PA', 'PB', 'PE',
                        'PI', 'PR', 'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO']

    def abrir_csv_candidatos(self, arquivo='./consulta_cand_2014/consulta_cand_2014_BRASIL.csv'):
        """
        Esse método retorna a lista de todos os candidatos que
        estão armazenados no arquivo consulta_cand_2014_BRASIL.csv
        """
        lista_candidatos = ListaCandidato()
        with open(arquivo, 'rt', encoding='latin-1') as f:
            for linha in f:
                palavras = linha.split(';')
                if '"DT_GERACAO"' in palavras:
                    continue

                candidato = Candidato()
                candidato.ano_eleicao = int(palavras[2][1:-1])
                candidato.sigla_uf = palavras[10][1:-1]
                candidato.codigo_cargo = int(palavras[13][1:-1])
                candidato.descricao_cargo = palavras[14][1:-1]
                candidato.nome = palavras[17][1:-1]
                candidato.id_candidato = int(palavras[15][1:-1])
                candidato.numero_urna = int(palavras[16][1:-1])
                candidato.cpf = int(palavras[20][1:-1])
                candidato.nome_urna = palavras[18][1:-1]
                candidato.numero_partido = int(palavras[27][1:-1])
                candidato.nome_partido = palavras[29][1:-1]
                candidato.sigla_partido = palavras[28][1:-1]
                candidato.codigo_ocupacao_candidato = int(palavras[49][1:-1])
                candidato.descricao_ocupacao = palavras[50][1:-1]
                candidato.data_nascimento = palavras[38][1:-1]
                candidato.sexo_candidato = palavras[42][1:-1]
                candidato.grau_instrucao = palavras[43][1:-1]
                candidato.estado_civil = palavras[46][1:-1]
                candidato.uf_nascimento = palavras[34][1:-1]
                candidato.nome_municipio_nascimento = palavras[37][1:-1]
                candidato.situacao_candidato_pos_pleito = palavras[53][1:-1]
                candidato.situacao_candidatura = palavras[53][1:-1]

                lista_candidatos.inserirComeco(NoCandidato(candidato))

        return lista_candidatos


    def abrir_csv_bens(self, arquivo='./bem_candidato_2014/bem_candidato_2014_BRASIL.csv'):
        """
        Esse método retorna um dicionário contendo os bens de todos os candidatos que
        estão armazenados num arquivo de ./bem_candidato_2014 e os coloca no atributo
        lista_bens de cada objeto Candidato
        """
        colecao_bens = {}
        with open(arquivo, 'rt', encoding='latin-1') as f:
            for linha in f:
                palavras = linha.split(';')
                """
                Ignorando o cabeçalho
                """
                if '"DT_GERACAO"' in palavras:
                    continue

                bem = Bem()
                bem.codigo_bem = int(palavras[13][1:-1])
                bem.descricao_tipo_bem = palavras[14][1:-1]
                bem.descricao_detalhada_bem = palavras[15][1:-1]
                bem.valor_bem = float(palavras[16][1:-4]) + float(palavras[16][-3:-1]) / 100
                bem.id_candidato = int(palavras[11][1:-1])

                if bem.id_candidato not in colecao_bens:
                    colecao_bens[bem.id_candidato] = ListaBem()
                    colecao_bens[bem.id_candidato].inserirComeco(NoBem(bem))

                else:
                    colecao_bens[bem.id_candidato].inserirComeco(NoBem(bem))

        lista_final = self.abrir_csv_candidatos()
        for candidato in lista_final:
            if candidato.id_candidato in colecao_bens:
                candidato.lista_bens = colecao_bens[candidato.id_candidato]

        return lista_final


def retornaCandidatosDeterminadaCaracteristica(lista, caracteristica):
    """
    Essa função retorna a lista de todos os candidatos que
    possuem alguma característica específica nos candidatos da lista
    """
    caracteristica = caracteristica.upper()
    nova_lista = ListaCandidato()

    for candidato in lista:
        if caracteristica in candidato.__dict__.values():
            nova_lista.inserirComeco(NoCandidato(candidato))

    exibirLista(nova_lista)

    return nova_lista


def retornaCandidatosComBensMaiorQueN(lista, valorDosBens):
    """
    Essa função retorna uma lista com os candidatos que possuem o total de bens
    superior a um determinado valor
    """
    nova_lista = ListaCandidato()

    for candidato in lista:
        if candidato.lista_bens.total >= valorDosBens:
            nova_lista.inserirComeco(NoCandidato(candidato))

    exibirLista(nova_lista)

    return nova_lista


def mostrarMediaPorCargo(lista, cargo):
    """
    Essa função retorna um valor que corresponde a média do total de bens
    dos candidatos que concorrem ao cargo especificado no argumento da função
    """
    cargo = cargo.upper()
    cont = 0
    total = 0

    for candidato in lista:
        if candidato.descricao_cargo == cargo:
            total += candidato.lista_bens.total
            cont += 1

    print(total / cont)

    return total / cont


def mostrarMediaPorUF(lista, sigla_UF):
    """
    Essa função retorna um valor que corresponde a média do total de bens
    dos candidatos do estado especificado no argumento da função
    """
    sigla_UF = sigla_UF.upper()
    while sigla_UF not in ['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MS', 'MT', 'PA', 'PB',
                           'PE', 'PI', 'PR', 'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO']:
        sigla_UF = input('Sigla de UF inválido\nDigite novamente\n').upper()

    cont = 0
    total = 0

    for candidato in lista:
        if candidato.sigla_uf == sigla_UF:
            total += candidato.lista_bens.total
            cont += 1

    return total / cont


def mostrarMediaPorPartido(lista, partido):
    """
    Essa função retorna um valor que corresponde a média do total de bens
    dos candidatos do partido especificado no argumento da função
    """
    partido = partido.upper()
    cont = 0
    total = 0

    for candidato in lista:
        if candidato.sigla_partido == partido or candidato.nome_partido == partido:
            total += candidato.lista_bens.total
            cont += 1

    print(total / cont)

    return total / cont


def mostrarMediaPorOcupacao(lista, ocupacao):
    """
    Essa função retorna um valor que corresponde a média do total de bens
    dos candidatos que possuem a ocupação especificado no argumento da função
    """
    ocupacao = ocupacao.upper()
    cont = 0
    total = 0

    for candidato in lista:
        if candidato.descricao_ocupacao == ocupacao:
            cont += 1
            total += candidato.lista_bens.total

    print(total / cont)

    return total / cont


def mostrarMediaPorAnoNascimento(lista, ano_nascimento):
    """
    Essa função retorna um valor que corresponde a média do total de bens
    dos candidatos que nasceram no mesmo ano
    """
    total = 0
    cont = 0

    for candidato in lista:
        if int(candidato.data_nascimento[-4:]) == ano_nascimento or candidato.data_nascimento[-4:] == ano_nascimento:
            total += candidato.lista_bens.total
            cont += 1

    print(total / cont)

    return total / cont


def removerCandidatoComCaracteristica(lista, caracteristica):
    """
    Essa função retorna a lista de todos os candidatos que
    possuem alguma característica específica nos candidatos da lista
    """
    caracteristica = caracteristica.upper()
    nova_lista = ListaCandidato()

    for candidato in lista:
        if caracteristica not in candidato.__dict__.values():
            nova_lista.inserirComeco(NoCandidato(candidato))

    exibirLista(nova_lista)

    return nova_lista


def exibirLista(lista):
    opcao = input('Gostaria de visualizar a lista com as modificações ?\nDigite "sim" ou "não"\n')
    while opcao.upper()[0] not in ('N', 'S', 'Y'):
        opcao = input('Gostaria de visualizar a lista com as modificações ?\nDigite "sim" ou "não"\n')

    if opcao.upper()[0] == 'N':
        return
    elif opcao.upper()[0] == 'Y' or opcao.upper()[0] == 'S':
        for candidato in lista:
            print('{}\n'.format(candidato))

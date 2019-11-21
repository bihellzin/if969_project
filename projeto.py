import time
from classe_candidato import *
from classe_bem import *
from classe_lista import *
from classe_controle import *

if __name__ == '__main__':
    lista_candidatos = Lista()
    arquivo_candidatos = Controle('./consulta_cand_2014/consulta_cand_2014_BRASIL.csv')
    inicio = time.time()
    info_candidato = arquivo_candidatos.abrir_csv()
    fim = time.time()
    print(fim-inicio, 'segundos')

    inicio = time.time()
    for i in range(1, len(info_candidato)):
        candidato = Candidato()
        candidato.ano_eleicao = info_candidato[i][2][1:-1]
        candidato.sigla_uf = info_candidato[i][10][1:-1]
        candidato.codigo_cargo = info_candidato[i][13][1:-1]
        candidato.descricao_cargo = info_candidato[i][14][1:-1]
        candidato.nome = info_candidato[i][17][1:-1]
        candidato.id_candidato = info_candidato[i][15][1:-1]
        candidato.numero_urna = info_candidato[i][16][1:-1]
        candidato.cpf = info_candidato[i][20][1:-1]
        candidato.nome_urna = info_candidato[i][18][1:-1]
        candidato.numero_partido = info_candidato[i][27][1:-1]
        candidato.nome_partido = info_candidato[i][29][1:-1]
        candidato.sigla_partido = info_candidato[i][28][1:-1]
        candidato.codigo_ocupacao_candidato = info_candidato[i][48][1:-1]
        candidato.descricao_ocupacao = info_candidato[i][49][1:-1]
        candidato.data_nascimento = info_candidato[i][37][1:-1]
        candidato.sexo_candidato = info_candidato[i][41][1:-1]
        candidato.grau_instrucao = info_candidato[i][43][1:-1]
        candidato.estado_civil = info_candidato[i][45][1:-1]
        candidato.uf_nascimento = info_candidato[i][34][1:-1]
        candidato.nome_municipio_nascimento = info_candidato[i][36][1:-1]
        candidato.situacao_candidato_pos_pleito = info_candidato[i][52][1:-1]
        candidato.situacao_candidatura = info_candidato[i][52][1:-1]
        candidato.lista_bens = Lista()

        lista_candidatos.anexar(No(candidato))

    fim = time.time()
    print(fim - inicio, 'segundos')
    input('continuar ?\n')
    for i in range(lista_candidatos.size):
        print(lista_candidatos[i].nome)

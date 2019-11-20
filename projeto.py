from classe_candidato import *
from classe_bem import *
from classe_lista import *
from classe_controle import *

if __name__ == '__main__':
    lista_candidatos = Lista()
    arquivo_candidatos = Controle('./consulta_cand_2014/consulta_cand_2014_BRASIL.csv')
    info_candidato = arquivo_candidatos.abrir_csv()

    for i in range(1, len(info_candidato)):
        candidato = Candidato()
        candidato.ano_eleicao = info_candidato[i][2]
        candidato.sigla_uf = info_candidato[i][10]
        candidato.codigo_cargo = info_candidato[i][13]
        candidato.descricao_cargo = info_candidato[i][14]
        candidato.nome = info_candidato[i][17]
        candidato.id_candidato = info_candidato[i][15]
        candidato.numero_urna = info_candidato[i][16]
        candidato.cpf = info_candidato[i][20]
        candidato.nome_urna = info_candidato[i][18]
        candidato.numero_partido = info_candidato[i][27]
        candidato.nome_partido = info_candidato[i][29]
        candidato.sigla_partido = info_candidato[i][28]
        candidato.codigo_ocupacao_candidato = info_candidato[i][48]
        candidato.descricao_ocupacao = info_candidato[i][49]
        candidato.data_nascimento = info_candidato[i][37]
        candidato.sexo_candidato = info_candidato[i][41]
        candidato.grau_instrucao = info_candidato[i][43]
        candidato.estado_civil = info_candidato[i][45]
        candidato.uf_nascimento = info_candidato[i][34]
        candidato.nome_municipio_nascimento = info_candidato[i][36]
        candidato.situacao_candidato_pos_pleito = info_candidato[i][52]
        candidato.situacao_candidatura = info_candidato[i][52]
        candidato.lista_bens = Lista()

        lista_candidatos.anexar(No(candidato))

    for i in range(lista_candidatos.size):
        print(lista_candidatos[i].nome)

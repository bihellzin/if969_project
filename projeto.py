from classe_controle import *

if __name__ == '__main__':
    todosCandidatos = ListaCandidatosFinal()

    todosCandidatos.root.candidato.lista_bens.total = 1000

    for i in candidatosNascimentoCrescente(todosCandidatos):
        print(i.data_nascimento)
        print('\n')

    print('\n###################################################################')

    for i in candidatosNascimentoDecrescente(todosCandidatos):
        print(i.data_nascimento)
        print('\n')

    print('\n###################################################################')


    for i in candidatosOrdemAlfabeticaCrescente(todosCandidatos):
        print(i.nome)
        print('\n')

    print('\n###################################################################')

    for i in candidatosOrdemAlfabeticaDecrescente(todosCandidatos):
        print(i.nome)
        print('\n')

    print('\n###################################################################')

    for i in candidatosPartidoCrescente(todosCandidatos):
        print(i.nome_partido)
        print('\n')

    print('\n###################################################################')

    for i in candidatosPartidoDecrescente(todosCandidatos):
        print(i.nome_partido)
        print('\n')

    for i in candidatosTotalBensCrescente(todosCandidatos):
        print(i.lista_bens.total)
        print('\n')
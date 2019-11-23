# import time
# from classe_candidato import *
# from classe_bem import *
from classe_lista import *
from classe_controle import *

if __name__ == '__main__':
    todosCandidatos = ListaCandidatosFinal()

    print(candidatosNascimentoCrescente(todosCandidatos))
    print('\n')

    print(candidatosNascimentoDecrescente(todosCandidatos))
    print('\n')

    print(candidatosOrdemAlfabeticaCrescente(todosCandidatos))
    print('\n')

    print(candidatosOrdemAlfabeticaDecrescente(todosCandidatos))
    print('\n')

    print(candidatosPartidoCrescente(todosCandidatos))
    print('\n')

    print(candidatosPartidoDecrescente(todosCandidatos))
    print('\n')

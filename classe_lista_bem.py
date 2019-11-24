class NoBem:
    def __init__(self, bem=None, prox=None, ante=None):
        self.bem = bem
        self.prox = prox
        self.ante = ante


class ListaBem:

    def __init__(self, objeto_iteravel=None):
        self.root = None
        self.size = 0
        self.total = 0
        if objeto_iteravel is not None:
            self.objeto_iteravel = objeto_iteravel
            for i in objeto_iteravel:
                node = NoBem(i)
                self.anexar(node)
            self.size = len(objeto_iteravel)

    def __str__(self):
        if self.size > 0:
            nos = ''

            ultimoNo = self.root
            while True:
                if ultimoNo.prox is None:
                    nos += str(ultimoNo.bem)
                    break
                else:
                    nos += str(ultimoNo.bem) + ', '
                ultimoNo = ultimoNo.prox

            return nos

        else:
            return 'Lista vazia'

    def __repr__(self):
        if self.listaVazia():
            return 'Lista()'

        retorno = 'Lista(['
        ultimo = self.root
        while True:
            if ultimo.prox is None:
                retorno += str(ultimo.bem) + '])'
                return retorno
            retorno += str(ultimo.bem) + ', '
            ultimo = ultimo.prox

    def __getitem__(self, indice):
        try:
            if indice >= self.size:
                raise IndexError
            else:
                inicio = 0
                procurado = self.root
                while inicio < indice:
                    procurado = procurado.prox
                    inicio += 1
                return procurado.bem
        except IndexError:
            print('ERRO !\nVocê inseriu um índice maior que a quantidade de itens da lista')

    def __setitem__(self, indice, value):
        try:
            if indice >= self.size:
                raise IndexError
            else:
                inicio = 0
                procurado = self.root
                while inicio < indice:
                    procurado = procurado.prox
                    inicio += 1
                procurado.bem = value

        except IndexError:
            print('ERRO !\nVocê inseriu um índice maior que a quantidade de itens da lista')

    def __iter__(self):
        class Ponteiro:
            def __init__(self, lista, passo=0):
                self.passo = passo
                self.lista = lista

            def __next__(self):
                if self.passo >= self.lista.size:
                    raise StopIteration
                value = self.lista[self.passo]
                self.passo += 1

                return value

        return Ponteiro(self)

    def listaVazia(self):
        if self.size:
            return False
        return True

    def anexar(self, novoNo):
        if self.listaVazia():
            self.root = novoNo
            self.root.prox = None

        else:
            if type(novoNo) is str or type(novoNo) is int or type(novoNo) is dict or type(novoNo) is list or type(
                    novoNo) is tuple:
                novoNo = NoBem(novoNo)
            ultimoNo = self.root
            while ultimoNo.prox is not None:
                ultimoNo = ultimoNo.prox
            ultimoNo.prox = novoNo
            novoNo.ante = ultimoNo
            novoNo.prox = None
        self.size += 1

    def indice(self, value):
        try:
            encontrou = False
            inicio = 0
            procurado = self.root
            while inicio < self.size:
                if value == procurado.bem:
                    return inicio
                procurado = procurado.prox
                inicio += 1
            if not encontrou:
                raise ValueError

        except ValueError:
            print('ERRO !\nVocê inseriu um valor que não existe')

    def selecionar(self, indice):
        if indice >= self.size:
            print('Índice maior que a quantidade de índices da lista')
        else:
            if indice == 0:
                item = self.root.bem
                self.root = self.root.prox
                self.root.ante = None
            else:
                inicio = 0
                achado = self.root
                proximo = achado.prox
                while inicio < indice:
                    achado = proximo
                    proximo = achado.prox
                    inicio += 1
                item = achado.bem
                achado.ante.prox = proximo
                proximo.ante = achado.ante
            self.size -= 1
            return item

    def inserirComeco(self, novoNo):
        if self.listaVazia():
            self.root = novoNo

        else:
            temp = self.root
            self.root = novoNo
            self.root.prox = temp
            self.root.prox.ante = self.root

        self.size += 1

    def inserir(self, indice, valor):
        if indice > self.size:
            print('índice não pode ser inserido na lista')
            return

        if self.listaVazia():
            valor = NoBem(valor)
            self.root = valor
            self.root.prox = None

        else:
            inicio = 0
            if type(valor) is str or type(valor) is int or type(valor) is dict or type(valor) is list or type(
                    valor) is tuple:
                valor = NoBem(valor)

            if indice == 0:
                temp = self.root
                self.root = valor
                self.root.prox = temp
                temp.ante = self.root
            else:
                achado = self.root
                proximo = achado.prox
                while inicio < indice:
                    achado = proximo
                    proximo = achado.prox
                    inicio += 1
                temp = achado.ante
                valor.ante = temp
                achado.ante.prox = valor
                achado.ante = valor
                valor.prox = achado
        self.size += 1

    def inserirOrdenado(self, novoNo):
        if self.listaVazia() and isinstance(novoNo, NoBem):
            self.root = novoNo

        else:
            no = self.root
            if isinstance(novoNo, NoBem):
                if novoNo.bem.valor_bem > no.bem.valor_bem:
                    while novoNo.bem.valor_bem > no.bem.valor_bem and no.prox is not None:
                        no = no.prox

                    if novoNo.bem.valor_bem < no.bem.valor_bem:
                        no = no.ante

                    if no.prox is None:
                        no.prox = novoNo
                        novoNo.ante = no

                    else:
                        temp = no.prox
                        no.prox.ante = novoNo
                        novoNo.prox = temp
                        novoNo.ante = no
                        no.prox = novoNo


                else:
                    while novoNo.bem.valor_bem < no.bem.valor_bem and no.ante is not None:
                        no = no.ante

                    if no is self.root:
                        self.inserirComeco(novoNo)

                    else:
                        temp = no.ante
                        no.ante.prox = novoNo
                        novoNo.ante = temp
                        novoNo.prox = no
                        no.ante = novoNo


            else:
                return False
        self.size += 1

    def concatenar(self, lista):
        ultimoLista = lista.root
        while ultimoLista.prox is not None:
            self.anexar(lista.selecionar(0))
            ultimoLista = ultimoLista.prox
        self.anexar(lista.selecionar(0))

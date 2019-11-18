class Candidato:
    def __init__(self):
        self._ano_eleicao = None
        self._sigla_uf = None
        self._codigo_cargo = None
        self._descricao_cargo = None
        self._nome = None
        self._id_candidato = None
        self._numero_urna = None
        self._cpf = None
        self._nome_urna = None
        self._numero_partido = None
        self._nome_partido = None
        self._sigla_partido = None
        self._codigo_ocupacao_candidato = None
        self._descricao_ocupacao = None
        self._data_nascimento = None
        self._sexo_candidato = None
        self._grau_instrucao = None
        self._estado_civil = None
        self._uf_nascimento = None
        self._nome_municipio_nascimento = None
        self._situacao_candidato_pos_pleito = None
        self._situacao_candidatura = None
        self._lista_bens = None

    @property
    def ano_eleicao(self):
        return self._ano_eleicao

    @ano_eleicao.setter
    def ano_eleicao(self, ano):
        self._ano_eleicao = ano

    @property
    def sigla_uf(self):
        return self._sigla_uf

    @sigla_uf.setter
    def sigla_uf(self, sigla):
        self._sigla_uf = sigla

    @property
    def codigo_cargo(self):
        return self._codigo_cargo

    @codigo_cargo.setter
    def codigo_cargo(self, codigo):
        self._codigo_cargo = codigo

    @property
    def descricao_cargo(self):
        return self._descricao_cargo

    @descricao_cargo.setter
    def descricao_cargo(self, descricao):
        self._descricao_cargo = descricao

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome_candidato):
        self._nome = nome_candidato

    @property
    def id_candidato(self):
        return self._id_candidato

    @id_candidato.setter
    def id_candidato(self, id_do_candidato):
        self._id_candidato = id_do_candidato

    @property
    def numero_urna(self):
        return self._numero_urna

    @numero_urna.setter
    def numero_urna(self, num_urna):
        self._numero_urna = num_urna

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf_candidato):
        self._cpf = cpf_candidato

    @property
    def nome_urna(self):
        return self._nome_urna

    @nome_urna.setter
    def nome_urna(self, nome):
        self._nome_urna = nome

    @property
    def numero_partido(self):
        return self._numero_partido

    @numero_partido.setter
    def numero_partido(self, numero):
        self._numero_partido = numero

    @property
    def nome_partido(self):
        return self._nome_partido

    @nome_partido.setter
    def nome_partido(self, nome):
        self._nome_partido = nome

    @property
    def sigla_partido(self):
        return self._sigla_partido

    @sigla_partido.setter
    def sigla_partido(self, sigla):
        self._sigla_partido = sigla

    @property
    def codigo_ocupacao_candidato(self):
        return self._codigo_ocupacao_candidato

    @codigo_ocupacao_candidato.setter
    def codigo_ocupacao_candidato(self, codigo):
        self._codigo_ocupacao_candidato = codigo

    @property
    def descricao_ocupacao(self):
        return self._descricao_ocupacao

    @descricao_ocupacao.setter
    def descricao_ocupacao(self, descricao):
        self._descricao_ocupacao = descricao

    @property
    def data_nascimento(self):
        return self._data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data):
        self._data_nascimento = data

    @property
    def sexo_candidato(self):
        return self._sexo_candidato

    @sexo_candidato.setter
    def sexo_candidato(self, sexo):
        self._sexo_candidato = sexo

    @property
    def grau_instrucao(self):
        return self._grau_instrucao

    @grau_instrucao.setter
    def grau_instrucao(self, grau):
        self._grau_instrucao = grau

    @property
    def estado_civil(self):
        return self._estado_civil

    @estado_civil.setter
    def estado_civil(self, estado):
        self._estado_civil = estado

    @property
    def uf_nascimento(self):
        return self._uf_nascimento

    @uf_nascimento.setter
    def uf_nascimento(self, uf):
        self._uf_nascimento = uf

    @property
    def nome_municipio_nascimento(self):
        return self._nome_municipio_nascimento

    @nome_municipio_nascimento.setter
    def nome_municipio_nascimento(self, nome):
        self._nome_municipio_nascimento = nome

    @property
    def situacao_candidato_pos_pleito(self):
        return self._situacao_candidato_pos_pleito

    @situacao_candidato_pos_pleito.setter
    def situacao_candidato_pos_pleito(self, situacao):
        self._situacao_candidato_pos_pleito = situacao

    @property
    def situacao_candidatura(self):
        return self._situacao_candidatura

    @situacao_candidatura.setter
    def situacao_candidatura(self, situacao):
        self._situacao_candidatura = situacao

    @property
    def lista_bens(self):
        return self._lista_bens

    @lista_bens.setter
    def lista_bens(self, lista):
        self._lista_bens = lista

    def incluirBem(self, objeto_bem):
        pass

    def __str__(self):
        saida = '{} -- {} -- {}\n{} ({}) {} ({})\nResumo dos bens:\n  - Total declarado: R${}\n  - Total por tipo de ' \
                'bem '

        return saida

    def __repr__(self):
        pass

    def __eq__(self, outro_candidato):
        if self._nome == outro_candidato._nome:
            if self._cpf == outro_candidato._cpf:
                return True

            else:
                return False
        else:
            return False

    def listar_bens(self):
        pass


class Bem:

    def __init__(self):
        self._codigo_bem = None
        self._descricao_tipo_bem = None
        self._descricao_detalhada_bem = None
        self._valor_bem = None

    @property
    def codigo_bem(self):
        return self._codigo_bem

    @codigo_bem.setter
    def codigo_bem(self, codigo):
        self._codigo_bem = codigo

    @property
    def descricao_tipo_bem(self):
        return self._descricao_tipo_bem

    @descricao_tipo_bem.setter
    def descricao_tipo_bem(self, descricao):
        self._descricao_tipo_bem = descricao

    @property
    def descricao_detalhada_bem(self):
        return self._descricao_detalhada_bem

    @descricao_detalhada_bem.setter
    def descricao_detalhada_bem(self, descricao):
        self._descricao_detalhada_bem = descricao

    @property
    def valor_bem(self):
        return self._valor_bem

    @valor_bem.setter
    def valor_bem(self, valor):
        self._valor_bem = valor

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def __eq__(self, outro_bem):
        if self._codigo_bem == outro_bem._codigo_bem:
            if outro_bem._descricao_detalhata_bem == self._descricao_detalhada_bem:
                return True

            else:
                return False
        else:
            return False


class No:
    def __init__(self, data=None, prox=None, ante=None):
        self.data = data
        self.prox = prox
        self.ante = ante


class Lista:

    def __init__(self, objeto_iteravel=None):
        self.root = None
        self.size = 0
        if objeto_iteravel is not None:
            self.objeto_iteravel = objeto_iteravel
            for i in objeto_iteravel:
                node = No(i)
                self.anexar(node)
            self.size = len(objeto_iteravel)

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
                novoNo = No(novoNo)
            ultimoNo = self.root
            while ultimoNo.prox is not None:
                ultimoNo = ultimoNo.prox
            ultimoNo.prox = novoNo
            novoNo.ante = ultimoNo
            novoNo.prox = None
        self.size += 1

    def __str__(self):
        if self.size > 0:
            nos = ''

            ultimoNo = self.root
            while True:
                if ultimoNo.prox is None:
                    nos += str(ultimoNo.data)
                    break
                else:
                    nos += str(ultimoNo.data) + ', '
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
                retorno += str(ultimo.data) + '])'
                return retorno
            retorno += str(ultimo.data) + ', '
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
                return procurado.data
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
                procurado.data = value

        except IndexError:
            print('ERRO !\nVocê inseriu um índice maior que a quantidade de itens da lista')

    def indice(self, value):
        try:
            encontrou = False
            inicio = 0
            procurado = self.root
            while inicio < self.size:
                if value == procurado.data:
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
                item = self.root.data
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
                item = achado.data
                achado.ante.prox = proximo
                proximo.ante = achado.ante
            self.size -= 1
            return item

    def inserir(self, indice, valor):
        if indice > self.size:
            print('índice não pode ser inserido na lista')
            return

        if self.listaVazia():
            valor = No(valor)
            self.root = valor
            self.root.prox = None

        else:
            inicio = 0
            if type(valor) is str or type(valor) is int or type(valor) is dict or type(valor) is list or type(
                    valor) is tuple:
                valor = No(valor)

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

    def concatenar(self, lista):
        ultimoLista = lista.root
        while ultimoLista.prox is not None:
            self.anexar(lista.selecionar(0))
            ultimoLista = ultimoLista.prox
        self.anexar(lista.selecionar(0))

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

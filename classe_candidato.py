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
                'bem '.format(self.nome_urna, self.numero_urna, self.sigla_partido, self.descricao_cargo, self.sigla_uf,
                              self.nome_municipio_nascimento, self.uf_nascimento, self.lista_bens)

        return saida

    def __repr__(self):
        saida = '{} -- {} -- {}\n{} ({}) {} ({})\nResumo dos bens:\n  - Total declarado: R${}\n  - Total por tipo de ' \
                'bem '.format(self.nome_urna, self.numero_urna, self.sigla_partido, self.descricao_cargo, self.sigla_uf,
                              self.nome_municipio_nascimento, self.uf_nascimento, self.lista_bens)

        return saida

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

    def __gt__(self, other):
        return self.id_candidato > other.id_candidato

    def __lt__(self, other):
        return self.id_candidato < other.id_candidato

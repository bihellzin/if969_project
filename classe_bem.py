class Bem:
    """
    Classe do objeto Bem com alguns atributos
    """
    def __init__(self):
        self._codigo_bem = None
        self._descricao_tipo_bem = None
        self._descricao_detalhada_bem = None
        self._valor_bem = None
        self._id_candidato = None

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

    @property
    def id_candidato(self):
        return self._id_candidato

    @id_candidato.setter
    def id_candidato(self, value):
        self._id_candidato = value

    def __str__(self):
        if len(self.descricao_detalhada_bem) <= 80:
            saida = '{} -- {} -- R$ {} Descrição: {}'.format(self.codigo_bem, self.descricao_tipo_bem, self.valor_bem,
                                                              self.descricao_detalhada_bem)

        else:
            descricao_final = ''
            contagem_letras = 0
            for i in self.descricao_detalhada_bem:
                if contagem_letras == 80:
                    descricao_final += '\n'
                    contagem_letras = 0

                descricao_final += i
                contagem_letras += 1
            saida = '{} -- {} -- R$ {} Descrição: {}'.format(self.codigo_bem, self.descricao_tipo_bem, self.valor_bem,
                                                              descricao_final)

        return saida

    def __repr__(self):
        if len(self.descricao_detalhada_bem) <= 80:
            saida = '{} -- {} -- R$ {} Descrição: {}'.format(self.codigo_bem, self.descricao_tipo_bem, self.valor_bem,
                                                              self.descricao_detalhada_bem)

        else:
            descricao_final = ''
            contagem_letras = 0
            for i in self.descricao_detalhada_bem:
                if contagem_letras == 80:
                    descricao_final += '\n'
                    contagem_letras = 0

                descricao_final += i
                contagem_letras += 1
            saida = '{} -- {} -- R$ {}\nDescrição: {}'.format(self.codigo_bem, self.descricao_tipo_bem, self.valor_bem,
                                                              descricao_final)

        return saida

    def __eq__(self, outro_bem):
        if self.codigo_bem == outro_bem.codigo_bem:
            if outro_bem.descricao_detalhata_bem == self.descricao_detalhada_bem:
                return True

            else:
                return False
        else:
            return False

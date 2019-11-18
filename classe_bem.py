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

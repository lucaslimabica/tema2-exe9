"""
@date 22 de Fevereiro de 2024
@author lucaslimabica
"""


class Pessoa:
    def __init__(
        self, nome: str, apelido: str, cc: str, morada: str, telemovel: str
    ) -> None:
        self.__nome = nome
        self.__apelido = apelido
        self.__cc = cc
        self.__morada = morada
        self.__telemovel = telemovel

    @property
    def nome(self):
        """Acessa e retorna o primeiro nome da pessoa"""
        # print("Getter: nome acessado")
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        """Altera o primeiro nome da pessoa"""
        # print(f"Setter: nome alterado para {novo_nome}")
        self.__nome = novo_nome

    @property
    def apelido(self):
        """Acessa e retorna no sobrenome/apelido da pessoa"""
        # print("Getter: nome acessado")
        return self.__apelido

    @apelido.setter
    def apelido(self, novo_apelido):
        """Altera o sobrenome/apelido da pessoa"""
        # print(f"Setter: o apelido foi alterado para {novo_apelido}")
        self.__apelido = novo_apelido

    @property
    def cc(self):
        """Acessa e retona o CC da pessoa"""
        # print("Getter: CC acessado")
        return self.__cc

    @cc.setter
    def cc(self, novo_cc):
        """Altera o CC da pessoa"""
        # print(f"Setter: CC alterado para {novo_cc}")
        self.__cc = novo_cc

    @property
    def morada(self):
        """Acessa e retorna a morada da pessoa"""
        # print("Getter: morada acessada")
        return self.__morada

    @morada.setter
    def morada(self, nova_morada):
        """Altera a morada da pessoa"""
        # print(f"Setter: Morada alterada para {nova_morada}")
        self.__morada = nova_morada

    @property
    def telemovel(self):
        """Acessa e retorna o telemovel pessoa"""
        # print("Getter: Telemovel acessado")
        return self.__telemovel

    @telemovel.setter
    def telemovel(self, novo_telemovel):
        """Altera o telemovel da pessoa"""
        # print(f"Setter: Telemovel alterado para {novo_telemovel}")
        self.__telemovel = novo_telemovel


if __name__ == "__main__":
    p1 = Pessoa(
        "Lucas",
        "Bica",
        "007",
        "Manuel da Costa Sousa, 2 Mata Lobos",
        "+351 928 115 788",
    )

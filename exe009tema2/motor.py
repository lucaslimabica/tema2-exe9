"""
@date 19 de Fevereiro de 2024
@author lucaslimabica
"""


class Motor:
    def __init__(
        self,
        combustivel: str,
        cavalos: float,
        torque: float,
        cilindros: int,
        cilindradas: float,
        peso: float,
        montadora: str,
        cambio: str = "Manual",
    ):
        self.__combustivel = combustivel
        self.__cavalos = cavalos
        self.__torque = torque
        self.__cilindros = cilindros
        self.__cilindradas = cilindradas
        self.__cambio = cambio
        self.__peso = peso
        self.__montadora = montadora

    @property
    def combustivel(self):
        """Retorna o tipo de combustível do motor"""
        # print("Getter: Combustível acessado")
        return self.__combustivel

    @combustivel.setter
    def combustivel(self, novo_combustivel):
        """Altera o combustível do motor"""
        # print(f"Setter: Combustível alterado para {novo_combustivel}")
        self.__combustivel = novo_combustivel

    @property
    def cavalos(self):
        """Retorna a quantidade de cavalos do motor"""
        # print("Getter: Qntd de Cavalos acessado")
        return self.__cavalos

    @cavalos.setter
    def cavalos(self, novo_cavalos):
        """Altera a quantidade de cavalos do motor"""
        # print(f"Setter: Qntd de Cavalos alterado para {novo_cavalos}")
        self.__cavalos = novo_cavalos

    @property
    def torque(self):
        """Retorna o toque do motor"""
        # print("Getter: Torque acessado")
        return self.__torque

    @torque.setter
    def torque(self, novo_torque):
        """Altera o toque do motor"""
        # print(f"Setter: Toque alterado para {novo_torque}")
        self.__torque = novo_torque

    @property
    def cilindros(self):
        """Retorna os cilindros do motor"""
        # print("Getter: cilindros acessado")
        return self.__cilindros

    @cilindros.setter
    def cilindros(self, novo_cilindros):
        """Altera os cilindros do motor"""
        # print(f"Setter: Toque alterado para {novo_cilindros}")
        self.__cilindros = novo_cilindros

    @property
    def cilindradas(self):
        """Retorna as cilindradas do motor"""
        # print("Getter: Cilindradas acessado")
        return self.__cilindradas

    @cilindradas.setter
    def cilindradas(self, novo_cilindradas):
        """Altera as cilindradas do motor"""
        # print(f"Setter: Cilindradas alterado para {novo_cilindradas}")
        self.__cilindradas = novo_cilindradas

    @property
    def peso(self):
        """Retorna as cilindradas do motor"""
        # print("Getter: Peso acessado")
        return self.__peso

    @peso.setter
    def peso(self, novo_peso):
        """Altera o peso do motor"""
        # print(f"Setter: Peso alterado para {novo_peso}")
        self.__peso = novo_peso

    @property
    def cambio(self):
        """Retorna o câmbio do motor"""
        # print("Getter: Câmbio acessado")
        return self.__cambio

    @cambio.setter
    def cambio(self, novo_cambio):
        """Altera o câmbio do motor"""
        # print(f"Setter: Câmbio alterado para {novo_cambio}")
        self.__cambio = novo_cambio

    @property
    def montadora(self):
        """Retorna a montadora do motor"""
        # print("Getter: Montadora acessado")
        return self.__montadora

    @montadora.setter
    def montadora(self, novo_montadora):
        """Altera a montadora do motor"""
        # print(f"Setter: Montadora alterado para {novo_montadora}")
        self.__montadora = novo_montadora


if __name__ == "__main__":
    e = Motor("Gasoleo", 245.3, 22, 6, 550, 400, "Fiat")

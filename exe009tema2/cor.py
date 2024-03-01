"""
@date 19 de Fevereiro de 2024
@author lucaslimabica
"""


class Cor:
    def __init__(self, nome_cor: str, r: int, g: int, b: int):
        self.__nome_cor = nome_cor
        self.__rgb = [r, g, b]

    @property
    def nome_cor(self):
        """Retorna o nome da cor"""
        # print("Getter: nome_cor acessado")
        return self.__nome_cor

    @nome_cor.setter
    def nome_cor(self, novo_nome: str):
        """Altera o nome da cor"""
        # print(f"O nome da cor fora aleterado para: {novo_nome}")
        self.__nome_cor = novo_nome

    @property
    def rgb(self):
        """Retorna o código RGB da cor"""
        # print("Getter: RGB acessado")
        return self.__rgb

    @rgb.setter
    def rgb(self, nrgb):
        """Forneça uma nova lista para substituir o código RGB da cor"""
        # print(f"O código da cor fora aleterado para: {nrgb}")
        self.__rgb = nrgb


if __name__ == "__main__":
    c = Cor("Azul", 250, 0, 4)

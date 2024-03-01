"""
@date 22 de Fevereiro de 2024
@author lucaslimabica
"""

from cor import Cor
from motor import Motor
from pessoa import Pessoa


class Carro:
    contagem = 0

    def __init__(
        self,
        dono: Pessoa,
        cor: Cor,
        motor: Motor,
        marca: str,
        modelo: str,
        consumo: float,
        kms: float,
    ):
        self.__dono = dono
        self.__cor = cor
        self.__motor = motor
        self.__marca = marca
        self.__modelo = modelo
        self.__consumo = consumo
        self.__kms = kms

        self.__class__.contagem += 1

    @property
    def dono(self):
        """Acessa e retorna o dono do carro"""
        # print("Getter: Dono acessado")
        return self.__dono

    @dono.setter
    def dono(self, novo_dono):
        """Altera o dono do carro"""
        assert isinstance(novo_dono, Pessoa)
        # print(f"Setter: Dono foi alterado para {novo_dono.nome}")
        self.__dono = novo_dono

    @property
    def motor(self):
        """Acessa e retorna o motor do carro"""
        # print("Getter: Motor acessado")
        return self.__motor

    @motor.setter
    def motor(self, novo_motor):
        """Altera o Motor do carro"""
        assert isinstance(novo_motor, Motor)
        # print(
        # f"Setter: o Motor fora aletarado foi alterado para um motor de {novo_motor.cavalos} cavalos"
        # )
        self.__motor = novo_motor

    @property
    def cor(self):
        """Acessa e retona a Cor do carro"""
        # print("Getter: Cor acessado")
        return self.__cor

    @cor.setter
    def cor(self, nova_cor):
        """Altera a Cor do carro"""
        assert isinstance(nova_cor, Cor)
        # print(f"Setter: Cor alterado para {nova_cor.nome_cor}")
        self.__cor = nova_cor

    @property
    def modelo(self):
        """Acessa e retorna o Modelo do carro"""
        # print("Getter: Modelo acessado")
        return self.__modelo

    @modelo.setter
    def modelo(self, novo_modelo):
        """Altera o Modelo do carro"""
        # print(f"Setter: Modelo alterado para {novo_modelo}")
        self.__modelo = novo_modelo

    @property
    def marca(self):
        """Acessa e retorna a Marca do carro"""
        # print("Getter: Marca acessada")
        return self.__marca

    @marca.setter
    def marca(self, nova_marca):
        """Altera a Marca do carro"""
        # print(f"Setter: Marca alterada para {nova_marca}")
        self.__marca = nova_marca

    @property
    def consumo(self):
        """Acessa e retorna o Consumo por litro do carro"""
        # print("Getter: Consumo acessado")
        return self.__consumo

    @consumo.setter
    def consumo(self, novo_consumo):
        """Altera o Consumo do carro"""
        # print(f"Setter: Consumo alterado para {novo_consumo}")
        self.__consumo = novo_consumo

    @property
    def kms(self):
        """Acessa e retorna a quilometragem do carro"""
        # print("Getter: Quilometragem acessado")
        return self.__kms

    @kms.setter
    def kms(self, novo_kms):
        """Altera a Quilometragem do carro"""
        # print(f"Setter: Quilometragem alterada para {novo_kms}")
        self.__kms = novo_kms


if __name__ == "__main__":
    p = Pessoa("Lucas", "Bica", "5555555", "Faro", "928")
    e = Motor("Gasoleo", 245.3, 22, 6, 550, 400, "Fiat")
    cor = Cor("Cinza", 255, 0, 10)
    c = Carro(p, cor, e, "Fiat", "Punto", 8.5, 6000)

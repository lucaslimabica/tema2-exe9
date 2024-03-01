from carro import Carro
from pessoa import Pessoa
from motor import Motor
from cor import Cor
from pyfiglet import figlet_format
import pickle

lista_carros = []
lista_pessoas = []
lista_motores = []
lista_cores = []


def main():
    global lista_carros
    global lista_pessoas
    global lista_motores
    global lista_cores

    while True:
        menu = figlet_format("FF Cars\n")
        print(menu)
        print("--- | Opções | ---")
        print("C1 - Lista de Carros", end="    ")
        print("C2 - Criar novo Carro")
        print("C3 - Editar Carro", end="       ")
        print("C4 - Apagar Carro")
        print("P1 - Lista de Pessoas", end="   ")
        print("P2 - Criar nova Pessoa")
        print("P3 - Editar Pessoa", end="      ")
        print("P4 - Apagar Pessoa")
        print("M1 - Lista de Motores", end="   ")
        print("M2 - Criar novo Motor")
        print("M3 - Editar Motor", end="       ")
        print("M4 - Apagar Motor")
        print("Cor1 - Lista de Cores", end="   ")
        print("Cor2 - Criar nova Cor")
        print("Cor3 - Editar Cor", end="       ")
        print("Cor4 - Apagar Cor")
        print("Save - Salvar Listas", end="    ")
        print("Load - Carregar Listas")
        print("Ex - Carregar Exemplo", end="   ")
        print("Skip - Sair do Menu")

        op = input(">>>").lower()
        if op == "cor1":
            print("--- | Lista de Cores | ---")
            for i, cor_lista in enumerate(lista_cores):
                print(f"Cor {i + 1}: {cor_lista.nome_cor} - RBG: {cor_lista.rgb}")
        elif op == "cor2":
            print("--- | A Criar Cor | ---")
            nome_cor = input("Insira o nome da cor:")
            r_cor = int(input("Insira o 'R' do código RGB:"))
            g_cor = int(input("Insira o 'G' do código RGB:"))
            b_cor = int(input("Insira o 'B' do código RGB:"))
            cor = Cor(nome_cor, r_cor, g_cor, b_cor)
            lista_cores.append(cor)
            print("--- | Cor Criada | ---")
        elif op == "cor3":
            print("--- | Edição de Cor | ---")
            for indice, cor_lista in enumerate(lista_cores):
                print(f"Cor {indice + 1} - {cor_lista.nome_cor}")
            print("Escolha o número da cor que deseja alterar")
            escolha = int(input(">>>")) - 1
            if 0 > escolha or escolha >= len(lista_cores):
                print("--- | Erro: A retornar Ao Menu | ---")
            else:
                novo_nome = input("Insira o novo nome da cor:")
                novo_r = int(input("Insira o novo 'R' do RGB:"))
                novo_g = int(input("Insira o novo 'B' do RGB:"))
                novo_b = int(input("Insira o novo 'G' do RGB:"))
                lista_cores[escolha] = Cor(novo_nome, novo_r, novo_g, novo_b)
                print("--- | Edição Realizada Com Sucesso! | ---")
        elif op == "cor4":
            if len(lista_cores) != 0:
                print("--- | Deletar Cor | ---")
                for indice, cor_lista in enumerate(lista_cores):
                    print(
                        f"Cor {indice + 1} - {cor_lista.nome_cor} RGB: {cor_lista.rgb}"
                    )
                print("Escolha o número da cor que deseja apagar")
                escolha = int(input(">>>"))
                while 0 >= escolha or escolha > len(lista_cores):
                    escolha = int(input("SELECIONE UM NÚMERO DENTRO DA LISTA! >>>"))
                escolha = escolha - 1
                del lista_cores[escolha]
                print("--- | Cor Apagada!!! A retornar Ao Menu | ---")
            else:
                print("--- | Não Há Cores Para Deletar! A Retornar Ao Menu | ---")
        elif op == "p1":
            print("--- | Lista de Pessoas | ---")
            for i, pessoa_lista in enumerate(lista_pessoas):
                print(f"Pessoa {i + 1}: {pessoa_lista.nome} {pessoa_lista.apelido}")
                print(
                    f"CC: {pessoa_lista.cc}, Morada: {pessoa_lista.morada}, Tel: {pessoa_lista.telemovel}"
                )
        elif op == "p2":
            print("--- | A Criar Pessoa | ---")
            nome = input("Insira o nome:")
            apelido = input("Insira o apelido:")
            cc = input("Insira o CC:")
            morada = input("Insira a morada:")
            telemovel = input("Insira o telemóvel:")
            pessoa = Pessoa(nome, apelido, cc, morada, telemovel)
            lista_pessoas.append(pessoa)
            print("--- | Pessoa Criada | ---")
        elif op == "p3":
            print("--- | Edição de Pessoa | ---")
            for indice, pessoa in enumerate(lista_pessoas):
                print(f"Pessoa {indice + 1} - {pessoa.nome}")
            print("Escolha o número da pessoa que deseja alterar")
            escolha = int(input(">>>")) - 1
            if 0 > escolha or escolha >= len(lista_pessoas):
                print("--- | Erro: A retornar Ao Menu | ---")
            else:
                novo_nome = input("Insira o novo nome:")
                novo_apelido = input("Insira o novo apelido:")
                novo_cc = input("Insira o novo CC:")
                novo_morada = input("Insira a nova morada:")
                novo_telemovel = input("Insira o novo telemóvel:")
                lista_pessoas[escolha] = Pessoa(
                    novo_nome, novo_apelido, novo_cc, novo_morada, novo_telemovel
                )
                print("--- | Edição Realizada Com Sucesso! | ---")
        elif op == "p4":
            if len(lista_pessoas) != 0:
                print("--- | Deletar Pessoa | ---")
                for indice, pessoa_lista in enumerate(lista_pessoas):
                    print(
                        f"Pessoa {indice + 1} - {pessoa_lista.nome} {pessoa_lista.apelido}"
                    )
                print("Escolha o número da pessoa que deseja apagar")
                escolha = int(input(">>>"))
                while 0 >= escolha or escolha > len(lista_pessoas):
                    escolha = int(input("SELECIONE UM NÚMERO DENTRO DA LISTA! >>>"))
                escolha = escolha - 1
                del lista_pessoas[escolha]
                print("--- | Pessoa Apagada!!! A retornar Ao Menu | ---")
            else:
                print("--- | Não Há Pessoas Para Deletar! A Retornar Ao Menu | ---")
        elif op == "m1":
            print("--- | Lista de Motores | ---")
            for i, motor_lista in enumerate(lista_motores):
                print(
                    f"Motor {i + 1}: {motor_lista.montadora} de {motor_lista.cavalos} Cavalos, {motor_lista.cilindros} cilindros"
                )
                print(
                    f"{motor_lista.cilindradas} cilindradas, {motor_lista.torque} de torque, cambio {motor_lista.cambio} de {motor_lista.peso} kg"
                )
        elif op == "m2":
            print("--- | A Criar Motor | ---")
            combustivel = input("Insira o tipo de combustivel:")
            cavalos = float(input("Insira o número de cavalos:"))
            torque = float(input("Insira o torque:"))
            cilindros = int(input("Insira o número de cilindros:"))
            cilindradas = float(input("Insira as cilindradas:"))
            cambio = input("Insira o cambio:")
            peso = float(input("Insira o peso:"))
            montadora = input("Insira a montadora")
            motor = Motor(
                combustivel,
                cavalos,
                torque,
                cilindros,
                cilindradas,
                peso,
                montadora,
                cambio,
            )
            lista_motores.append(motor)
            print("--- | Motor Criado | ---")
        elif op == "m3":
            print("--- | Edição de Motor | ---")
            for indice, motor in enumerate(lista_motores):
                print(
                    f"Motor {indice + 1} - {motor.montadora} de {motor.cavalos} cavalos"
                )
            print("Escolha o número do motor que deseja alterar")
            escolha = int(input(">>>")) - 1
            if 0 > escolha or escolha >= len(lista_pessoas):
                print("--- | Erro: A retornar Ao Menu | ---")
            else:
                novo_combustivel = input("Insira o novo tipo de combustivel:")
                novo_cavalos = float(input("Insira o novo número de cavalos:"))
                novo_torque = float(input("Insira o novo torque:"))
                novo_cilindros = int(input("Insira o novo número de cilindros:"))
                novo_cilindradas = float(input("Insira as novas cilindradas:"))
                novo_cambio = input("Insira o novo cambio:")
                novo_peso = float(input("Insira o novo peso:"))
                novo_montadora = input("Insira a nova montadora:")
                lista_motores[escolha] = Motor(
                    novo_combustivel,
                    novo_cavalos,
                    novo_torque,
                    novo_cilindros,
                    novo_cilindradas,
                    novo_peso,
                    novo_montadora,
                    novo_cambio,
                )
                print("--- | Edição Realizada Com Sucesso! | ---")
        elif op == "m4":
            if len(lista_motores) != 0:
                print("--- | Deletar Motor | ---")
                for indice, motor_lista in enumerate(lista_motores):
                    print(
                        f"Motor {indice + 1} - {motor_lista.montadora} de {motor_lista.cavalos} cavalos"
                    )
                print("Escolha o número do motor que deseja apagar")
                escolha = int(input(">>>"))
                while 0 >= escolha or escolha > len(lista_motores):
                    escolha = int(input("SELECIONE UM NÚMERO DENTRO DA LISTA! >>>"))
                escolha = escolha - 1
                del lista_motores[escolha]
                print("--- | Motor Apagado!!! A retornar Ao Menu | ---")
            else:
                print("--- | Não Há Motores Para Deletar! A Retornar Ao Menu | ---")
        elif op == "c1":
            print("--- | Lista de Carros | ---")
            for i, carro_lista in enumerate(lista_carros):
                print(
                    f"Carro {i + 1}: {carro_lista.marca} {carro_lista.modelo} {carro_lista.cor.nome_cor}"
                )
                print(
                    f"com {carro_lista.kms} kms rodados, consumo de {carro_lista.consumo} kms/L"
                )
                print(
                    f"Dono: {carro_lista.dono.nome}, Motor: {carro_lista.motor.montadora} de {carro_lista.motor.cavalos} cavalos"
                )
        elif op == "c2":
            print("-- | A Criar Carro | ---")
            if (
                len(lista_cores) == 0
                or len(lista_motores) == 0
                or len(lista_pessoas) == 0
            ):
                print("--- | !! Alerta !! | ---")
                print(
                    "Para a criação de um carro é necessário selecionar um dono, um motor e uma cor para ele!!"
                )
                print(
                    "Contudo um ou mais destes itens não há pelo menos um já existe no sistema"
                )
                print(
                    f"Pessoas: {len(lista_pessoas)}, Motores: {len(lista_motores)} e Cores: {len(lista_cores)}"
                )
                print("A voltar para o menu para realizar a criação do item em falta!")
            else:
                print("---| Selecione o Motor | ---")
                for indice, motor_lista in enumerate(lista_motores):
                    print(
                        f"Motor {indice + 1} - {motor_lista.montadora} de {motor_lista.cavalos} cavalos"
                    )
                print("Escolha o número do motor que deseja selecionar")
                escolha_m = int(input(">>>"))
                while 0 >= escolha_m or escolha_m > len(lista_motores):
                    escolha_m = int(input("SELECIONE UM NÚMERO DENTRO DA LISTA! >>>"))
                escolha_m = escolha_m - 1
                print("---| Selecione a Cor | ---")
                for indice, cor_lista in enumerate(lista_cores):
                    print(
                        f"Cor {indice + 1} - {cor_lista.nome_cor} RGB: {cor_lista.rgb}"
                    )
                print("Escolha o número da cor que deseja selecionar")
                escolha_c = int(input(">>>"))
                while 0 >= escolha_c or escolha_c > len(lista_cores):
                    escolha_c = int(input("SELECIONE UM NÚMERO DENTRO DA LISTA! >>>"))
                escolha_c = escolha_c - 1
                print("---| Selecione o Motor | ---")
                for indice, pessoa_lista in enumerate(lista_pessoas):
                    print(
                        f"Pessoa {indice + 1} - {pessoa_lista.nome} {pessoa_lista.apelido}"
                    )
                print("Escolha o número da pessoa que deseja selecionar")
                escolha_p = int(input(">>>"))
                while 0 >= escolha_p or escolha_p > len(lista_pessoas):
                    escolha_p = int(input("SELECIONE UM NÚMERO DENTRO DA LISTA! >>>"))
                escolha_p = escolha_p - 1
                a_marca = input("Insira a marca do carro:")
                o_modelo = input("Insira o modelo do carro:")
                o_consumo = float(input("Insira o consumo do carro:"))
                o_kms = float(input("Insira a quilometragem do carro:"))
                carro = Carro(
                    dono=lista_pessoas[escolha_p],
                    cor=lista_cores[escolha_c],
                    motor=lista_motores[escolha_m],
                    marca=a_marca,
                    modelo=o_modelo,
                    consumo=o_consumo,
                    kms=o_kms,
                )
                lista_carros.append(carro)
                print("--- | Carro Criado Com Sucesso | ---")
        elif op == "c3":
            for i, carro_lista in enumerate(lista_carros):
                print(
                    f"Carro {i + 1}: {carro_lista.marca} {carro_lista.modelo} {carro_lista.cor.nome_cor}"
                )
                print("Selecione o carro que queira editar")
                escolha_carro = int(input(">>>"))
                while 0 >= escolha_carro or escolha_carro > len(lista_carros):
                    escolha_carro = int(
                        input("SELECIONE UM NÚMERO DENTRO DA LISTA! >>>")
                    )
                escolha_carro = escolha_carro - 1
                print("--- | Edite o Motor | ---")
                novo_combustivel = input("Insira o novo tipo de combustivel:")
                novo_cavalos = float(input("Insira o novo número de cavalos:"))
                novo_torque = float(input("Insira o novo torque:"))
                novo_cilindros = int(input("Insira o novo número de cilindros:"))
                novo_cilindradas = float(input("Insira as novas cilindradas:"))
                novo_cambio = input("Insira o novo cambio:")
                novo_peso = float(input("Insira o novo peso:"))
                novo_montadora = input("Insira a nova montadora:")
                carro_lista.motor.combustivel = novo_combustivel
                carro_lista.motor.cavalos = novo_cavalos
                carro_lista.motor.torque = novo_torque
                carro_lista.motor.cilindros = novo_cilindros
                carro_lista.motor.cilindradas = novo_cilindradas
                carro_lista.motor.peso = novo_peso
                carro_lista.motor.cambio = novo_cambio
                carro_lista.motor.montadora = novo_montadora
                print("--- | Motor Editado | ---")
                print("--- | Edite o Dono | ---")
                novo_nome = input("Insira o novo nome:")
                novo_apelido = input("Insira o novo apelido:")
                novo_cc = input("Insira o novo CC:")
                novo_morada = input("Insira a nova morada:")
                novo_telemovel = input("Insira o novo telemóvel:")
                carro_lista.dono.nome = novo_nome
                carro_lista.dono.apelido = novo_apelido
                carro_lista.dono.cc = novo_cc
                carro_lista.dono.telemovel = novo_telemovel
                print("--- | Dono Editado | ---")
                print("--- | Edite a Cor | ---")
                novo_nome_cor = input("Insira o novo nome da cor:")
                novo_r = int(input("Insira o novo 'R' do RGB:"))
                novo_g = int(input("Insira o novo 'B' do RGB:"))
                novo_b = int(input("Insira o novo 'G' do RGB:"))
                carro_lista.cor.nome_cor = novo_nome_cor
                carro_lista.cor.rgb = [novo_r, novo_g, novo_b]
                print("--- | Cor Editada | ---")
                print("--- | Edite o Carro | ---")
                nova_marca = input("Insira a nova marca do carro:")
                novo_modelo = input("Insira o novo modelo do carro:")
                novo_consumo = float(input("Insira o novo consumo do carro:"))
                novo_kms = float(input("Insira a nova quilometragem do carro:"))
                carro_lista.marca = nova_marca
                carro_lista.modelo = novo_modelo
                carro_lista.consumo = novo_consumo
                carro_lista.kms = novo_kms
                print("--- | Carro Editado | ---")
        elif op == "c4":
            if len(lista_carros) != 0:
                for i, carro_lista in enumerate(lista_carros):
                    print(
                        f"Carro {i + 1}: {carro_lista.marca} {carro_lista.modelo} {carro_lista.cor.nome_cor}"
                    )
                print("Selecione o carro que queira editar")
                escolha_car = int(input(">>>"))
                while 0 >= escolha_car or escolha_car > len(lista_carros):
                    escolha_car = int(input("SELECIONE UM NÚMERO DENTRO DA LISTA! >>>"))
                escolha_car = escolha_car - 1
                del lista_carros[escolha_car]
                print("--- | Carro Apagado!!! A retornar Ao Menu | ---")
            else:
                print("--- | Não Há Carros Para Deletar! A Retornar Ao Menu | ---")
        elif op == "load":
            print("--- | A Carregar Lista | ---")
            with open("lista_cores.pkl", "rb") as f:
                lista_cores = pickle.load(f)
            with open("lista_motores.pkl", "rb") as f:
                lista_motores = pickle.load(f)
            with open("lista_pessoas.pkl", "rb") as f:
                lista_pessoas = pickle.load(f)
            with open("lista_carros.pkl", "rb") as f:
                lista_carros = pickle.load(f)
        elif op == "ex":  # Caso Queira Executar Um Exemplo
            cor_ex = Cor("Azul", 1, 1, 1)
            pessoa_ex = Pessoa("Lucas", "Bica", "007", "Faro", "928")
            motor_ex = Motor("Gasolina", 330, 430, 6, 3000, 1700, "Toyota", "Manual")
            carro_ex = Carro(
                pessoa_ex, cor_ex, motor_ex, "Toyota", "Supra", 10.5, 200000
            )
            lista_carros.append(carro_ex)
            lista_motores.append(motor_ex)
            lista_cores.append(cor_ex)
            lista_pessoas.append(pessoa_ex)
            print("--- | Exemplo Carregado | ---")
        elif op == "save":
            print("--- | Listas Salvas no Sistema | ---")
            with open("lista_cores.pkl", "wb") as f:
                pickle.dump(lista_cores, f)
            with open("lista_pessoas.pkl", "wb") as f:
                pickle.dump(lista_pessoas, f)
            with open("lista_motores.pkl", "wb") as f:
                pickle.dump(lista_motores, f)
            with open("lista_carros.pkl", "wb") as f:
                pickle.dump(lista_carros, f)
        else:
            print("--- | Até Logo :) | ---")
            break


if __name__ == "__main__":
    main()

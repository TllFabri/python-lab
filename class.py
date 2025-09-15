"""
Modele e implemente as classes para as seguintes entidades: Casa, Carro, Fogão; AS classes precisam ter: 
pelo menos 4 atributos, sendo pelo menos um privado; 3 métodos, sendo pelo menos um privado; A classe precisa 
alterar a sua saida caso seja usada a função print();

"""

class Casa:
    def __init__(self, endereco, cor, num_quartos, preco):
        self.endereco = endereco
        self.cor = cor
        self.num_quartos = num_quartos
        self.__preco = preco  # atributo privado

    def abrir_porta(self):
        print(f"A porta da casa na {self.endereco} foi aberta.")

    def pintar(self, nova_cor):
        print(f"A casa foi pintada de {self.cor} para {nova_cor}.")
        self.cor = nova_cor

    def __avaliar_preco(self):  # método privado
        return f"O valor estimado da casa é R${self.__preco:,.2f}"

    def __str__(self):
        return f"Casa {self.cor}, {self.num_quartos} quartos, localizada em {self.endereco}."


class Carro:
    def __init__(self, modelo, marca, ano, preco):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self.__preco = preco  # atributo privado

    def ligar(self):
        print(f"O {self.modelo} está ligado!")

    def acelerar(self):
        print(f"O {self.modelo} está acelerando!")

    def __calcular_ipva(self):  # método privado
        return self.__preco * 0.04  # 4% do valor do carro

    def __str__(self):
        return f"Carro {self.marca} {self.modelo}, ano {self.ano}."


class Fogao:
    def __init__(self, marca, bocas, cor, preco):
        self.marca = marca
        self.bocas = bocas
        self.cor = cor
        self.__preco = preco  # atributo privado

    def acender_boca(self, numero):
        if 1 <= numero <= self.bocas:
            print(f"A boca {numero} foi acesa.")
        else:
            print("Número de boca inválido!")

    def apagar_boca(self, numero):
        if 1 <= numero <= self.bocas:
            print(f"A boca {numero} foi apagada.")
        else:
            print("Número de boca inválido!")

    def __verificar_gas(self):  # método privado
        return "Nível de gás: OK"

    def __str__(self):
        return f"Fogão {self.marca}, {self.bocas} bocas, cor {self.cor}."
    

# Exemplo de uso
if __name__ == "__main__":
    casa = Casa("Rua das Flores, 123", "azul", 3, 350000)
    carro = Carro("Civic", "Honda", 2022, 120000)
    fogao = Fogao("Brastemp", 4, "prata", 2000)

    print(casa)
    casa.abrir_porta()
    casa.pintar("vermelha")

    print(carro)
    carro.ligar()
    carro.acelerar()

    print(fogao)
    fogao.acender_boca(2)
    fogao.apagar_boca(2)

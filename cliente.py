


from datetime import date
from helper import data_para_str, str_para_date


class Cliente:
    
    contador: int = 101


    def __init__(self: object, nome: str, email: str, cpf: str, data_nascimento: str) -> None:

        self.__codigo: int = Cliente.contador

        self.__nome: str = nome
        self.__email: str = email
        self.__cpf: str = cpf

        self.__data_nascimento: date = str_para_date(data_nascimento)
        self.__data_cadastro: date = date.today()

        Cliente.contador+=1


    @property
    def codigo(self: object) -> int:
        return self.__codigo

    @property
    def nome(self: object) -> str:
        return self.__nome

    @property
    def email(self: object) -> str:
        return self.__email

    @property
    def cpf(self: object) -> str:
        return self.__cpf

    @property
    def data_nascimento(self: object) -> str:
        return data_para_str(self.__data_nascimento) # ATENÇÃO AQUI!

    @property
    def data_cadastro(self: object) -> str:
        return data_para_str(self.__data_cadastro)    # ATENÇÃO AQUI!        



    def __str__(self: object) -> str:
        return f'\nCódigo: {self.codigo} \nNome: {self.nome} \nData de Nascimento: {self.data_nascimento} \nCadastro: {self.data_cadastro}'

        












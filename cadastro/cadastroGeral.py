from insert.inserts import Inserts
dados = Inserts()
class CadastroGeral():
    def cadastroCliente(self):
        nome=input("Nome completo: ")
        cpf=input("CPF: ")
        idade=input("Idade: ")
        telefone=input("Telefone: ")
        senha=input("Senha: ")

        dados.insertClient(nome,cpf,idade,telefone,senha)
    
    def cadastroDoItem(self):
        nome=input("Nome do item: ")
        preco=input("Preço do item: ")
        dados.insertItens(nome, preco)







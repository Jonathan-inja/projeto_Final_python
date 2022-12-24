import json
from cadastro.cadastroGeral import CadastroGeral
from insert.inserts import Inserts

#instancias
salva = Inserts()
cadastro = CadastroGeral()

class Common():
    def verificadorUser(self,nomeCompleto):
        with open("data/clientes.json", encoding='utf-8') as jsonFile:
            user = json.load(jsonFile)
        
        for valor in range(len(user)):
            if(user[valor]['nome'] == nomeCompleto):
                return True

common = Common()

class Pedidos():
    def autenticator():
        user=input("Digite o nome do Cliente:")
        if(common.verificadorUser(user)):
            with open("data/itens.json", encoding='utf-8') as jsonFile:
                escolha = json.load(jsonFile)
            
            print("==================== Itens Disponiveis =====================")
            for pedido in range(len(escolha)):
                print(f"[{pedido}]      {escolha[pedido]['nome_do_item']} ---------------------- R$ {escolha[pedido]['preco']}")
            

            pedidoCliente = int(input(":"))
            valorPago = float(input("Digita valor pago:"))
            troco = valorPago - float(escolha[pedidoCliente]['preco'])
            print(f"Troco Do Cliente:{troco}")
            salva.nota(user,pedidoCliente,valorPago,troco)

        else:
            print("Usuario ainda não cadastrado!")
            cadastro.cadastroCliente()
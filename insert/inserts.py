import json
from os import path
import datetime
class Inserts():
    def insertClient(self, nome,cpf,idade,telefone,senha):

 
        filename = "data/clientes.json"
        listObj = []
        
        
        # Lendo o arquivo json
        with open(filename) as fp:
            listObj = json.load(fp)
            listObj.append({
            "nome":nome,
            "cpf": cpf,
            "idade": idade,
            "telefone": telefone,
            "senha":senha

            })
        
        with open(filename, 'w') as json_file:
            json.dump(listObj, json_file, 
                                indent=4,  
                                separators=(',',': '))
        
        print('Usuario cadastrado Com sucesso')
    
    def insertItens(self,nomeDoItem,preco):
        filename = "data/itens.json"
        listObj = []
        with open(filename) as fp:
            listObj = json.load(fp)
            listObj.append({
            "nome_do_item":nomeDoItem,
            "preco": preco,
            })
        
        with open(filename, 'w') as json_file:
            json.dump(listObj, json_file, 
                                indent=4,  
                                separators=(',',': '))
        
        print('Pedido Inserido no Menu!')
    
    def nota(self,nomeCliente,pedidoCliente,valorPago,troco):
        filename = "data/notaFiscal.json"
        listObj = []
        with open(filename) as fp:
            listObj = json.load(fp)
            listObj.append({
            "nome_do_cliente":nomeCliente,
            "pedido_do_cliente": pedidoCliente,
            "valor_pago": valorPago,
            "troco": troco,
            "data": str(datetime.datetime.now())
            })
        
        with open(filename, 'w') as json_file:
            json.dump(listObj, json_file, 
                                indent=4,  
                                separators=(',',': '))
        
import json
from cadastro.cadastroGeral import CadastroGeral
from pedido.pedidos import Pedidos
cadastro = CadastroGeral()
pedido = Pedidos



print('''Sejá Bem Vindo(a)!''')
while True:
    print('''--------- OPÇÕES INICIAIS ---------''')
    print('''
    [1] - Cadastrar Cliente
    [2] - Fazer Pedido
    [3] - Adicionar item
    [4] - Gerá Nota das vendas
    [5] - Sair.
    ''')
    escolha = int(input(":"))
    if(escolha == 1):
        cadastro.cadastroCliente()
    elif(escolha == 2):
        pedido.autenticator()
    elif(escolha == 3):
        cadastro.cadastroDoItem()
    elif(escolha == 4):
        with open("data/notaFiscal.json", encoding='utf-8') as jsonFile:
            user = json.load(jsonFile)

        listWrite = list()
        
        Topo = ("--------- Nota ---------  \n")
        listWrite.append(Topo)
        
        for valor in range(len(user)):
            nome=f"Nome Do Cliente   -------------------- {str(user[valor]['nome_do_cliente'])} \n"
            pedidoCliente=f"Pedido_do_cliente --------------------- {str(user[valor]['pedido_do_cliente'])} \n"
            valorCliente= f"Valor_pago  --------------------------- {str(user[valor]['valor_pago']) } \n"
            troco= f"Troco   --------------------- {str(user[valor]['troco'])} \n"
            data=  f"Data ---------------------------------- {str(user[valor]['data'])} \n"
            fim="========================================================= \n" 
            
            listWrite.append(nome)
            listWrite.append(pedidoCliente)
            listWrite.append(valorCliente)
            listWrite.append(troco)
            listWrite.append(data)
            listWrite.append(fim)
        with open("impressaoNotaFiscal.txt","a") as impressao:
            impressao.writelines(listWrite)
    elif(escolha == 5):
        break
    else:
        print("Opção não encontrada por favor digitá novamente o numero da opção!!!")

'''Implementar um código com menu de 4 opções: 
1 - Adicionar um nome a lista, 
2 - Imprimir todos os nomes da lista, 
3 - Apagar um nome na lista e 
4 - Atualizar um nome na lista.'''

def menu(list):
    lista = list
    while True:
        print("Lista de opções")
        print("1 : adicionar nome a o conjunto: ")
        print("2 : apresentar os nomes adicionados a lista: ")
        print("3 : apagar um nome a lista: ")
        print("4 : adicionar um nome a lista: ")
        print("Digite '0' para sair")
        opcao = input(">> ")
        match opcao:
          case "1":
            nomes = input("Digite o nome: ")
            lista.append(nomes)
          case "2":
            if len(lista) > 0:
              print(lista)
            else:
              ("Não há elementos na lista")
          case "3":
            apagarNome = input("Digite o nome a se apagado: ")
            print(deletarElementoDaLista(apagarNome, lista))
          case "4":
            nomeAtualizar = input("Digite o nome que queira atualizar: ")
            adicionarNome = input("Atalizar para o nome: ")
            print(adicionarElementoAlista(nomeAtualizar, adicionarNome ,lista))
          case "0":
              break
          case _:
              print("opção não encontrada")
               
def deletarElementoDaLista(nome, list):
    for n in list:
        if n == nome:
            list.remove(nome)
            resultado = list
        else:
            resultado = "Elemento não encontrado"
    return resultado

def adicionarElementoAlista(nameA, nameB, list):
  encontrado = False
  for i in range(len(list)):
      if list[i] == nameA:
          list[i] = nameB
          encontrado = True
          break
    
  if encontrado:
      resultado = list
  else:
      resultado = "Elemento não encontrado"
    
  return resultado

lista_nomes =[]
menu(lista_nomes)
      
      
         
      
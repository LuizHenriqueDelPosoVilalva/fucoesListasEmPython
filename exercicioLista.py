'''implementar um código com menu de 4 opções: 1 - Adicionar um nome a lista, 2 - 
Imprimir todos os nomes da lista, 3 - Apagar um nome na lista e 4 - Atualizar um nome na lista.'''

lista = []
while True:
    nome = input("Digite quantos nomes quer adicionar a lista, digite 0 para sair: ")

    if nome == "0":
        break
    else:
        lista.append(nome)
        
print(lista)
lista.pop(2)
print(lista)
lista[3] = "josé"
print(lista)

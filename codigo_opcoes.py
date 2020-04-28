import sys


itens = []
opcao = ''

#função para adicionar itens à lista itens
def adicionaItens():

	op = 's'
	while(op == 's'):
		if(op == 's'):
			i = input('Digite o item a ser adicionado: ')
			itens.append(i)
			print('Item adicionado com sucesso')
			op = input('Deseja adicionar mais um item à lista s- sim, n- não', '\n')
	else:
		
		menu()

#função para listar itens da lista itens
def listaItens():
	print('Lista de itens:\n')
	for i in itens:
		print(i)
	print('Número de itens na lista: ',len(itens),'\n')

	menu()

#funcao para deletar itens da lista itens
def deletaItens():

	item = input('Qual item você deseja deletar da lista: ')

	for i in itens:

		if (i == item):

			itens.remove(i)
			print('Item removido com sucesso!', '\n')

	menu()


def menu():

	#def listaItens():

	opcao = int(input('Digite a opção desejada:\n 1-Listar itens\n 2-Adicionar itens\n 3-Deletar itens\n 4-Voltar ao menu inicial\n 0-Sair do programa'))

	#menu de opcoes de acoes a serem realizadas:

	#lista itens da lista
	if (opcao == 1):

		listaItens()

	#adiciona itens à lista
	elif (opcao == 2):

		adicionaItens()

	#deleta itens da lista
	elif (opcao == 3):

		deletaItens()

	#volta ao menu inicial
	elif (opcao == 4):

		menu()

	elif (opcao == 0):

		print('Até a próxima!')
		sys.exit()


menu()












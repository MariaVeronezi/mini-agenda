AGENDA = {'Maria': '6666-6666'}

def exibir_agenda():

  for nome, telefone in AGENDA.items():
    print("Contato: " + nome + " - Telefone: " + telefone)

def adicionar_contato():
  nome = input("Qual o nome? ")
  telefone = input("Qual o telefone? ")
  AGENDA[nome] = telefone

def remover_contato():
  nome = input("Digite o nome para remover? ")
  AGENDA.pop(nome)



sair = False
while(sair == False):
  print('----------------------------')
  print('Acessar agenda')
  print('Escolha uma opção:')
  print('1. Exibir agenda', end="  ")
  print('2. Adicionar um novo contato')
  print('3. Remover um contato', end= "  ")
  print('4. Sair')
  opcao = int(input("> "))

  if opcao == 1:
    exibir_agenda()
  elif opcao == 2:
    adicionar_contato()
  elif opcao == 3:
    remover_contato()
  elif opcao == 4:
    sair = True
  else:
    print(' opção não encontrada ')

print('Agenda fechada')

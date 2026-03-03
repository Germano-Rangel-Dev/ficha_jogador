# Exercício Ficha de Jogador
# Objetivo: Praticar Variáveis, entrada de dados e saída formatada

print('=== Criador de Ficha do Jogador ===')
nome = input('Digite o nome do Jogador(Avatar): ')
idade = int(input('Digite a idade: ')) 
classe = input('Digite a classe do jogador(Guerreiro, Mago, Arqueiro...): ')
nivel = int(input('Digite o nível do Jogador: '))
vida = float(input('Quantidade de vida do jogador(max. 100): '))
poder =float(input('Qual a quantidade de poder(max. 50):'))

poder_total = nivel + poder
anos_para_100 = 100 - idade

print('\n=== FICHA DE JOGADOR ===')
print(f'Nome: {nome}')
print(f'Idade: {idade}')
print(f'Classe: {classe}')
print(f'Nível: {nivel}')
print(f'Vida: {vida}')
print(f'Poder: {poder}')
print(f'O poder especial do {classe} {nome} é: {poder_total}')
print(f'Faltam {anos_para_100} anos de idade para {nome} conseguir chegar ao limite de idade que são 100.')


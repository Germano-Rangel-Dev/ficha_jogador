# ==========================================
# Ficha do Jogador V2
# Exercício de Python para treinar variáveis
# ==========================================

print("===================================")
print("     FICHA DO JOGADOR - VERSÃO 2   ")
print("===================================\n")

# Entrada de dados
nome = input("Digite o nome do jogador: ")
idade = int(input("Digite a idade: "))
classe = input("Digite a classe (Guerreiro, Mago, Arqueiro...): ")
nivel = int(input("Digite o nível do jogador(máx. 100): "))
vida = float(input("Digite a quantidade de vida(máx. 50): "))
poder = float(input("Digite a quantidade de poder(máx.100): "))
ataque = float(input("Digite o valor de ataque(máx. 100): "))
defesa = float(input("Digite o valor de defesa(máx. 80): "))

# Cálculos com variáveis
poder_total = vida + poder + ataque + defesa
media_atributos = poder_total / 4
anos_para_100 = 100 - idade

# Classificação do jogador
if poder_total < 100:
    rank = "Iniciante"
elif poder_total < 200:
    rank = "Aventureiro"
elif poder_total < 300:
    rank = "Veterano"
else:
    rank = "Lenda"

# Mensagem especial por classe
if classe.lower() == "guerreiro":
    habilidade = "Ataque Pesado"
elif classe.lower() == "mago":
    habilidade = "Bola de Fogo"
elif classe.lower() == "arqueiro":
    habilidade = "Chuva de Flechas"
else:
    habilidade = "Habilidade Misteriosa"

# Exibição da ficha
print("\n===================================")
print("         FICHA DO PERSONAGEM       ")
print("===================================")
print(f"Nome: {nome}")
print(f"Idade: {idade} anos")
print(f"Classe: {classe}")
print(f"Nível: {nivel}")
print(f"Vida: {vida}")
print(f"Poder: {poder}")
print(f"Ataque: {ataque}")
print(f"Defesa: {defesa}")

print("\n----------- STATUS -----------")
print(f"Poder total: {poder_total}")
print(f"Média dos atributos: {media_atributos:.2f}")
print(f"Rank: {rank}")
print(f"Habilidade especial: {habilidade}")

if anos_para_100 > 0:
    print(f"Faltam {anos_para_100} anos para chegar aos 100 anos.")
elif anos_para_100 == 0:
    print("Você chegou aos 100 anos!")
else:
    print("Você já passou dos 100 anos. Que lenda!")

print("\n===================================")
print(f"O jogador {nome}, da classe {classe}, está pronto para a aventura!")
print("===================================")
def calcular_nivel(vitorias, derrotas):
    # Calcula o saldo de vitórias
    saldo_vitorias = vitorias - derrotas
    
    # Determina o nível com base no número de vitórias
    if vitorias < 10:
        nivel = "Ferro"
    elif 10 <= vitorias <= 20:
        nivel = "Bronze"
    elif 21 <= vitorias <= 50:
        nivel = "Prata"
    elif 51 <= vitorias <= 80:
        nivel = "Ouro"
    elif 81 <= vitorias <= 90:
        nivel = "Diamante"
    elif 91 <= vitorias <= 100:
        nivel = "Lendário"
    else:
        nivel = "Imortal"
    
    # Exibe a mensagem final
    print(f"O Herói tem um saldo de {saldo_vitorias} e está no nível  {nivel}")
    
    return saldo_vitorias, nivel

# Exemplo de uso da função
vitorias = int(input("Digite o número de vitórias: "))
derrotas = int(input("Digite o número de derrotas: "))

# Chama a função e exibe o resultado
calcular_nivel(vitorias, derrotas)
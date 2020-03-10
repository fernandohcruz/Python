import random

def baralho():
    return [1,2,3,4,5,6,7,8,9,10,"Q","J","K"]

def cartas():
    return random.choice(baralho())

def soma_pontos(soma):
    carta = cartas()
    print("A carta retirada foi: {carta}".format(carta=carta))
    if carta == "Q" or carta == "J" or carta == "K":
        carta = 10
    soma = soma + carta
    return soma

def vitoria_derrota(soma):
    if soma == 21:
        return True
    elif soma > 21:
        return False

def jogada(player):
    x = input(f"Deseja pegar uma carta Player {player}? 'SIM' 'NAO': ")
    if x == "s":
        return True
    else:
        return False

def continua():
    x = input("Desejam continuar a jogar? 'SIM' 'NAO': ")
    if x == "s":
        return True
    else:
        return False

def confere21(dicionario):
    return dicionario > 21

def all_21(dicionario):
    count = 0
    for i in range(len(dicionario)):
        if confere21(dicionario[i+1]):
            count+=1
    return count == len(dicionario)

def main():
    print("Bem Vindo ao BlackJack!!")
    while True:
        lista_jogadores = {}
        jogadores = int(input("Quantos jogadores iram jogar? "))
        for i in range(jogadores):
            lista_jogadores[i+1] = 0
        game = True
        i = 1
        while game:
            if not confere21(lista_jogadores[i]):
                jog = jogada(i)
                if jog:
                    lista_jogadores[i] = soma_pontos(lista_jogadores[i])
                    print(lista_jogadores)
                    if all_21(lista_jogadores): 
                        print("Não houve ganhadores!!")
                        break 
                    elif vitoria_derrota(lista_jogadores[i]):
                        print(f"Player {i} GANHOU!!!")
                        break
            i+=1
            if i == jogadores+1: i = 1

        if not continua():
            break

# print(cartas())
# print(soma_pontos(5))
# print(vitoria_derrota(21))
main()
# print(all_21({1: 25, 2: 27, 3: 28}))
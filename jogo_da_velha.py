import random
def tabuleiro(lista):
    i=1
    while i <= len(lista):
        if i%3!=0: print(f"{lista[i-1]}|", end="")
        elif i%3==0: print(f"{lista[i-1]}")
        i+=1

def iniciando():
    mark = ""
    while not (mark == "X" or mark == "O"):
        mark = input("Você quer ser 'X' ou 'O'? ").upper()

    if mark == "X":
        return ("X", "O")
    else:
        return ("O", "X")

def comeca_jogando():
    if random.randint(0,1)==0:
        return "Player 2"
    else:
        return "Player 1"

def checa_espaco(board, position):
    return board[position] == " "

def checa_cheio(board):
    for i in range(len(board)):
        if checa_espaco(board, i):
            return False
    return True

def vitoria(lista, mark):
    if lista[0] == mark and lista[1] == mark and lista[2] == mark or lista[3] == mark and lista[4] == mark and lista[5] == mark or lista[6] == mark and lista[7] == mark and lista[8] == mark or lista[0] == mark and lista[3] == mark and lista[6] == mark or lista[1] == mark and lista[4] == mark and lista[7] == mark or lista[2] == mark and lista[5] == mark and lista[8] == mark or lista[0] == mark and lista[4] == mark and lista[8] == mark or lista[2] == mark and lista[4] == mark and lista[6] == mark:
        return True
    else:
        return False

def jogada(board, turn):
    pos = -1
    while pos not in [0,1,2,3,4,5,6,7,8] or not checa_espaco(board,pos):
        pos = int(input(f"Escolha sua jogada de (0-8) {turn}: "))
        
    return pos

def preencher(board, pos, mark):
    board[pos] = mark

def novamente():
    x = input("Querem jogar novamente? 'SIM' ou 'NAO': ").lower()
    if x == "sim":
        return True
    else:
        return False

def main():
    while True:
        board = [" "] * 9
        turn = comeca_jogando()
        print(f"{turn} começa")
        if turn == "Player 1":
            player1, player2 = iniciando()
        else:
            player2, player1 = iniciando()


        game = True
        while game:
            if turn == "Player 1":
                tabuleiro(board)
                pos = jogada(board, turn)
                preencher(board, pos, player1)
            if vitoria(board, player1):
                tabuleiro(board)
                print(f"Parabéns {turn}, você ganhou!!!")
                game = False
            else:
                if checa_cheio(board) and game != False:
                    tabuleiro(board)
                    print("Empate!!")
                    break
                else: turn = "Player 2"

            if turn == "Player 2":
                tabuleiro(board)
                pos = jogada(board, turn)
                preencher(board, pos, player2)
            if vitoria(board, player2):
                tabuleiro(board)
                print(f"Parabéns {turn}, você ganhou!!!")
                game = False
            else:
                if checa_cheio(board) and game != False:
                    tabuleiro(board)
                    print("Empate!!")
                    break
                else: turn = "Player 1"

        if not novamente():
            print("Fim de JOGO!!")
            break

main()
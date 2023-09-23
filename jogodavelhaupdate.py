import os

simbolo1 = input(' J1 escreva o valor que você quer que represente seu simbolo: ')
simbolo1 = simbolo1[0]
while True:
    simbolo2 = input(' J2 escreva o valor que você quer que represente seu simbolo: ')
    simbolo2 = simbolo2[0]
    if (simbolo1 == simbolo2):
        print ('esse simbolo já esta sendo usado')
    else:
        break

class JogoDaVela:
    tabuleiro = {'7': ' ', '8': ' ', '9': ' ', '4': ' ', '5': ' ', '6': ' ', '1': ' ', '2': ' ', '3': ' '}
    turno = None

    def __init__(self, jogador_inicial= simbolo1 ):
        self.turno = jogador_inicial

    def exibir_tabuleiro(self):
        os.system('cls')
        print("┌───┬───┬───┐")
        print(f"│ {self.tabuleiro['7']} │ {self.tabuleiro['8']} │ {self.tabuleiro['9']} │")
        print("├───┼───┼───┤")
        print(f"│ {self.tabuleiro['4']} │ {self.tabuleiro['5']} │ {self.tabuleiro['6']} │")
        print("├───┼───┼───┤")
        print(f"│ {self.tabuleiro['1']} │ {self.tabuleiro['2']} │ {self.tabuleiro['3']} │")
        print("└───┴───┴───┘")

    def verificar_jogada(self, jogada):
        if jogada in self.tabuleiro.keys():
            if self.tabuleiro[jogada] == " ":
                return True
        return False

    def verificar_tabuleiro(self):
        # Verificações das 3 verticais
        if self.tabuleiro['7'] == self.tabuleiro['4'] == self.tabuleiro['1'] != ' ':
            return self.tabuleiro['7']
        elif self.tabuleiro['8'] == self.tabuleiro['5'] == self.tabuleiro['2'] != ' ':
            return self.tabuleiro['8']
        elif self.tabuleiro['9'] == self.tabuleiro['6'] == self.tabuleiro['3'] != ' ':
            return self.tabuleiro['9']


        # Verificações das 3 horizontais
        elif self.tabuleiro['7'] == self.tabuleiro['8'] == self.tabuleiro['9'] != ' ':
            return self.tabuleiro['7']
        elif self.tabuleiro['4'] == self.tabuleiro['5'] == self.tabuleiro['6'] != ' ':
            return self.tabuleiro['8']
        elif self.tabuleiro['1'] == self.tabuleiro['2'] == self.tabuleiro['3'] != ' ':
            return self.tabuleiro['1']

        # Verificações das 2 diagonais
        elif self.tabuleiro['7'] == self.tabuleiro['5'] == self.tabuleiro['3'] != ' ':
            return self.tabuleiro['7']
        elif self.tabuleiro['1'] == self.tabuleiro['5'] == self.tabuleiro['9'] != ' ':
            return self.tabuleiro['1']

        # Verificando empate
        if [*self.tabuleiro.values()].count(' ') == 0:
            return "empate"
        else:
            return [*self.tabuleiro.values()].count(' ')

    def jogar(self):

        while True:
            self.exibir_tabuleiro()

            print(f"Turno do {self.turno}, qual sua jogada?")

            # Enquanto o jogador não fizer uma jogada válida
            while True:
                jogada = input("Jogada: ")

                if self.verificar_jogada(jogada):  # Se a jogada for válida...
                    break  # Encerra o loop
                else:
                    print(f"jogado do {self.turno} inválida, jogue novamente.")

            self.tabuleiro[jogada] = self.turno

            estado = self.verificar_tabuleiro()

            if estado == simbolo1 :
                input(f'{simbolo1}  é o vencedor!!!')
                break

            elif estado == simbolo2 :
                input(f'{simbolo2} é o vencedor!!!')

            if estado == "empate":
                input("EMPATE!!!")
                break


            # Troca o jogador do próximo turno
            self.turno = simbolo1  if self.turno == simbolo2  else simbolo2

        self.exibir_tabuleiro()


jogo = JogoDaVela()

jogo.jogar()







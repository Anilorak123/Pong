# Exercize 8
import sys

print("Wybierz: papier, kamień lub nożyce")

while True:
    game_dict = {'kamień':1, 'nożyce': 2, 'papier': 3}
    game = "t"
    while game == "t":
        player_a = str(input("Gracz A: "))
        player_b = str(input("Gracz B: "))
        a = game_dict.get(player_a)
        b = game_dict.get(player_b)
        sub = a - b
        if sub == 0:
            print("Remis")
        elif sub == -1 or 2:
            print("Gracz A wygrywa")
        elif sub == -2 or 1:
            print("Gracz B wygrywa")
        print("Jeśli chcesz zagrać jeszcze raz napisz t. Jeśli chcesz zakończyć napisz n")
        game = input(str())
    else:
        sys.exit()
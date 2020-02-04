# Exercize 8
import sys

print("Wybierz: papier, kamień lub nożyce")

while True:
    game_dict = {'kamień':1, 'nożyce': 2, 'papier': 3}
    game = "y"
    while game == "y":
        player_a = str(input("Gracz A: "))
        player_b = str(input("Gracz B: "))
        a = game_dict.get(player_a)
        b = game_dict.get(player_b)
        sub = a - b
        if sub == 0:
            print("It is a draw")
        elif sub == -1 or 2:
            print("Player A wins")
        elif sub == -2 or 1:
            print("Player B wins")
        print("If you want to play again write y. If you want to finish write anything else.")
        game = input(str())
    else:
        sys.exit()
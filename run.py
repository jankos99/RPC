symbol_win = ['P', 'R', 'S', 'P']

def game():
    p1 = input("P1 symbol: scissors -> S, rock -> R, paper -> P  --> ")
    p2 = input("P2 symbol: scissors -> S, rock -> R, paper -> P  --> ")

    if(p1 == p2):
        return "It is a tie."
    elif(symbol_win[symbol_win.index(p1) + 1] == p2):
        return "Player 1 is a winner."
    else:
        return "Player 2 is a winner."

while True:
    user = input("For new game hit Y, otherwise N --> ")
    if user == "Y":
        print(game())
    else:
        break

print("Game Over")
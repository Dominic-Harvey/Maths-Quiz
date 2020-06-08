import itertools

def win(current_game):

    def all_same(l):
        if l.count(l[0]) == len(l) and l [0] != 0:
            return True
        else:
            return False

    #Horizontal
    for row in game:
        print(row)
        if all_same(row):
            print (f"PLayer {row[0]} is the winner horizontally!")

    #Diagonal
    diags = []
    for col, row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if all_same(diags):
        print (f"PLayer {diags[0]} is the winner Diagonaly (/)!")

    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    if all_same(diags):
        print (f"PLayer {diags[0]} is the winner Diagonaly (\\)!")

    #Vertical
    for col in range(len(game)):
        check = []

        for row in game:
            check.append(row[col])
        
        if all_same(check):
            print (f"PLayer {check[0]} is the winner Vertically (|)!")


def game_board(game_map, player=0, row=0, column=0, just_dislplay=False):
    try:
        if game_map[row][column] !=0:
            print ("This postion is already occupied, choose another")
            return False
        print ("   "+"  ".join([str(i) for i in range(len(game_map))]))
        if not just_dislplay:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map, True

    except IndexError as e:
        print("Error: make sure you input row/column as 0 1 or 2", e)
        return game_map, False

    except Exception as e:
        print ("Something went very wrong!", e)
        return game_map, False

play = True
players = [1, 2]
while play:
    game = [[0, 0, 0], 
             [0, 0, 0], 
             [0, 0, 0]]

    game_won = False
    game, _ = game_board(game, just_dislplay=True)
    player_choice = itertools.cycle([1, 2])
    while not game_won:
        current_player = next (player_choice)
        print(f"Current player: {current_player}")
        played = False

        while not played:
            column_choice = int(input("What column do you want to play? (0, 1, 2): "))
            row_choice = int(input("What row do you want to play? (0, 1, 2): "))
            game, played = game_board(game, current_player, row_choice, column_choice)

        if win(game):
            game_won = True
            again = input("The game is over would you like to play again> (y/n) ")
            if again.lower() == "y":
                print ("Restarting")
            elif again.lower() == "n":
                print ("Shuting Down")
                play = False
            else:
                print ("Not a valid answer, shuting down")
                play = False


#game = game_board(game, just_dislplay=True)
#game = game_board(game_board, player=1, row=3, column=1)
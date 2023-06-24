### ------------------------------------- actions -------------------------------------

def make_board():
  board = []
  num_label = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
  board.append([" ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S"])
  for i in range(0,20):
    board_row = []
    board_row.append(num_label[i])
    for j in range(0,20):
      board_row.append("·")
    board.append(board_row)

  return board

def print_board(my_board):
  for i in range(0,20):
    if i<10:
      print(my_board[i][0], end="  ")
      for j in range(1,20):
        print(my_board[i][j], end=" ")
      print("")
    else:
      for j in range(0,20):
        print(my_board[i][j], end=" ")
      print("")

def convert_to_coordinates(user_input):
    split = user_input.split()
    coordinates = (int(split[0]), ord(split[1])-64)
    return coordinates

# Move pieces
def move_x(user_input):
    point = convert_to_coordinates(user_input)
    x = point[0]
    y = point[1]
    gomoku_board[x][y] = "x"
def move_o(user_input):
    point = convert_to_coordinates(user_input)
    x = point[0]
    y = point[1]
    gomoku_board[x][y] = "o"

### ------------------------------------- coordinate and input checks -------------------------------------

# convert input (number letter) to coordinates
def input_valid(user_input):
    if len(user_input) != 3 and len(user_input) != 4:
        valid = False
    elif len(user_input) == 3 and user_input[0] not in ["1","2","3","4","5","6","7","8","9"]:
        valid = False
    elif len(user_input) == 4 and user_input[0:2] not in ["10","11","12","13","14","15","16","17","18","19"]:
        valid = False
    elif ord(user_input[-1]) > ord("S") or ord(user_input[-1]) < ord("A"):
        valid = False
    else:
        valid = True
    return valid

# Check if point is on the board
def on_board(x, y):
    if 19 >= x >= 1 and 19 >= y >= 1:
        return True
    else:
        return False

# Check if move is on board and space is not occupied
def move_valid(user_input):
    point = convert_to_coordinates(user_input)
    x = point[0]
    y = point[1]
    if on_board(x, y) == True and gomoku_board[x][y] == "·":
        return True
    else:
        return False


### ------------------------------------- Win condition checks -------------------------------------

# check for horizontal win after this move (argument would be last user input for move)
def has_horizontal_win(user_input, player):
    point = convert_to_coordinates(user_input)
    pieces_in_row = [(point[0], point[1])]
    if player == 1:
        piece = "o"
    elif player == 2:
        piece = "x"
    win = False
    for i in range(2):
        if i == 1:
            xshift = -1
        else:
            xshift = 1

        x = point[0]
        y = point[1]

        for i in range(5):
            x = x+xshift
            if on_board(x,y) == True and gomoku_board[x][y] == piece:
                if (x, y) not in pieces_in_row:
                    pieces_in_row.append((x, y))
            else:
                break
        if len(pieces_in_row) >= 5:
            win = True
            break
    return win

# check for vertical win after this move (argument would be last user input for move)
def has_vertical_win(user_input, player):
    point = convert_to_coordinates(user_input)
    pieces_in_row = [(point[0], point[1])]
    if player == 1:
        piece = "o"
    elif player == 2:
        piece = "x"
    win = False
    for i in range(2):
        if i == 1:
            yshift = -1
        else:
            yshift = 1

        x = point[0]
        y = point[1]

        for i in range(5):
            y = y+yshift
            if on_board(x,y) == True and gomoku_board[x][y] == piece:
                if (x, y) not in pieces_in_row:
                    pieces_in_row.append((x, y))
            else:
                break
        if len(pieces_in_row) >= 5:
            win = True
            break
    return win

# check for 45° (/) diagonal win
def has_45diagonal_win(user_input, player):
    point = convert_to_coordinates(user_input)
    pieces_in_row = [(point[0], point[1])]
    if player == 1:
        piece = "o"
    elif player == 2:
        piece = "x"
    win = False
    for i in range(2):
        if i == 1:
            shift = -1
        else:
            shift = 1

        x = point[0]
        y = point[1]

        for i in range(5):
            x = x+shift
            y = y+shift
            if on_board(x,y) == True and gomoku_board[x][y] == piece:
                if (x, y) not in pieces_in_row:
                    pieces_in_row.append((x, y))
            else:
                break
        if len(pieces_in_row) >= 5:
            win = True
            break
    return win

# check for 315° (\) diagonal win
def has_315diagonal_win(user_input, player):
    point = convert_to_coordinates(user_input)
    pieces_in_row = [(point[0], point[1])]
    if player == 1:
        piece = "o"
    elif player == 2:
        piece = "x"
    win = False
    for i in range(2):
        if i == 1:
            yshift = -1
            xshift = 1
        else:
            yshift = 1
            xshift = -1

        x = point[0]
        y = point[1]

        for i in range(5):
            x = x+xshift
            y = y+yshift
            if on_board(x,y)==True and gomoku_board[x][y] == piece:
                if (x, y) not in pieces_in_row:
                    pieces_in_row.append((x, y))
            else:
                break
        if len(pieces_in_row) >= 5:
            win = True
            break
    return win

# check for overall win
def has_win(user_input, player):
    if has_horizontal_win(user_input, player)==True or has_vertical_win(user_input, player)==True \
            or has_45diagonal_win(user_input, player)==True or has_315diagonal_win(user_input, player)==True:
        return True
    else:
        return False


### ------------------------------------- Game code -------------------------------------

gomoku_board = make_board()
#print_board(gomoku_board)


while True:
    end = False
    print('''
     __          __  _                          
     \ \        / / | |                         
      \ \  /\  / /__| | ___ ___  _ __ ___   ___ 
       \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \ 
        \  /\  /  __/ | (_| (_) | | | | | |  __/
         \/  \/ \___|_|\___\___/|_| |_| |_|\___|''')
    print("                        to Gomoku!")
    print('''
    Menu: 
    1. Instructions 
    2. Play
    ''')
    while True:
        selection = input("Select: ")
        if selection == "1" or selection == "2":
            selection = int(selection)
            break
        else:
            print("Invalid selection. Please select a menu option (ex. '1').")

    if selection == 1:
        print('''
        Instructions:
        Gomoku is a 2 player game in which players take turns placing pieces on a 19x19 board. 
        The first player to have five of their pieces in a row, horizontally, vertically, or diagonally, wins the game. 
        Player 1's pieces are "o"s, and player 2's are "x"s. When it is your turn, you can place one piece on an empty 
        space on the board by entering the row number followed by a space, and the column letter in caps (ex. "14 A").
        When one of the players has gotten 5 pieces in a row, the game will automatically end and announce the winner. 
        Good luck!    
        ''')
        input("\nEnter anything to go back to main menu.")
    else:
        turn = 1
        print_board(gomoku_board)
        while True:
            if turn%2 != 0:
                player = (1, "o")
            else:
                player = (2, "x")
            print("\nIt is now player ", player[0], "’s (", player[1], ") turn to move", sep="")
            while True:
                player_input = input("Player "+str(player[0])+" ("+player[1]+") make a move: ")
                if input_valid(player_input)==False:
                    print("\nInvalid input. Format for coordinate input is row number followed by a space followed by column letter in caps (ex. '10 M')")
                elif move_valid(player_input)==False:
                    print("\nMove has to be on the board, and the space cannot be occupied.")
                else:
                    print("")
                    break
            if player[0] == 1:
                move_o(player_input)
            elif player[0] == 2:
                move_x(player_input)
            print_board(gomoku_board)
            if has_win(player_input, player[0]) == True:
                print("\nPlayer ", player[0], " (", player[1], ") has won\n", sep="")
                while True:
                    choice = input("Would you like to play again? (Y/N): ")
                    if choice == "N" or choice == "n":
                        print("Thank you for playing!")
                        end = True
                        break
                    elif choice == "Y" or choice == "y":
                        end = False
                        break
                    else:
                        print("\ninvalid input.")
                break
            turn = turn + 1
    if end==True:
        break
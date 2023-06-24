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

gomoku_board = make_board()
print_board(gomoku_board)
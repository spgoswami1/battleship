import random, copy

# Function to print board
def print_board(board):
    for row in board:
        print(row)

# Function to place ship
def place_ship(board, ship, s, x, y, orientation):
    print(ship)
    if orientation==1:
        for i in range(ship):
            board[x+i][y] = s
    elif orientation == 0:
        for i in range(ship):
            board[x][y+i] = s
    return board

# Function to check whether the ship placement is valid of Not
def validate(board, ships, x, y, orientation):
    if orientation==1 and x+ships >10:
        return False
    elif orientation == 0 and y+ships >10:
        return False
    else:
        if orientation==1:
            for i in range(ships):
                if board[x+i][y] != -1:
                    return False
        elif orientation==0:
            for i in range(ships):
                if board[x][y+1] != -1:
                    return False
    return True

# Function to get the ship orientation
def v_or_h():
	while(True):
		user_input = int(input("Orientation 0 for horizontal, 1 for vertical ? "))
		if user_input == 0 or user_input == 1:
			return user_input
		else:
			print("Invalid input. Please only enter v or h")

# This is the function to setup the ships for each player
def setup_ship(board, ships):
    #Replace 0 with ship key
    #Battleship 4, Cruiser 3, Destroyer 2, Submarine 1
    ship_code = [4, 3, 2, 1]
    count = 0
    for ship in ships.keys():
        # Getting ship coordinates from user for each ship and validating the position
        print("Now we are placing a ship : "+ship)
        # In this part we can get coordinates directly if user smart enough to not place the ships at
        # wrong locations, else we need a function to handle cases for validation
        x = int(input("Please give x coordinate(0-9 allowed) :"))
        y = int(input("Please give y coordinate(0-9 allowed) :"))
        # We can also validate Function also here just to validate whether the given co-ordinates and orientation are
        # within the given bounds
        orientation = v_or_h()
        board = place_ship(board, ships[ship], ship_code[count], x, y, orientation)
        count += 1
        print_board(board)
    input("Voila ! You have placed all ships now you are ready to battle")
    return board

# Function to check outcome of a move made by the player
def make_move(board, x, y):
    if board[x][y] == 0:
        return "miss"
    elif board[x][y] == "*" or board[x][y]=="$":
        return "try again"
    else:
        return "hit"

#To check whether a player has won or not
def check_win(board):
    # simple for loop to check all cells in 2d board
    # if any cell contains a char that is not a hit or a miss return false
    for i in range(10):
        for j in range(10):
            if board[i][j] != 0 and board[i][j] != "*" and board[i][j] != "$":
                return False
    return True

# This Function is to define the player move
def player_move(board):
    # Getting coordinated input from player to check it hit, sink or win
    x = int(input("Please give x coordinate(0-9 allowed) :"))
    y = int(input("Please give y coordinate(0-9 allowed) :"))
    res = make_move(board, x, y)
    if res == "hit":
        print("Yeah! you have hit a ship")
        board[x][y] = "$"
        if check_win(board):
            return "WIN"
    elif res == "miss":
        print("Sorry! It's a miss")
        board[x][y] = "*"
    elif res == "try again":
        print("You already guessed the co-ordinate, Please try again")

    return board

# -----------------Board Setup and Game initialization---------------
# Game Board is a 10*10 Board

# This is the main driver function
def main():
    print("It is a 2 players game. Bring your mate !!")
    print("It is a game on 10*10 Board")
    print("Let's start the game ")

    player_1 = input("Enter Player 1 Name:")
    player_2 = input("Enter Player 2 Name:")
    players = [player_1, player_2]

    # Board setup is done, players are now ready to compete
    # Let's hide the ships now
    # There are four types of ships
    # 1. Battleship [4 Units]
    # 2. Cruisers [3 Units]
    # 3. Destroyers [2 Units]
    # 4. Submarines [1 Unit]
    ships = {"Battleship":4,
             "Cruiser":3,
             "Destroyer":2,
             "Submarine":1}

    board = []
    for i in range(10):
        board_row = []
        for j in range(10):
            board_row.append(0)
        board.append(board_row)

    #Setup player1 and player2 boards
    player1_board = copy.deepcopy(board)
    player2_board = copy.deepcopy(board)

    print("This is Player1's turn to setup the ships")
    player1_board = setup_ship(player1_board, ships)
    print("This is Player2's turn to setup the ships")
    player2_board = setup_ship(player2_board, ships)

    # Main Game Loop
    while(1):
        # Player 1 is making a move now.
        print(player_1+" Your Turn")
        player2_board = player_move(player2_board)
        if player2_board == "WIN":
            print(player_1+" , Congratulation! you have won")
            print_board(player2_board)
            print_board(player1_board)
            quit()
        # Same setting for player 2 also
        print(player_2 + " Your Turn")
        player1_board = player_move(player1_board)
        if player1_board == "WIN":
            print(player_1+ " , Congratulation! you have won")
            print_board(player2_board)
            print_board(player1_board)
            quit()

main()

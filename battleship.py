from random import randint
brd = []
score = "0:0"


# Create Two Players
def player_name():

    print("Enter Player 1 Name: ")
    p1 = input()
    print("Enter Player 2 Name: ")
    p2 = input()
    print("\n" + "\n")
    print(p1 + " VERSUS " + p2 + "\n")


# Creating the board
for x in range(10):
    brd.append(["O"] * 10)


# Printing board
def show_board(brd):
    for row in brd:
        print(" ".join(row))


# Creating random points
def random_row(brd):
    return randint(0, len(brd) - 1)


def random_col(brd):
    return randint(0, len(brd[0]) - 1)


# Printing Ship Temporarildef show_ship():
   #print("Row: %s" % (ship_row1))
   # print("Column: %s" % (ship_col1))


# Play against a computer or 2 player
def choose_mode():
    print("Let's Play Battleship!")
    print("Please choose 1 player or 2 players?")
    choice = input()

    if(choice == "1"):
        print("You chose single player \nPlease input name of the player")
        p = input()
        print(p + " VERSUS Computer")
        show_board(brd)
        # Placing ship
        ship_row = random_row(brd)
        ship_col = random_col(brd)
        show_ship()
    else:
        player_name()
        # !!! ISSUE WITH PRINTING
        # Print first board
        print("Player 1 Board")
        show_board(brd)
        print("\n")
        # Place ship
        ship_row1 = random_row(brd)
        ship_col1 = random_col(brd)
        show_ship()
        # Print second board
        print("Player 2 board")
        show_board(brd)


choose_mode()


def user_guesses():
    # Input User Guesses
    for turn in range(4):
        print("Turn: ", turn + 1)
        guess_r = int(input("Guess Row: "))
        guess_c = int(input("Guess Column: "))

    # Show When Ship is Hit
    if guess_r == ship_row and guess_c == ship_col:
        print("Congratulations! You hit my battleship!")
    
    else:
        # Guess is NOT on board
        if (guess_r < 0 or guess_r > 9) or (guess_c < 0 or guess_c > 9):
            print("Oops, the coordinates are not on the board")

        # Points Already Used
        elif(brd[guess_r][guess_c] == "X"):
            print("You guessed that one already.")
        # Missed Ship
        else:
            print("Oh no! You missed!")
            brd[guess_r][guess_c] = "X"
        print("Turn: ", turn + 1)
        show_board(brd)









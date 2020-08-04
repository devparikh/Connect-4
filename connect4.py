import sys
import random 
import numpy as np 

game_started = False
replay_game = True
playing_game = True
P1_marker = '1'
P2_marker = '2'

Column_Count = 7
Row_count = 6


# Here in this function we are creating a board 
def create_board(theboard):
   # To create the board I am using numpy

   board_list =  np.zeros((6,7))
   print(board_list)

global board_list



# This function is randomly picking a player to start
def random_player_start():
    while True:
        try:
            user_input_1 = str(input("What is your name player One:"))
            Player_1 = user_input_1
            Name = user_input_1

            user_input_2 = str(input("What is your name player Two:"))

            Player_2 = user_input_2
            Name_2 = user_input_2
        except:
            while Player_1 != str:
                error_input_1 = str(input("Invalid input! What is your name player One: "))
                continue

            while Player_2 != str:
                error_input_2 = str(input("What is your name player Two"))
        else:
            break
        
        
        random_list = ["Player_1" , "Player_2"]

        Player = random.choice(random_list)

        if Player == "Player_1":
            Turn = 'Player_1'
            return Turn
            print("It is {}'s turn".format('Player_1'))
        else:
            Turn = 'Player_2'
            return Turn
            print("It is {}'s turn".format('Player_2'))

    

# Here I am placing the marker of either of the two player on there desired positions
def place_marker(theboard,marker,position):
    board_list[position] = marker 
    






# This function will tell the current player how many spaces are left on the board
def space_left_checker(board_list,position):
    # I NEED TO DO COLUNMS INSTEAD
    # Checking how many spaces are in the rows 
    def space_left_rows():
        space_left = 0
        
        for c in range(Column_Count):
            if Column_Count-1 and Column_Count -2 and Column_Count-3 and Column_Count -4 and Column_Count -5 and Column_Count -6 and Column_Count-7 == '0.':
                return True
                space_left = space_left + 7
            
            if Column_Count - 1 and Column_Count - 2 and Column_Count - 3 and Column_Count - 4 and Column_Count - 5 and Column_Count - 6 == '0.':
                return True
                space_left = space_left + 6
            if Column_Count - 1 and Column_Count - 2 and Column_Count - 3 and Column_Count - 4 and Column_Count - 5 == '0.':
                return True
                space_left = space_left + 5
            
            if Column_Count - 1 and Column_Count - 2 and Column_Count - 3 and Column_Count - 4:
                return True
                space_left = space_left + 4
                
             
            if Column_Count-1 and Column_Count-2 and Column_Count - 3 == '0.':
                return True
                space_left = space_left + 3
                 
            if Column_Count-1 and Column_Count -2 == '0':
                return True 
                space_left = space_left + 2
            
            if Column_Count -1 == '0.':
                return True
                space_left = space_left +1 

            return space_left  
# Here I am checking if the entire board is full and to see if there is a tie
def full_board(theboard):
    for position in range(1,43):
        if space_left_checker(board_list,position):
            return False
        return True

# Here I am making sure that the player input is a number in the board
def player_choice(*args):
    position  = 0

    while position not in range(1,43) or not space_left_checker(board_list,position):
        position = int(input("Choose an input from 1 to 42"))
    return position




def win_check(*args):
    # Here I split up the check into rows, columns, and horizontals
    def check_horizontals():
        # Here we can use if statements to check if 4 consecutive positions are taken by a certain player and check all of the combinations
        for c in range(Column_Count-3):
            for r in range(Row_count):
                
                if board_list[c][r+1] and board_list[c][r+1] and board_list[c][r+2] and board_list[c][r+3] == '1':
                    print("Player 1 has won")
                    winner = 'Player_1'
                elif board_list[c][r] and board_list[c][r+1] and board_list[c][r+2] and board_list[c][r+3] == '2':
                    print("Player 2 has won!")
                    winner = 'Player_2'
                    

    def check_vertical():
        for c in range(Column_Count-3):
            for r in range(Row_count):
                if board_list[c][r] and board_list[c][r+1] and board_list[c][r+2] and board_list[c][r+3] == '1':
                    print("Player 1 has won")
                    winner = 'Player_1'
                elif board_list[c][r] and board_list[c][r+1] and board_list[c][r+2] and board_list[c][r+3] == '2':
                    print("Player 2 has won")
                    winner = 'Player_2'

    def diagnols_positivly_sloped():
        for c in range(Column_Count -3):
            for r in range(Row_count - 3):
                if [r][c] and [r+1][c+1] and [r+2][c+2] and [r+3][c+3] == '1':
                    print("Player 1 has won!")
                    winner = 'Player_1'
                elif [r][c] and [r+1][c+1] and [r+2][c+2] and [r+3][c+3] == '2':
                    print("Player 2 has won!")
                    winner = 'Player_2'
    def diagnols_negetivly_sloped():
        for c in range(Column_Count - 3):
            for r in range(Row_count - 3):
                if [r][c] and [r-1][c-1] and [r-2][c-2] and [r-3][c-3] == '1':
                    print("Player 1 has won!")
                    winner = 'Player_2'
# This function asks if the winner wants to play again
def replay(*args):
    # Here I am 
    replay_input = str(input("Do you want to play again? YES or NO"))
    return replay_input == 'YES'
       

def connect4(*args):
    global board_list
    board_list = np.zeros((6,7))



    theboard = np.zeros((6,7))
    print(theboard)
    random_player_start()

    Turn = random_player_start
        
        
    play_game = input("Do you want to play? YES or NO").lower()
    if play_game == 'yes':
        game_on = True
    else:
        game_on = False



    while game_on == True:
        if Turn == 'Player_1': 
                position = player_choice(board_list)
                place_marker(theboard,P1_marker,position)

                if win_check(theboard,P1_marker):
                    create_board(theboard)
                    print("Player 1 has won")
                    
                    game_on = False
                else:
                    if full_board(theboard):
                        print("The game is a tie!")
                        game_one = False
                    else:
                        Turn = 'Player_2'
        else:
                Position = player_choice(board_list)
                place_marker(theboard,P1_marker,position)

                if win_check(theboard,P2_marker):
                    create_board(theboard)
                    print("Player 2 has won")
                    
                    game_on = False
                else:
                    if full_board(theboard):
                        print("The game is a tie!")
                        game_one = False
                    else:
                        Turn = 'Player_1'

connect4()

            
            
            


            


                
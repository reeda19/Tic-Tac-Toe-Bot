import sys
computer_win = False #global variable that checks if computer has won

def check_for_two(x, o):
     #checking rows
    for i in range (0, 7, 3):
        count_row = 0
        row_x  = False
        vacancy_row=None
        for j in range (i,i+3):
            if elements[j]==x:
              count_row+=1
            elif not elements[j] == o:
                vacancy_row = j
        if(count_row>=2 and vacancy_row is not None):
            return vacancy_row

    #checking columns
    for i in range (3):
        vacancy_col=None
        count_column = 0
        col_x = False
        for j in range (i, i+7, 3):
            if elements[j] == x:
                count_column += 1
            elif not elements[j] == o:
                vacancy_col = j
        if(count_column>=2 and vacancy_col is not None):
            return vacancy_col
    return -1

#checks if there is an 'x' in 2 opposite corners. If so, returns a middle space on the outer ring as a countermove
def check_corners():
    if(elements[0]=='X' and elements[8]=='X') or (elements[2]=='X' and elements[6]=='X'):
        #if space is empty, return that space
        if elements[1]==' ':
            return 1
        elif elements[3]==' ':
            return 3
        elif elements[5]==' ':
            return 5
        elif elements[7]==' ':
            return 7
    return -1
#computer moves in a random position
def go_random():
    try:
        return elements.index(' ')
    except ValueError:
        print('It\'s a tie!')
        #exit here
#places on 'O' for the computer
def computer_move():

    #check for two O's in a row
    win = check_for_two('O','X')
    if win>=0:
       elements[win] = 'O'
       global computer_win
       computer_win = True
       return

    #check for corners
    corners = check_corners()
    if corners>=0:
        elements[corners] = 'O'
        return
    
    #If center square is open, go there
    elif elements[4] == ' ':
        elements[4] = 'O'
        return


    two = check_for_two('X','O')
    if two>=0:
        elements[two] = 'O'
        return


    #Go random if no other moves are open
    elements[go_random()] = 'O'
    return

elements = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
#continuously executed until game is over. Main function
while True:
    #Tic tac toe grid that is formatted using elements of an array
    grid = ("""
   {} | {} | {}
  ___|___|___
   {} | {} | {} 
  ___|___|___
   {} | {} | {}
     |   |
     """).format(elements[0],elements[1],elements[2],elements[3],elements[4],elements[5],elements[6],elements[7],elements[8])
    print(grid)

    #checks if computer has 3 in a row
    if computer_win:
        print("Computer has won!")
        exit(0)
    #repeats until player correctly executes a move
    while True:
        try:
            user_input=int(input('Where would you like to go: '))
            if user_input<0 or user_input>8: #out of bounds
               print('Please enter a number between 0 and 8 inclusive')
            elif not elements[user_input]== ' ': #space is not empty
               print('Please choose an open space')
            else:
             elements[user_input]='X' #place X in user position if available
             break
        except ValueError: #not an integer
            print('Please enter a valid integer')
    #computer's turn
    computer_move()
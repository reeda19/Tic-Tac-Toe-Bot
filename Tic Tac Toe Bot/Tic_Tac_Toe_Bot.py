def check_for_two(x, o):
    for r in range (3):
        count_row = 0
        count_column = 0
        row_x  = False
        col_x = False
        vacancy_row=None
        vacancy_col=None
        for c in range(3):
            if elements[r][c]==x:
                count_row+=1
            elif elements[r][c]==o:
                row_x = True
            else:
                vacancy_row=[r, c]
            if elements[c][r]==x:
                count_column+=1
            elif elements[c][r]==o:
                col_x = True
            else:
                vacancy_col=[c, r]
        if(count_column>=2 and not col_x):
            return vacancy_col
        elif(count_row>=2 and not row_x):
            return vacancy_row
    return []

def check_corners():
    if(elements[0][0]=='X' and elements[2][2]=='X') or (elements[0][2]=='X' and elements[2][0]=='X'):
        if elements[0][1]==' ':
            return [0, 1]
        elif elements[1][0]==' ':
            return [1, 0]
        elif elements[1][2]==' ':
            return [1, 2]
        elif elements[2][1]==' ':
            return [2, 1]
    return []
def computer_move():
    win = check_for_two('O','X')
    corners = check_corners()
    if len(win):
        elements[win[0]][win[1]] = 'O'
        return
    elif elements[1][1] == ' ':
        elements[1][1] = 'O'
        return
    two = check_for_two('X','O')
    if len(two)>0:
        elements[two[0]][two[1]] = 'O'
        return
    elif elements[1][1] == ' ':
        elements[1][1] = 'O'
        return
    if len(corners)>0:
        elements[corners[0]][corners[1]] = 'O'

elements = [[' ', ' ', ' '],[' ', ' ', ' '], [' ', ' ', ' ']]
while True:
    grid = ("""
   {} | {} | {}
  ___|___|___
   {} | {} | {}
  ___|___|___
   {} | {} | {}
     |   |
     """).format(elements[0][0],elements[0][1],elements[0][2],elements[1][0],elements[1][1],elements[1][2],elements[2][0],elements[2][1],elements[2][2])
    print(grid)
    while True:
        try:
            user_input=int(input('Where would you like to go: '))
            if user_input<0 or user_input>8: #out of bounds
               print('Please enter a number between 0 and 8 inclusive')
            elif not elements[int(user_input/3)][int(user_input%3)]== ' ':
               print('Please choose an open space')
            else:
             elements[int(user_input/3)][int(user_input%3)]='X'
             break
        except ValueError: #not an integer
            print('Please enter a valid integer')
      
    computer_move()
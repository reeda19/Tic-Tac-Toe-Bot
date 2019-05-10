def computer_move():
    print('filler')
elements = [[' ', ' ', ' '],[' ', ' ', ' '], [' ', ' ', 'X']]
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
    user_input=int(input('Where would you like to go?'))
    elements[int(user_input/3)][int(user_input%3)]='O'
    computer_move()
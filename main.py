
def check_cell(field, row, column):
    system = [[-1 , -1] , [-1 , 0] , [-1 , 1] , [0 , -1] , [0 , 1] , [1 , -1] , [1 , 0] , [1 , 1]]
    count = 0
    for i in system:
        x = row + i[0]
        y = column + i[1]

        if x == -1:
            x = len(field[row]) - 1
        if y == -1:
            y = len(field[column]) - 1

        if x == 5:
            x = 0
        if y == 5:
            y = 0

        if field[x][y] == 'x':
            count += 1

    if field[row][column] == '.':
        return count == 3
    if field[row][column] == 'x':
        return count == 2 or count == 3
    return False

def nextCircle(field):
    field_new = ['',
                 '',
                 '',
                 '',
                 '']

    for row in range(len(field)):
        for column in range(len(field[row])):
            if check_cell(field, row, column):
                field_new[row] += 'x'
            else:
                field_new[row] += '.'

    #print('\n'.join(field_new) + '\n')

    return field_new


field = ['.....',
         '..x..',
         'x....',
         '..x..',
         '.....']

nextCircle(field)
import random

#Checking neighbors of cell
def check_cell(field, row, column):
    system = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    count = 0
    for i in system:
        x = row + i[0]
        y = column + i[1]

        if x == -1:
            x = len(field[row]) - 1
        if y == -1:
            y = len(field[column]) - 1

        if x == len(field):
            x = 0
        if y == len(field[0]):
            y = 0

        if field[x][y] == 'x':
            count += 1

    if field[row][column] == '.':
        return count == 3
    if field[row][column] == 'x':
        return count == 2 or count == 3
    return False


#NEXT STATION OF FIELD
def nextCircle(field):
    field_new = []

    for row in range(len(field)):
        field_new.append('')
        for column in range(len(field[row])):
            if check_cell(field, row, column):
                field_new[row] += 'x'
            else:
                field_new[row] += '.'

    # print('\n'.join(field_new) + '\n')

    return field_new


#CREATING RANDOM FIELD WITH WIDTH(ROWS) AND HEIGHT(COLUMNS)
def randomField(rows, columns):
    field = []
    for row in range(rows):
        field.append('')
        for column in range(columns):
            rand = random.random()
            if rand>0.85:
                symb = 'x'
            else:
                symb = '.'
            field[row] += symb
    return field


#START POINT
if __name__ == '__main__':
    print("Количество циклов:")
    cycle = int(input())
    print("Размер сетки:")
    rows = int(input())
    columns = int(input())
    field = randomField(rows,columns)
    print('\n'.join(field) + '\n')
    field_new = []
    for i in range(cycle):
        field_new = nextCircle(field)
    print('\n'.join(field_new) + '\n')

import main

def test_nextStateExcpected():
    field = ['.....',
             '..x..',
             'x....',
             '..x..',
             '.....']

    field_expected = ['.....',
                      '.....',
                      '.x...',
                      '.....',
                      '.....']

    assert main.nextCircle(field) == field_expected

def test_nextStateExcpectedWrong():
    field = ['.....',
             '..x..',
             'x....',
             '..x..',
             '.....']

    field_expected = ['.....',
                      '.....',
                      '.....',
                      '.....',
                      '.....']

    assert main.nextCircle(field) != field_expected

def test_randomField():
    field = main.randomField(6,7)
    assert len(field) == 6 and len(field[0]) == 7

def test_randomFieldSameSize():
    field = main.randomField(10,10)
    assert len(field) == 10 and len(field[0]) == 10

def test_CheckCell():
    field = ['.....',
             '..x..',
             'x....',
             '..x..',
             '.....']
    assert !main.check_cell(field, 0, 0)

def test_CheckCellTrue():
    field = ['.....',
             '..x..',
             'x....',
             '..x..',
             '.....']
    assert main.check_cell(field, 2, 1) == True

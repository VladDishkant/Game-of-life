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
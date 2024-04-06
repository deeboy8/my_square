def middle(row, column):
    empty_spaces = row - 2
    x = 0
    while x < column - 2:
        print('|', end="")
        i = 0
        while i < empty_spaces:
            print(' ', end="")
            i += 1
        print('|')
        x += 1


def top_and_bottom(row):
    dashes = row - 2
    if row <= 2:
        i = 0
        while i < row - 1:
            print('o', end="")
            i += 1
    else:
        print('o', end="")
        i = 0
        while i < dashes:
            print('-', end=""); i += 1
    print('o')


def my_square(row, column):
    if row == 0 or column == 0:
        exit
    else:
        if row and column == 1:
            print('o')
            exit
        else:
            top_and_bottom(row)
            if column > 2:
                middle(row, column)
            top_and_bottom(row)
            
square = my_square(7, 4)
print(square)
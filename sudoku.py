import sys


# UTILS

def parse_file(filename):
    with open(filename) as f:
        content = f.readlines()
    return [[[int(i)] for i in list(line.strip())] for line in content]

def fill_possibilities(p):
    return [[cell if cell != [0] else [1,2,3,4,5,6,7,8,9] for cell in row] for row in p]

def do_algorithm(algorithm, a):
    changed = True
    i = 0
    while changed == True:
        changed = algorithm(a)
        i += 1
    return i

# checking

def is_solved(a):
    for row in a:
        for cell in row:
            if len(cell) != 1:
                return False
    return True

# elements

def column(a, c):
    return [r[c] for r in a]

def block(a, x, y):
    return [cell for row in a[x:x+3] for cell in row[y:y+3]]

def block_of_cell(a, x, y):
    i, j = (x//3)*3, (y//3)*3 # floor to nearest multiple of 3
    return block(a, i, j)

# display

def print_incomplete(a, filled=True):
    for row in a:
        for cell in row:
            if len(cell) > 1 or filled == True:
                print('{:10}'.format(str(cell).strip('[]').replace(' ', '').replace(',', '')), end='')
            else:
                print('{:10}'.format(''), end='')
        print()

def print_complete(a):
    print('\n'.join([' '.join([str(item) for cell in row for item in cell]) for row in a]))


# ALGORITHM 1: Pruning

def prune_cells_once(a):
    changed = False
    for i, row in enumerate(a):
        for j, cell in enumerate(row):
            if len(cell) == 1:
                continue

            all_cells = row + column(a, j) + block_of_cell(a, i, j)
            all_filled = [cell[0] for cell in all_cells if len(cell) == 1]
            new_cell = [k for k in cell if k not in all_filled]

            if new_cell == cell:
                continue
            else:
                a[i][j] = new_cell
                changed = True

    return changed


# ALGORITHM 2: Find Uniques

def find_uniques_once(a):
    changed = False
    
    for r in range(0, 9):
        for c in range(0, 9):
            if len(a[r][c]) == 1:
                continue
            
            possibilities_row = [item for cell in a[r] for item in cell]
            possibilities_col = [item for cell in column(a, c) for item in cell]
            possibilities_blk = [item for cell in block_of_cell(a, r, c) for item in cell]

            for item in a[r][c]:
                if possibilities_row.count(item) == 1 or possibilities_col.count(item) == 1 or possibilities_blk.count(item) == 1:
                    a[r][c] = [item]
                    changed = True

    return changed


if __name__ == '__main__':
    p = parse_file(sys.argv[1])
    a = fill_possibilities(p)
    
    prune_iterations = 0
    uniques_iterations = 0

    while not is_solved(a):
        try:
            prune_iterations += do_algorithm(prune_cells_once, a)

            if is_solved(a):
                break

            uniques_iterations += do_algorithm(find_uniques_once, a)
        except KeyboardInterrupt:
            print()
            print_incomplete(a)
            sys.exit(0)

    print_complete(a)
    print('iterations: {} / {}'.format(prune_iterations, uniques_iterations))


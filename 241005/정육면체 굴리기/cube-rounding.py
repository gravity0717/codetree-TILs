import sys 

n, m, x, y, k = map(int, sys.stdin.readline().split())
board = [list(map(int, input().split())) for _ in range(n)]
directions =  list(map(int, input().split()))
dice = [0] * 6

def move_east(dice, x, y):
    if 0 <= x+1 < m:
    #   0    1    2  3  4   5
        bot, top, west, east, south, north = dice 
        # roll to east 
        dice[0], dice[1], dice[2], dice[3] = east, west, bot, top 
        x += 1 
        return dice, x, y, True
    return dice, x, y, False

def move_west(dice, x, y):
    if 0 <= x - 1 < m: 
    #   0    1    2  3  4   5
        bot, top, west, east, south, north = dice 
        # roll to west 
        dice[0], dice[1], dice[2], dice[3] = west, east, top, bot
        x -= 1 
        return dice, x, y, True
    return dice, x, y, False
    
def move_north(dice, x, y):
    if 0 <= y - 1 < n:
        #   0    1    2  3  4   5
        bot, top, west, east, south, north = dice 
        # roll to east 
        dice[0], dice[1], dice[4], dice[5] = north, south, bot, top
        y -= 1 
        return dice, x, y, True
    return dice, x, y, False

def move_south(dice, x, y):
    if 0 <= y + 1 < n:
        #   0    1    2  3  4   5
        bot, top, west, east, south, north = dice 
        # roll to east 
        dice[0], dice[1], dice[4], dice[5] = south, north, top, bot
        y += 1 
        return dice, x, y, True
    return dice, x, y, False

move_funcs = [None, move_east, move_west, move_north, move_south]
for d in directions:
    dice, x, y, flag = move_funcs[d](dice, x, y)
    
    if flag == False:
        continue

    if board[y][x] == 0:
        board[y][x] = dice[0]
    else:
        dice[0] = board[y][x]
        board[y][x] = 0 

    print(dice[1])
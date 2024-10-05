import sys 

n, m, x, y, k = map(int, sys.stdin.readline().split())
board = [list(map(int, input().split())) for _ in range(n)]
directions =  list(map(int, input().split()))
dice = [0] * 6
dx , dy = [0, 0, 0, -1, 1], [0, 1, -1, 0, 0] # arr[y][x] 이렇게 하는 대신 변위를 뒤집자 

def is_in_range(x,y):
    return 0<=x and x < n and 0<= y and y<m

def roll_east(dice):
    #   0    1    2  3  4   5
    bot, top, west, east, south, north = dice 
    # roll to east 
    dice[0], dice[1], dice[2], dice[3] = east, west, bot, top 
    return dice

def roll_west(dice):
    #   0    1    2  3  4   5
    bot, top, west, east, south, north = dice 
    # roll to west 
    dice[0], dice[1], dice[2], dice[3] = west, east, top, bot
    return dice
    
def roll_north(dice):
    #   0    1    2  3  4   5
    bot, top, west, east, south, north = dice 
    # roll to east 
    dice[0], dice[1], dice[4], dice[5] = north, south, bot, top
    return dice

def roll_south(dice):
    #   0    1    2  3  4   5
    bot, top, west, east, south, north = dice 
    # roll to east 
    dice[0], dice[1], dice[4], dice[5] = south, north, top, bot
    return dice

roll_funcs = [None, roll_east, roll_west, roll_north, roll_south]
for d in directions:
    nx, ny = x + dx[d], y + dy[d]
    if is_in_range(nx,ny):
        x, y = nx, ny 
        dice = roll_funcs[d](dice)
        if board[x][y] == 0:
            board[x][y] = dice[0]
        else:
            dice[0] = board[x][y]
            board[x][y] = 0 
    
        print(dice[1])
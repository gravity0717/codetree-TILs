import sys

def solve():
    sys.setrecursionlimit(10000)  # 재귀 깊이 제한을 늘림

    # 보드 크기 입력
    N, M = map(int, sys.stdin.readline().rstrip().split())
    board = [list(sys.stdin.readline().strip()) for _ in range(N)]

    # R과 B의 초기 위치 찾기
    rx, ry, bx, by = -1, -1, -1, -1
    for y in range(N):
        for x in range(M):
            if board[y][x] == 'R':
                rx, ry = x, y
            elif board[y][x] == 'B':
                bx, by = x, y

    # 이동 방향 정의: 상, 하, 좌, 우
    directions = [(-1,0), (1,0), (0,-1), (0,1)]  # 상, 하, 좌, 우

    # 최소 이동 횟수를 저장할 변수
    min_moves = [float('inf')]

    # 구슬을 이동시키는 함수
    def move(x, y, dx, dy):
        count = 0  # 이동 횟수
        while True:
            if board[y + dy][x + dx] == '#':  # 벽을 만나면 멈춤
                break
            x += dx
            y += dy
            count +=1
            if board[y][x] == 'O':  # 구멍에 빠지면 멈춤
                break
        return x, y, count

    # 백트래킹 함수
    def backtrack(rx, ry, bx, by, depth, visited):
        # 이동 횟수가 10회를 초과하면 포기
        if depth > 10:
            return

        for dx, dy in directions:
            # R과 B를 이동
            nrx, nry, r_count = move(rx, ry, dx, dy)
            nbx, nby, b_count = move(bx, by, dx, dy)

            # B가 구멍에 빠졌으면 이 경로는 실패
            if board[nby][nbx] == 'O':
                continue  # 다음 방향 시도

            # R이 구멍에 빠졌고 B는 안 빠졌으면 성공
            if board[nry][nrx] == 'O':
                min_moves[0] = min(min_moves[0], depth)
                continue  # 다음 방향 시도

            # 두 구슬이 같은 위치에 있다면
            if nrx == nbx and nry == nby:
                if r_count > b_count:
                    nrx -= dx
                    nry -= dy
                else:
                    nbx -= dx
                    nby -= dy

            # 이미 방문한 상태라면 포기
            if (nrx, nry, nbx, nby) in visited:
                continue

            # 새로운 상태를 방문으로 표시하고 재귀 호출
            visited.add((nrx, nry, nbx, nby))
            backtrack(nrx, nry, nbx, nby, depth +1, visited)
            visited.remove((nrx, nry, nbx, nby))  # 백트래킹

    # 방문한 상태를 추적하기 위한 집합
    visited = set()
    visited.add((rx, ry, bx, by))

    # 백트래킹 시작
    backtrack(rx, ry, bx, by, 1, visited)

    # 결과 출력
    if min_moves[0] <=10:
        print(min_moves[0])
    else:
        print(-1)

if __name__ == "__main__":
    solve()
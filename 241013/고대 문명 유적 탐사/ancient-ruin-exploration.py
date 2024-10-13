from collections import deque
import sys
import copy

def input():
    return sys.stdin.readline()

def rotate_3x3(subgrid, angle):
    # Rotate the 3x3 subgrid by the given angle clockwise
    # angle is one of [90, 180, 270]
    grid = copy.deepcopy(subgrid)
    for _ in range(angle // 90):
        # Perform 90 degree rotation
        grid = [list(row) for row in zip(*grid[::-1])]
    return grid

def find_artifacts(grid):
    visited = [[False]*5 for _ in range(5)]
    artifacts = []
    for i in range(5):
        for j in range(5):
            if not visited[i][j]:
                q = deque()
                q.append((i,j))
                visited[i][j] = True
                same = [(i,j)]
                while q:
                    x, y = q.popleft()
                    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx <5 and 0 <= ny <5 and not visited[nx][ny] and grid[nx][ny] == grid[i][j]:
                            visited[nx][ny] = True
                            q.append((nx, ny))
                            same.append((nx, ny))
                if len(same) >=3:
                    artifacts.append(same)
    return artifacts

def fill_grid(grid, artifacts, wall, wall_ptr):
    # Remove artifacts
    for artifact in artifacts:
        for x, y in artifact:
            grid[x][y] = 0  # 0 represents empty

    # Collect empty positions
    empty = []
    for c in range(5):
        for r in reversed(range(5)):
            if grid[r][c] == 0:
                empty.append((r, c))
    
    # Fill empty positions with wall pieces
    for pos in empty:
        if wall_ptr >= len(wall):
            wall_ptr = 0
        grid[pos[0]][pos[1]] = wall[wall_ptr]
        wall_ptr +=1
    return grid, wall_ptr

def simulate(grid, subgrid_top_left, angle, wall, wall_ptr):
    # Make a deep copy of the grid to simulate
    temp_grid = copy.deepcopy(grid)
    r, c = subgrid_top_left
    # Extract the 3x3 subgrid
    sub = [row[c:c+3] for row in temp_grid[r:r+3]]
    # Rotate the subgrid
    rotated = rotate_3x3(sub, angle)
    # Put it back
    for i in range(3):
        for j in range(3):
            temp_grid[r+i][c+j] = rotated[i][j]
    total_value = 0
    current_wall_ptr = wall_ptr

    while True:
        artifacts = find_artifacts(temp_grid)
        if not artifacts:
            break
        # Calculate value
        for artifact in artifacts:
            total_value += len(artifact)
        # Remove artifacts and fill
        temp_grid, current_wall_ptr = fill_grid(temp_grid, artifacts, wall, current_wall_ptr)
    return total_value, temp_grid, current_wall_ptr

def main():
    import sys
    sys.setrecursionlimit(10000)
    K, M = map(int, sys.stdin.readline().split())
    grid = []
    for _ in range(5):
        grid.append(list(map(int, sys.stdin.readline().split())))
    wall = list(map(int, sys.stdin.readline().split()))
    wall_len = len(wall)
    wall_ptr =0
    results = []
    for _ in range(K):
        max_value = -1
        best_angle = 0
        best_r = 0
        best_c = 0
        best_grid = []
        best_wall_ptr = wall_ptr
        # Iterate over all possible 3x3 subgrids
        for r in range(0,3):
            for c in range(0,3):
                for angle in [90, 180, 270]:
                    value, new_grid, new_wall_ptr = simulate(grid, (r, c), angle, wall, wall_ptr)
                    if value > max_value:
                        max_value = value
                        best_angle = angle
                        best_r = r
                        best_c = c
                        best_grid = new_grid
                        best_wall_ptr = new_wall_ptr
                    elif value == max_value:
                        if angle < best_angle:
                            best_angle = angle
                            best_r = r
                            best_c = c
                            best_grid = new_grid
                            best_wall_ptr = new_wall_ptr
                        elif angle == best_angle:
                            if c < best_c or (c == best_c and r < best_r):
                                best_r = r
                                best_c = c
                                best_grid = new_grid
                                best_wall_ptr = new_wall_ptr
        if max_value ==0:
            break
        results.append(max_value)
        grid = best_grid
        wall_ptr = best_wall_ptr
    print(*results)


if __name__ == "__main__":
    main()
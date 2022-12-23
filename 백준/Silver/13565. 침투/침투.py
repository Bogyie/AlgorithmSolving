
def main():
    m, n = map(int, input().split())
    arr = tuple(tuple(map(lambda x: x == '0', input())) for _ in range(m))

    search = ((-1, 0,), (1, 0,), (0, -1,), (0, 1,),)
    visit = [[False for _ in range(n)] for _ in range(m)]

    stack = [(0, i,) for i, v in enumerate(arr[0]) if v]
    for s in stack:
        row, col = s
        visit[row][col] = True

    while stack:
        curr = stack.pop()  # current row, current column
        for delta in search:  # delta row, delta column
            nr, nc = map(sum, zip(curr, delta))
            if 0 <= nr < m and 0 <= nc < n:  # bound check

                if nr == m - 1:
                    return True

                # visit, can go check
                if visit[nr][nc] or not arr[nr][nc]:
                    continue
                visit[nr][nc] = True
                stack.append((nr, nc,))

    return False


print("YES" if main() else "NO")

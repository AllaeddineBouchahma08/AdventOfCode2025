def solve():
    with open("input.txt", "r", encoding="utf-8") as f:
        lines = [line.rstrip("\n") for line in f if line.strip()]

    if not lines:
        print(0)
        return

    rows = len(lines)
    cols = len(lines[0])
    grid = [list(line) for line in lines]

    dirs = [(-1, -1), (-1, 0), (-1, 1),
            ( 0, -1),          ( 0, 1),
            ( 1, -1), ( 1, 0), ( 1, 1)]

    accessible = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != "@":
                continue
            neigh = 0
            for dr, dc in dirs:
                rr, cc = r + dr, c + dc
                if 0 <= rr < rows and 0 <= cc < cols and grid[rr][cc] == "@":
                    neigh += 1
                    if neigh >= 4:
                        break
            if neigh < 4:
                accessible += 1

    print(accessible)


if __name__ == "__main__":
    solve()

def solve():
    with open("input.txt", "r", encoding="utf-8") as f:
        lines = [line.rstrip("\n") for line in f if line.strip()]

    rows = len(lines)
    cols = len(lines[0])
    grid = [list(row) for row in lines]

    dirs = [(-1, -1), (-1, 0), (-1, 1),
            ( 0, -1),          ( 0, 1),
            ( 1, -1), ( 1, 0), ( 1, 1)]

    def count_adjacent(r, c):
        cnt = 0
        for dr, dc in dirs:
            rr, cc = r + dr, c + dc
            if 0 <= rr < rows and 0 <= cc < cols and grid[rr][cc] == "@":
                cnt += 1
        return cnt

    total_removed = 0

    while True:
        to_remove = []

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "@":
                    if count_adjacent(r, c) < 4:
                        to_remove.append((r, c))

        if not to_remove:
            break

        # remove them
        for r, c in to_remove:
            grid[r][c] = "."
        total_removed += len(to_remove)

    print(total_removed)


if __name__ == "__main__":
    solve()

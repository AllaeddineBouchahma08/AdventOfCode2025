def solve():
    with open("input.txt", "r", encoding="utf-8") as f:
        lines = [line.rstrip("\n") for line in f]

    width = max(len(line) for line in lines)
    grid = [line.ljust(width) for line in lines]
    height = len(grid)

    in_block = False
    blocks = []
    cur_start = None

    for c in range(width):
        col = [grid[r][c] for r in range(height)]
        empty = all(ch == " " for ch in col)

        if not empty and not in_block:
            in_block = True
            cur_start = c

        if empty and in_block:
            in_block = False
            blocks.append((cur_start, c - 1))

    if in_block:
        blocks.append((cur_start, width - 1))

    total_sum = 0

    for start, end in blocks:
        op = None
        op_row = None
        for r in range(height - 1, -1, -1):
            seg = grid[r][start:end+1].strip()
            if seg in ("+", "*"):
                op = seg
                op_row = r
                break

        numbers = []
        for c in range(end, start - 1, -1):
            digits = []
            for r in range(op_row):
                ch = grid[r][c]
                if ch.isdigit():
                    digits.append(ch)
            if digits:
                num = int("".join(digits))
                numbers.append(num)

        if op == "+":
            val = sum(numbers)
        else:
            val = 1
            for x in numbers:
                val *= x

        total_sum += val

    print(total_sum)


if __name__ == "__main__":
    solve()

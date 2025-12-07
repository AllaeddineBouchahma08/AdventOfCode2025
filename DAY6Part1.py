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
        for r in range(height - 1, -1, -1):
            segment = grid[r][start:end+1].strip()
            if segment in ("+", "*"):
                op = segment
                op_row = r
                break

        nums = []
        for r in range(op_row):
            segment = grid[r][start:end+1].strip()
            if segment:
                nums.append(int(segment))

        
        if op == "+":
            val = sum(nums)
        else:
            val = 1
            for x in nums:
                val *= x

        total_sum += val

    print(total_sum)


if __name__ == "__main__":
    solve()

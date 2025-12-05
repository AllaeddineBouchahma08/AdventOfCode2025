def solve():
    with open("input.txt", "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f]

    # Split on blank line: first part is ranges, second part is ingredient IDs
    blank_index = lines.index("")
    range_lines = lines[0:blank_index]
    id_lines = lines[blank_index+1:]

    ranges = []
    for r in range_lines:
        a, b = r.split("-")
        ranges.append((int(a), int(b)))

    ids = [int(x) for x in id_lines]

    fresh_count = 0

    for x in ids:
        for lo, hi in ranges:
            if lo <= x <= hi:
                fresh_count += 1
                break

    print(fresh_count)


if __name__ == "__main__":
    solve()

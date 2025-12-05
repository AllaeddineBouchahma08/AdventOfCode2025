def solve():
    with open("input.txt", "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f]

    blank_index = lines.index("")
    range_lines = lines[0:blank_index]

    ranges = []
    for r in range_lines:
        a, b = r.split("-")
        ranges.append((int(a), int(b)))

    ranges.sort()
    merged = []
    cur_lo, cur_hi = ranges[0]

    for lo, hi in ranges[1:]:
        if lo <= cur_hi + 1:   
            cur_hi = max(cur_hi, hi)
        else:
            merged.append((cur_lo, cur_hi))
            cur_lo, cur_hi = lo, hi

    merged.append((cur_lo, cur_hi))

    total = 0
    for lo, hi in merged:
        total += (hi - lo + 1)

    print(total)


if __name__ == "__main__":
    solve()

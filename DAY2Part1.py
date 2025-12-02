def is_invalid_id(n: int) -> bool:
    s = str(n)
    if len(s) % 2 != 0:
        return False
    mid = len(s) // 2
    return s[:mid] == s[mid:]

def solve():
    with open("input.txt", "r") as f:
        line = f.read().strip()

    total = 0

    # split ranges
    for part in line.split(","):
        if not part:
            continue
        lo, hi = map(int, part.split("-"))

        for x in range(lo, hi + 1):
            if is_invalid_id(x):
                total += x

    print(total)


if __name__ == "__main__":
    solve()

def is_invalid_id(n: int) -> bool:
    s = str(n)
    L = len(s)

    for k in range(1, L // 2 + 1):
        if L % k != 0:
            continue
        block = s[:k]
        if block * (L // k) == s:
            return True

    return False


def solve():
    with open("input.txt", "r") as f:
        line = f.read().strip()

    total = 0

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

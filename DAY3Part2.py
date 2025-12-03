def solve():
    with open("input.txt", "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    def max_k_digits(s: str, k: int) -> int:
        n = len(s)
        to_remove = n - k
        stack = []

        for c in s:
            while to_remove > 0 and stack and stack[-1] < c:
                stack.pop()
                to_remove -= 1
            stack.append(c)

        result = stack[:k]

        return int("".join(result))

    K = 12
    total = 0

    for line in lines:
        total += max_k_digits(line, K)

    print(total)


if __name__ == "__main__":
    solve()

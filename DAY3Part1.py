def solve():
    with open("input.txt", "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    def max_joltage_from_line(s: str) -> int:
        if len(s) < 2:
            return 0

        digits = [ord(c) - 48 for c in s]
        n = len(digits)
        best = 0

        for i in range(n - 1):
            tens = digits[i]
            ones = max(digits[i+1:]) 
            val = tens * 10 + ones

            if val > best:
                best = val
                if best == 99:  
                    return 99

        return best

    total = 0
    for line in lines:
        total += max_joltage_from_line(line)

    print(total)


if __name__ == "__main__":
    solve()

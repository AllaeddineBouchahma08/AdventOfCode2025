def solve():
    with open("input.txt", "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    pos = 50
    hits = 0

    for line in lines:
        direction = line[0]
        steps = int(line[1:])

        if direction == "L":
            pos = (pos - steps) % 100
        else:
            pos = (pos + steps) % 100

        if pos == 0:
            hits += 1

    print("Password =", hits)


if __name__ == "__main__":
    solve()

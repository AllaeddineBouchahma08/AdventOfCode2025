def solve():
    with open("input.txt", "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    pos = 50
    hits = 0

    for line in lines:
        direction = line[0]
        steps = int(line[1:])

        if direction == "R":
            k0 = (-pos) % 100
        else:
            k0 = pos % 100

        if k0 == 0:
            k0 = 100  

        if k0 <= steps:
            hits += 1 + (steps - k0) // 100

        if direction == "R":
            pos = (pos + steps) % 100
        else:
            pos = (pos - steps) % 100

    print("Password =", hits)


if __name__ == "__main__":
    solve()

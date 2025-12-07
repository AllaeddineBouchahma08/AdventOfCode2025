def solve():
    with open("input.txt", "r") as f:
        lines = [line.rstrip('\n') for line in f]
    
    grid = lines
    height = len(grid)
    width = len(grid[0]) if height > 0 else 0
    
    # Find starting position 'S'
    start_col = -1
    for col in range(width):
        if grid[0][col] == 'S':
            start_col = col
            break
    
    # Simulate beams: (row, col) positions moving downward
    beams = [(1, start_col)]  # Start one row below S
    splits = 0
    
    # Track active beam positions to handle merging
    seen_states = set()
    
    while beams:
        new_beams = []
        
        for row, col in beams:
            if row >= height:
                continue
            
            state = (row, col)
            if state in seen_states:
                continue
            seen_states.add(state)
            
            if grid[row][col] == '^':
                # Beam hits splitter - count the split
                splits += 1
                # Create two new beams from adjacent positions
                if col > 0:
                    new_beams.append((row + 1, col - 1))
                if col < width - 1:
                    new_beams.append((row + 1, col + 1))
            else:
                # Continue downward
                new_beams.append((row + 1, col))
        
        beams = new_beams
    
    print("Beam splits =", splits)

if __name__ == "__main__":
    solve()
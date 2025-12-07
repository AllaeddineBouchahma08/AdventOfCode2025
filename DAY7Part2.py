def solve():
    with open("input.txt", "r") as f:
        lines = [line.rstrip('\n') for line in f]
    
    grid = lines
    height = len(grid)
    width = len(grid[0]) if height > 0 else 0
    
    start_col = -1
    for col in range(width):
        if grid[0][col] == 'S':
            start_col = col
            break
    

    memo = {}
    
    def count_paths(row, col):
        if row >= height:
            return 1
        
        if (row, col) in memo:
            return memo[(row, col)]
        
        result = 0
        
        if grid[row][col] == '^':
         
            if col > 0:
                result += count_paths(row + 1, col - 1)

            if col < width - 1:
                result += count_paths(row + 1, col + 1)
        else:
            result = count_paths(row + 1, col)
        
        memo[(row, col)] = result
        return result
    
    timelines = count_paths(1, start_col)
    
    print("Number of timelines =", timelines)

if __name__ == "__main__":
    solve()
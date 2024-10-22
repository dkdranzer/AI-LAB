
def calculate_cost(state):
    attacks = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                attacks += 1
    return attacks

def get_neighbors(state):
    neighbors = []
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            new_state = state[:]
            new_state[i], new_state[j] = new_state[j], new_state[i]
            neighbors.append(new_state)
    return neighbors

def print_board(state):
    n = len(state)
    board = [["." for _ in range(n)] for _ in range(n)]
    for col in range(n):
        row = state[col]
        board[row][col] = "Q"
    for row in board:
        print(" ".join(row))
    print()

def hill_climbing(initial_state):
    current_state = initial_state
    current_cost = calculate_cost(current_state)
    steps = []

    print("Initial State:")
    print_board(current_state)

    while current_cost > 0:  
        neighbors = get_neighbors(current_state)
        next_state = None
        next_cost = float('inf')

        for neighbor in neighbors:
            cost = calculate_cost(neighbor)
            if cost < next_cost:
                next_cost = cost
                next_state = neighbor

        if next_cost >= current_cost:
            break

        current_state = next_state
        current_cost = next_cost
        steps.append((current_state, current_cost))
        print("Next State:")
        print_board(current_state)

    return current_state, current_cost, steps

# Initial state: x0=3, x1=1, x2=2, x3=0 ,columns are fixed these are row numbers
initial_state = [3, 1, 2, 0]
final_state, final_cost, execution_steps = hill_climbing(initial_state)


print("Final State:", final_state)
print("Final Cost:", final_cost)

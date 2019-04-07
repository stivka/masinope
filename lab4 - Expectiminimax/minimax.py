X = 1
O = -1
EMPTY = 0

start_state = [0,0,0,
               0,0,0,
               0,0,0]

start_moves = [0,1,2,3,4,5,6,7,8]

ai_side = X

def minimax_ai(turn, avail_moves, state):
    # this is the top level of search
    # we search all possible moves
    # (PASS and ROLL in case of the Pig game)
    # and pick the one that returns the highest minimax estimate
    best_move = None
    best_value = -2
    for move in avail_moves:
        new_state = state.copy()
        new_state[move] = turn
        new_avail_moves = avail_moves.copy()
        new_avail_moves.remove(move)
        v = minimax(turn, new_state, new_avail_moves, 4)

        if v > best_value:
            best_value = v
            best_move = move


    return

def find_win_loss(state):
    for row in range(3):
        roff = row*3
        
    return

def minimax(turn, state, avail_moves, depth):
    # update remaining depth as we go deeper in the search tree
    depth = depth - 1

    # case 1a: somebody won, stop searching
    # return a high value if AI wins, low if it loses.
    win_loss = find_win_loss(state)
    if win_loss != 0:
        return win_loss

    # end of search tree
    if not avail_moves:
        return 0

    # case 1b: out of depth, stop searching
    # return game state eval (should be between win and loss)
    if depth < 1:
        return 0
    # case 2: AI's turn (and NOT a chance node):
    # return max value of possible moves (recursively)
    if turn == ai_side:
        best_value = -2
        for move in avail_moves:
            new_state = state.copy()
            new_state[move] = turn
            new_avail_moves = avail_moves.copy()
            new_avail_moves.remove(move)
            v = minimax(-turn, new_state, new_avail_moves, 4)

            if v > best_value:
                best_value = v
        
    # case 3: player's turn:
    # return min value (assume optimal action from player)

    return
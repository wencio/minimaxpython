def minimax(state, player):
    if game_over(state):
        return evaluate(state)
    
    if player == 'X':
        best_score = -math.inf
        for move in possible_moves(state):
            new_state = make_move(state, move, player)
            score = minimax(new_state, 'O')
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for move in possible_moves(state):
            new_state = make_move(state, move, player)
            score = minimax(new_state, 'X')
            best_score = min(best_score, score)
        return best_score

def get_best_move(state):
    best_score = -math.inf
    best_move = None
    for move in possible_moves(state):
        new_state = make_move(state, move, 'X')
        score = minimax(new_state, 'O')
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

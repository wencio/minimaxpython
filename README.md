# minimaxpython
Here's an example of Tic Tac Toe AI implemented using Minimax algorithm in Python:
In this code, the minimax function recursively evaluates each possible move and returns the score for each terminal node. The get_best_move function selects the move with the highest score for the AI to play.

To make the AI smarter, we can add heuristics to the evaluation function. For example, we can assign higher scores to states where the AI has more winning combinations available or penalize states where the opponent has more winning combinations available. We can also use Alpha-Beta Pruning to reduce 
the number of nodes explored and make the algorithm more efficient.

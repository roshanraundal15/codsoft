from flask import Flask, render_template, request, jsonify
import math
import os

app = Flask(__name__, template_folder='templates')

# Game logic

def check_winner(board):
    win_combos = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for combo in win_combos:
        a, b, c = combo
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]
    if all(x is not None for x in board):
        return 'Draw'
    return None

def minimax(board, is_maximizing):
    winner = check_winner(board)
    if winner == 'O':
        return 1
    elif winner == 'X':
        return -1
    elif winner == 'Draw':
        return 0
    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] is None:
                board[i] = 'O'
                score = minimax(board, False)
                board[i] = None
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] is None:
                board[i] = 'X'
                score = minimax(board, True)
                board[i] = None
                best_score = min(score, best_score)
        return best_score

def ai_move(board):
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] is None:
            board[i] = 'O'
            score = minimax(board, False)
            board[i] = None
            if score > best_score:
                best_score = score
                move = i
    return move

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/move', methods=['POST'])
def move():
    data = request.get_json()
    board = data.get('board', [None]*9)
    # Human move is already applied on the board
    winner = check_winner(board)
    if winner:
        return jsonify({'board': board, 'winner': winner})
    # AI move
    move = ai_move(board)
    if move is not None:
        board[move] = 'O'
    winner = check_winner(board)
    return jsonify({'board': board, 'winner': winner})

if __name__ == '__main__':
    app.run(debug=True) 
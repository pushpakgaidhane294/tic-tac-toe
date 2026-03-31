from flask import Flask, render_template, request, jsonify
import os

# ✅ FIX: absolute template path (important for Render)
base_dir = os.path.abspath(os.path.dirname(__file__))
template_dir = os.path.join(base_dir, 'templates')

app = Flask(__name__, template_folder=template_dir)

WINS = [
    [0,1,2],[3,4,5],[6,7,8],
    [0,3,6],[1,4,7],[2,5,8],
    [0,4,8],[2,4,6]
]

def check_winner(board, marker):
    for line in WINS:
        if all(board[i] == marker for i in line):
            return line
    return None

def is_draw(board):
    return all(cell is not None for cell in board)

def minimax(board, is_max):
    if check_winner(board, 'X'):
        return 10
    if check_winner(board, 'O'):
        return -10
    if is_draw(board):
        return 0

    best = -float('inf') if is_max else float('inf')
    for i in range(9):
        if board[i] is None:
            board[i] = 'X' if is_max else 'O'
            score = minimax(board, not is_max)
            board[i] = None
            if is_max:
                best = max(best, score)
            else:
                best = min(best, score)
    return best

def best_move(board):
    best = -float('inf')
    move = -1
    for i in range(9):
        if board[i] is None:
            board[i] = 'X'
            score = minimax(board, False)
            board[i] = None
            if score > best:
                best = score
                move = i
    return move

# ✅ FIX: allow HEAD request (Render health check)
@app.route('/', methods=['GET', 'HEAD'])
def index():
    return render_template('index.html')

# ✅ FIX: safe JSON handling
@app.route('/api/ai-move', methods=['POST'])
def ai_move():
    data = request.get_json()

    if not data or 'board' not in data:
        return jsonify({"error": "Invalid request"}), 400

    board = data.get('board')

    move = best_move(board)
    board[move] = 'X'

    win_line = check_winner(board, 'X')
    draw = is_draw(board)

    return jsonify({
        'move': move,
        'win_line': win_line,
        'draw': draw,
        'winner': 'X' if win_line else None
    })

# ✅ FIX: safe JSON handling
@app.route('/api/check', methods=['POST'])
def check():
    data = request.get_json()

    if not data or 'board' not in data or 'marker' not in data:
        return jsonify({"error": "Invalid request"}), 400

    board = data.get('board')
    marker = data.get('marker')

    win_line = check_winner(board, marker)
    draw = is_draw(board)

    return jsonify({
        'win_line': win_line,
        'draw': draw,
        'winner': marker if win_line else None
    })

# ✅ production safe
if __name__ == '__main__':
    app.run()

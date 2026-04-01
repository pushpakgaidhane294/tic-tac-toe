from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

board = [""] * 9
current_player = "X"
mode = "ai"

scores = {"X": 0, "O": 0, "draw": 0}

# ---------- WIN CHECK ----------
def check_winner(b):
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    for i,j,k in wins:
        if b[i] == b[j] == b[k] and b[i] != "":
            return b[i]
    if "" not in b:
        return "Draw"
    return None

# ---------- MINIMAX ----------
def minimax(b, is_max):
    winner = check_winner(b)
    if winner == "X":
        return 10
    elif winner == "O":
        return -10
    elif winner == "Draw":
        return 0

    if is_max:
        best = -1000
        for i in range(9):
            if b[i] == "":
                b[i] = "X"
                score = minimax(b, False)
                b[i] = ""
                best = max(best, score)
        return best
    else:
        best = 1000
        for i in range(9):
            if b[i] == "":
                b[i] = "O"
                score = minimax(b, True)
                b[i] = ""
                best = min(best, score)
        return best

def best_move():
    best_score = -1000
    move = None
    for i in range(9):
        if board[i] == "":
            board[i] = "X"
            score = minimax(board, False)
            board[i] = ""
            if score > best_score:
                best_score = score
                move = i
    return move

# ---------- ROUTES ----------
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/start", methods=["POST"])
def start():
    global board, current_player, mode

    data = request.json
    mode = data.get("mode", "ai")

    board = [""] * 9

    if mode == "ai":
        current_player = "O"
        ai = best_move()
        if ai is not None:
            board[ai] = "O"
            current_player = "X"
    else:
        current_player = "X"

    return jsonify({"board": board, "scores": scores})

@app.route("/move", methods=["POST"])
def move():
    global current_player, board, scores

    data = request.json
    pos = data.get("move")

    if board[pos] == "":
        board[pos] = current_player

        winner = check_winner(board)

        if not winner:
            if mode == "ai":
                current_player = "O"
                ai = best_move()
                if ai is not None:
                    board[ai] = "O"
                current_player = "X"
                winner = check_winner(board)
            else:
                current_player = "O" if current_player == "X" else "X"

        if winner:
            if winner == "Draw":
                scores["draw"] += 1
            else:
                scores[winner] += 1

        return jsonify({
            "board": board,
            "winner": winner,
            "current": current_player,
            "scores": scores
        })

    return jsonify({"error": "Invalid move"})

# ---------- RUN ----------
if __name__ == "__main__":
    app.run(debug=True)

# 🎮 Reinforcement Learning-Based Tic Tac Toe Game with AI Opponent

An interactive web-based **Tic Tac Toe** game powered by **Reinforcement Learning (Q-Learning)**. The AI agent learns optimal strategies through reward-based learning, allowing users to play against a computer or another player in a modern and responsive web interface.

---

## 📌 Project Overview

This project demonstrates the application of **Reinforcement Learning (RL)** in game development. A Q-Learning agent is trained to make intelligent decisions by interacting with the game environment and maximizing rewards over time.

The application is developed using **Python (Flask)** for the backend and **HTML, CSS, and JavaScript** for the frontend.

---

## 🎯 Objectives

- Develop a Reinforcement Learning-based AI agent.
- Implement the Q-Learning algorithm for optimal gameplay.
- Create an interactive and responsive web interface.
- Allow users to play against an AI opponent or another player.
- Deploy the application online for public access.

---

## 🚀 Features

- 🤖 AI Opponent using Reinforcement Learning (Q-Learning)
- 👥 Multiplayer Mode (Player vs Player)
- 🎮 Interactive Tic Tac Toe Gameplay
- 🏆 Winner Detection
- 📊 Live Scoreboard
- 🔄 Restart Game Option
- 💻 Responsive User Interface
- ☁️ Deployable on Render

---

## 🛠️ Technologies Used

### Backend
- Python
- Flask

### Frontend
- HTML5
- CSS3
- JavaScript

### Deployment
- Render

### Version Control
- Git
- GitHub

---

## 🧠 Reinforcement Learning Concept

The AI agent learns by interacting with the game environment.

### Agent
AI Player

### Environment
Tic Tac Toe Board

### State
Current board configuration

### Actions
- Place X
- Place O

### Rewards

| Result | Reward |
|---------|---------|
| Win | +1 |
| Draw | 0 |
| Lose | -1 |

The Q-Learning algorithm updates its knowledge after every move and gradually learns optimal gameplay strategies.

---

## 📂 Project Structure

```
tic-tac-toe/
│
├── app.py
├── requirements.txt
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/tic-tac-toe.git
```

Move into project

```bash
cd tic-tac-toe
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run application

```bash
python app.py
```

Open browser

```
http://127.0.0.1:5000
```

---

## 🌐 Deployment

This project is deployed using **Render**.

Build Command

```bash
pip install -r requirements.txt
```

Start Command

```bash
gunicorn app:app
```

---

## 📸 Screenshots

Add screenshots of:

- Home Page
- Game Board
- AI Gameplay
- Winner Popup
- Scoreboard

Example:

```
screenshots/
├── home.png
├── gameplay.png
├── winner.png
```

---

## 📈 Future Enhancements

- Deep Q-Learning (DQN)
- Multiple AI Difficulty Levels
- Game Statistics Dashboard
- Sound Effects
- Dark/Light Theme
- Online Multiplayer
- Game History
- Player Rankings

---

## 📚 Learning Outcomes

Through this project, I learned:

- Reinforcement Learning fundamentals
- Q-Learning algorithm
- Flask Web Development
- Frontend Integration
- Game Logic Design
- Cloud Deployment using Render
- Git & GitHub Workflow

---

## 👨‍💻 Author
**Pushpak Gaidhane**

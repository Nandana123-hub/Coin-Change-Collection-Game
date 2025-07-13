# 🎮 Optimum Coin Change Game (Streamlit)

An interactive game built with Python and Streamlit that challenges users to use the **least number of coins** to reach a target value. Each level is dynamically generated with different coin denominations and target amounts, offering a fresh challenge every time!

---

## 🚀 Features

- 🎯 **Random Levels**: New target and coin set every round
- 💡 **Hint System**: Suggests how many coins might be optimal
- 🧠 **Dynamic Algorithm**: Uses dynamic programming to evaluate the optimal solution
- 🏆 **Scoring & Rewards**: Earn points, see attempts, and progress across levels
- 🎨 **Attractive UI**: Clean, colorful, and mobile-friendly interface
- 🎉 **Rain Effects**: Celebratory animations when you win a level
- 🔁 **Replayable**: Challenge yourself again and again with new levels

---

## 🧮 How It Works

1. You're given a **target amount** and a set of **coin denominations**.
2. Your task is to enter a combination of coins that exactly matches the target.
3. The game checks whether:
   - Your total is correct ✅
   - You used only allowed coins 🪙
   - You used the optimal number of coins 💡
4. You earn a score based on performance and progress to the next level.

---

## 🛠️ Tech Stack

- **Python 3**
- **Streamlit**
- **Dynamic Programming** (for calculating optimal solutions)
- `streamlit-extras` (for UI effects)

---

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/coin-change-game.git
   cd coin-change-game

Install dependencies:
pip install -r requirements.txt
Or manually:
pip install streamlit streamlit-extras
Run the app:
py -m streamlit run app.py

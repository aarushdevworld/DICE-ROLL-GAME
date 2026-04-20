# 🎲 FAAAHH! Dice Roll Game

A simple and fun **Python-based Dice Rolling Game** that supports both **Single Player** and **Multiplayer** modes. Built using modular Python files and a menu-driven system.

---

## 🚀 Features

- 🎯 Single Player Mode (roll dice endlessly)
- 👥 Multiplayer Mode (2 players compete)
- 🔁 Replay option after each round
- 📋 Menu-driven interface
- 🧩 Modular code structure (separate files for logic)

---

## 📁 Project Structure

```

FAAAHH-Dice-Game/
│
├── main.py        # Entry point of the program
├── menu.py        # Displays game menu
├── single.py      # Single player mode
├── multi.py       # Multiplayer mode
├── roll.py        # Dice rolling logic

````

---

## ⚙️ How It Works

- The program starts from **main.py** which calls the menu system
- The menu allows users to choose between:
  - Single Player 
  - Multiplayer 
- Dice rolling is handled by a reusable function in `roll.py`  

---

## 🎮 Game Modes

### 🧍 Single Player
- Rolls a dice (1–6)
- Displays result
- Option to play again  

---

### 👥 Multiplayer
- Two players enter their names
- Each rolls the dice
- Higher number wins
- Tie condition handled  

---

## ▶️ How to Run

1. Make sure Python is installed
2. Download or clone this repository
3. Run the main file:

```bash
python main.py
````

---

## 🛠️ Requirements

* Python 3.x
* No external libraries required (uses built-in `random` module)

---

## 💡 Future Improvements
* 🔊 Sound effects for dice roll
* 🏆 Score tracking system
* 🤖 Add AI opponent

---

## 👨‍💻 Author

* Aarush (Student Project)

---

## 📜 License

This project is open-source and free to use for learning purposes.

---

## ❤️ Acknowledgement

Built as a beginner-friendly Python project to understand:

* Functions
* Modules
* Loops
* User Input Handling

---

🎉 *Enjoy rolling the dice!*



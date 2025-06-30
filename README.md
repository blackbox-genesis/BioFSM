# BioFSM - Synthetic Biology Logic Game

**BioFSM** is an experimental game that blends synthetic biology with logic circuits.\
Built using Python and Tellurium, it turns genetic circuit behavior into interactive puzzles. Each level simulates a real biological system, powered by a custom finite state machine (FSM) engine and rendered through a basic Streamlit UI.

This prototype includes:

- A tutorial level on gene expression logic
- A chaotic survival level based on feedback loops and random mutations

It's not meant to be a perfect app - it’s a proof-of-concept for how biological design can be made playable, and how circuits can be tested through simulated decision-making.

> Think of it as a synthetic biology sandbox… with consequences.

---

## ⚙️ Tech Stack

BioFSM is built entirely in Python and leverages powerful tools from both biological modeling and user interface design.

- **Language**: Python 3.11
- **Simulation Engine**: [Tellurium](http://tellurium.analogmachine.org/) (includes Antimony + RoadRunner for SBML-based gene circuit modeling)
- **UI**: Streamlit (interactive interface for running levels and viewing outputs)
- **Visualization**: Matplotlib (time-course plots of gene/protein expression)
- **Other Libraries**: `io` for file stream handling, plus built-in Python modules

---

##  Levels

###  Level 1 - Basic Gene Expression (File: `levels.py`)

Level 1 is kind of like a tutorial - it looks simple, but it’s actually not.

It runs directly on an actual **Tellurium gene circuit script**, and gives the player **two input choices: IPTG and aTc**. One of them activates GFP expression, the other doesn’t. If the player selects the correct one and runs the simulation, they’ll see **real-time gene expression results** on a graph.

This was the first level I built, and honestly, I wasn’t even sure it would work. But surprisingly, it did - and the fact that you could actually interact with real genetic logic in a game-like setup was fascinating. Since I’m not a software developer, I used **AI tools** and open-source references to piece together a basic Streamlit interface.

> It’s not flashy, but it works - and that felt like a small win in itself.

---

###  Level 2 - Mutation Mayhem & Feedback Chaos (File: `level2_feedback.py`)

**Building this level was a nerve-wracking experience.**\
Level 2 is completely chaotic - probably the most intense part of the prototype so far.

Here, the player gets **three inputs** to pick from: IPTG, AHL, and aTc.

- `IPTG` inhibits **LacI**
- `AHL` activates **TetR**, but only if **LacI is repressed**
- `aTc` acts as the **reset**, degrading both **TetR** and **LacI**

The goal is to keep the output (GFP) **ON for at least 4 turns**, and survive **10+ total turns**.\
But there’s a twist: the system randomly **mutates itself**, flipping the logic of **TetR** and **LacI** at unpredictable moments.

If the output turns ON **while feedback is active**, it’s **game over**.

Players have to carefully sequence their inputs, manage conditional activation, and survive instability under pressure.

> “It was pure madness building this one - I wasn’t sure if the feedback loops would behave at all. But somehow, it worked - and turned into my favorite level.”

---

##  File Structure & How It Works

BioFSM is made up of simulation levels, a custom finite-state-machine engine, and a basic Streamlit interface. The system uses Python and Tellurium to simulate actual gene circuit dynamics, with game-like logic layered on top.

Here’s an overview of the core files:

```
BioFSM/
├── levels.py              # Contains Level 1 simulation logic (gene expression puzzle)
├── level2_feedback.py     # Contains Level 2 logic (mutation + feedback chaos)
├── fsm_engine.py          # Core FSM logic: state handling, mutation flips, input processing
├── utils.py               # Plotting functions, protein tracking, timer tools
├── toggle_model.py        # Reusable circuit logic used by FSM for toggle behaviors
├── main_app.py            # Streamlit interface for running the game
├── requirements.txt       # All required packages (Tellurium, Streamlit, matplotlib, etc.)
└── README.md              # You are here
```

⚠️ **Note**: The FSM engine and Streamlit UI were built with the help of **AI tools** (like ChatGPT) and various **open-source references**. The goal wasn’t to make a polished app — it was to create a working, interactive prototype that lets players experiment with biological logic in a game-like format.

---

##  How to Run

### 1. Clone the repository:

```bash
git clone https://github.com/blackbox-genesis/BioFSM.git
cd BioFSM
```

### 2. Install required libraries:

```bash
pip install -r requirements.txt
```

### 3. Launch the game:

```bash
streamlit run main_app.py
```

If you get any errors, make sure Tellurium is properly installed (some systems need extra dependencies).

---

##  License

This project is released under the **MIT License**.\
Feel free to fork, build on, or use parts of this project with proper attribution.

---

##  About the Author

[Aditya Raj – LinkedIn](https://www.linkedin.com/in/aditya-synbio/)\
Undergraduate student & aspiring synthetic biologist.\
I build strange gene circuits and sometimes turn them into games.


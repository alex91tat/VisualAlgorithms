# 🧠 Pathfinding Algorithm Visualizer

---

### 📘 Description

**Pathfinding Algorithm Visualizer** is a Python desktop application that lets users explore and compare how different **pathfinding algorithms** find routes in a grid.  
It’s built with **Pygame** and designed to visually demonstrate the step-by-step logic behind algorithms such as **A\***, **Dijkstra**, **BFS**, **DFS**, and more.

This project demonstrates concepts of **graph traversal**, **heuristics**, **algorithm efficiency**, and **real-time visualization** in computer science.

---

### ⚙️ Features

- 🎨 **Interactive visualization** — watch algorithms explore and find paths in real time  
- 🧭 **Multiple algorithms** — A*, Dijkstra, BFS, DFS, UCS, IDS, DLS, and IDA*  
- 🧱 **Custom grid creation** — draw start, end, and barrier nodes with your mouse  
- 🔄 **Reset and clear options** — easily rebuild and test different scenarios  
- 🧮 **Heuristic functions** — supports Manhattan and Euclidean distance for A* and IDA*  
- 🧪 **Modular code structure** — separate logic for grid, spot, and algorithms for easy maintenance

---

### 🧩 Project Structure

```text
project/
├── main.py                    # Main application with GUI and event loop
├── searching_algorithms.py    # Core logic for all implemented search algorithms
├── grid.py                    # Grid management, drawing, and interaction
├── spot.py                    # Spot (node) class definition
├── utils.py                   # Constants, colors, and configuration
└── README.md                  # Project documentation
```

---

### 🧠 How It Works

1. 🖥️ **Launch the program** — a grid appears on the screen.  
2. 🎯 **Set up the environment:**
   - Left-click to place the **Start node** (cyan)
   - Left-click again to place the **End node** (pink)
   - Continue left-clicking to add **Barriers** (dark blue)  
3. ⚙️ **Choose an algorithm** — select from **A\***, **BFS**, **DFS**, **Dijkstra**, **UCS**, **IDS**, or **IDA\***.  
4. 🧩 **Watch the algorithm run:**
   - **Open nodes** → currently being explored  
   - **Closed nodes** → already visited  
   - **Final path** → displayed in **purple** once found  
5. ✅ **Completion:** when the algorithm finishes, the optimal path is shown.  
6. 🔄 **Try again:** click **CLEAR GRID** to reset and run a new simulation.

---

### 🚀 Technologies Used

- 🐍 **Python 3.12+**
- 🎮 **Pygame**
- 🧱 **Object-Oriented Design**

---



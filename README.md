# 📐 Cable Layout Optimizer

An interactive web application built with **Flask** and **Plotly.js** to calculate the optimal cable layout using **Kruskal's Minimum Spanning Tree (MST) algorithm**. This tool helps engineers and planners determine the most cost-effective way to lay cables between multiple locations.

---

## 🚀 Features

- 🔧 Add and remove connection points on a live grid
- 📈 Visualize cable layout and MST in real-time
- 📏 Calculate total cable length using Euclidean distance
- 💰 Estimate cost based on user-defined rate per unit length
- 📊 Dynamic graph updates with interactive Plotly plotting

---

## 🧠 How It Works

1. User clicks to add locations on a 2D grid.
2. App computes all possible edges and their weights (distances).
3. Uses **Kruskal's algorithm** to generate the optimal layout (MST).
4. Displays total cable length and total cost based on input rate.

---

## 🔍 Technologies Used

- 🐍 Python 3.x
- 🌐 Flask (for backend)
- 📊 Plotly.js (for interactive plotting)
- 🧮 NumPy (for distance calculations)
- 🖥️ HTML + CSS + JS (frontend)

---

## 📂 Project Structure

├── app.py # Flask backend for handling calculations
├── templates/
│ └── index.html # Frontend UI with Plotly visualization
├── static/ # (Optional) CSS/JS if split from HTML
└── README.md # You're here!


---

## ▶️ Running the App

1. **Clone the repository**
   ```bash
   git clone https://github.com/vishesh230104/Optimised_cable_layout_system.git
   cd Optimised_cable_layout_system


2. **Install dependencies**
   ```bash
   pip install flask numpy


3. **Run the server**
   ```bash
   python app.py


4. Open http://127.0.0.1:5000 in your browser.


🧪 Example Use Case
Scenario: You are laying network cables between multiple buildings.

Goal: Minimize the total length and cost.

Result: The app provides an MST layout and the total cost based on your unit price.


🙌 Acknowledgments
Inspired by graph theory and real-world network planning problems.

Uses Kruskal's algorithm for MST computation.


👨‍💻 Author
Vishesh – @vipvishesh123@gmail.com

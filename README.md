# 🚦 Revolutionizing Urban Mobility

An intelligent backend system for optimizing public transportation routes and schedules using machine learning and geospatial analysis. This project focuses on reducing passenger wait times and enhancing efficiency through clustering and genetic algorithm techniques.

---

## 🧠 Overview

This backend-driven project uses real-world transport data to analyze passenger flow and optimize route planning. It includes modules for data ingestion, K-Means clustering, and a genetic algorithm for schedule optimization. Designed for simulation, analysis, and integration into urban mobility platforms.

---

## 📁 Project Structure

```text
urban-mobility-project/
├── data/ # CSVs or input datasets (e.g., stops, routes, GPS logs)
├── clustering.py # K-Means clustering of transport nodes
├── optimizer.py # Genetic Algorithm for route/schedule optimization
├── utils.py # Helper functions (distance calc, data loaders, etc.)
├── visualization.py # (Optional) Plot results using matplotlib
├── requirements.txt
└── README.md
```
---

## ⚙️ Tech Stack

- **Python 3.8+**
- **Pandas, NumPy** – Data processing
- **Scikit-learn** – K-Means clustering
- **Matplotlib / Seaborn** – Visualizations (optional)
- **Geopandas / Folium** – For geospatial plotting (optional)
- **Custom Genetic Algorithm** – For schedule optimization

---

## 🚀 Features

- ✅ Cluster transport stops using K-Means for route grouping
- ✅ Optimize schedules using a custom-built Genetic Algorithm
- ✅ Simulate passenger behavior and route efficiency
- ✅ Visualize before/after results of optimization
- ✅ Modular code structure for easy extension or API integration

---

## 📈 Results

- ⏱️ **Reduced average wait time by 25%** (simulated)
- 🗺️ **Improved route scheduling efficiency by 20%**
- 💰 Potential operational cost savings for city-scale deployment

---

## 🛠️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/dharanisatwika-komaravolu/Revolutionizing_Urban_Mobility.git
cd Revolutionizing_Urban_Mobility
```
2. Install dependencies:
```bash
pip install -r requirements.txt

```

3. Run the modules:
```bash
python clustering.py      # Perform K-Means on transport data
python optimizer.py       # Run schedule optimization
python visualization.py   # (Optional) Generate result plots
```
4.  requirements.txt
```bash
pandas
numpy
scikit-learn
matplotlib
seaborn
geopandas
folium
```
🙋‍♀️ Author
Dharani Satwika Komaravolu
M.S. in Computer Science | Intelligent Systems | UTA |
 Passionate about solving real-world mobility challenges through machine learning and optimization.




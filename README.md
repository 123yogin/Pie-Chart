
# 📊 Visualization of Product Stock with Pie Chart

## 📌 Summary

This project is a Python-based inventory visualization tool that processes stock data from CSV files and generates interactive pie charts. It offers quick, insightful, and professional views of product stock distribution to assist in inventory management and business decision-making.

---

## 🚀 Project Overview

### 🎯 Objective

To build a robust, modular Python application that converts raw inventory data into interactive pie charts, enabling stakeholders to make quick, informed decisions.

### 🧩 Problem Statement

Traditional inventory systems often display raw tabular data that can be hard to interpret. This project addresses that by offering:
- Visual representation of inventory data
- Quick insights into stock levels
- Percentage-based analysis
- Professional-quality reporting outputs

---

## 🛠️ Technical Architecture

### 📐 System Flow

`[CSV Input] → [Validation] → [Processing Engine] → [Visualization] → [Export]`

### 🔧 Core Components

#### Data Layer
- **Input Format**: CSV with `Product` and `Stock` columns
- **Validation**: Auto-checks for correct formatting and data integrity

#### Visualization Layer
- **Library**: Matplotlib for professional visual outputs
- **Features**: Custom styling, interactive legends, labels, and percentage displays

---

## 🧱 Implementation

### 🏗️ Code Architecture

Uses a class-based design with memory optimization (`__slots__`) and modular functions.

#### `StockVisualizer` Class
- `load_data()`: Loads and validates the CSV
- `create_visualization()`: Generates the pie chart
- `print_statistics()`: Displays analytics
- `save_chart()`: Exports chart as an image

---

## 📦 Project Structure

```
.
├── pie_chart.py             # Main application file
├── product_stock.csv        # Sample dataset (10 products)
├── output.png               # Example chart output
└── README.md                # Project documentation
```

---

## 📈 Results & Deliverables

### 📂 Outputs
- **Interactive Pie Chart**: Easily understandable visuals
- **Analytics Report**: Console-based statistical summary
- **Exportable Charts**: Presentation-ready images
- **Sample Dataset**: Included for demo purposes

### 🔍 Sample Output (From `product_stock.csv`)
```
Total Stock: 525 units
Average Stock: 52.5 per product
Highest Stock: Mouse (120 units) - 22.9%
Lowest Stock: Camera (15 units) - 2.9%
```

### 📊 Visual Insights
- Mouse & Keyboard = 38% of stock
- Camera & Tablet need restocking
- Healthy levels for Smartphone & Headphones

---

## 📚 Requirements

- Python 3.x
- matplotlib
- pandas

Install dependencies using:

```bash
pip install matplotlib pandas
```
---

## 📜 License

This project is licensed under the MIT License.

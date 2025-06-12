# Linear Regression from Scratch 🧠📈

This project demonstrates how to build a **Linear Regression model** in Python using fundamental concepts — no libraries like scikit-learn are used for the regression itself. It's a clean, modular, and educational implementation based on solving normal equations with NumPy.

---

## 📂 Project Structure

- `linear_regression.py` — Main script with user interaction and output
- `parameters.py` — Calculates necessary summations for the regression equations
- `formula.py` — Solves the linear regression normal equations using NumPy

---

## 🧮 Math Behind It

We solve the following two normal equations to find constants `a` and `b`:

Σy = n·a + b·Σx

Σxy = a·Σx + b·Σx²

From this, we derive:
y = a + bx


---

## ✅ Features

- Object-Oriented Design (`LinearRegression` class)
- Modular code with clean separation of logic
- Uses `numpy.linalg.solve` to solve 2x2 equations
- Accepts user input and gives predicted output
- Proper output formatting with rounding
- Great for beginners learning machine learning math

---

## 📦 Dependencies

- Python 3.x
- NumPy

Install with:
```bash
pip install numpy
```
--- 

▶️ How to Run
python linear_regression.py
Then follow the prompts to input x-values and get corresponding y predictions.
 ---
 
🚀 Example Output

 for this linear regression we have: 
(2, 8)
(3, 12)
(4, 15)
(5, 20)
sum of x: 14
sum of y: 55
sum of xy: 212
sum of xsqr: 54
a: 0.1
b: 3.9
enter the value of x : 2
for this value of x, as per linear regression the value of y is 7.9

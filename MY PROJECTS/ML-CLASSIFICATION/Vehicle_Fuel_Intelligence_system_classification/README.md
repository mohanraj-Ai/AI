# 🚗 Vehicle Fuel Efficiency Classification System

<p align="center">

### 🤖 AI-Powered Automotive Fuel Efficiency Classification

**Machine Learning • Random Forest • Flask • Automotive Analytics**

</p>

<p align="center">

Predict vehicle fuel-efficiency classes using key automotive parameters and a trained Machine Learning model.

</p>

---

## 🌟 Project Showcase

<p align="center">
  <img src="assets/capture.png" alt="Vehicle Fuel Intelligence System" width="900">
</p>

### 🖥️ Live Prediction Interface

The application provides an interactive web interface where users can enter vehicle specifications and receive a real-time Machine Learning prediction.

---

## 🎯 What Does This Project Do?

The **Vehicle Fuel Intelligence System** is an end-to-end Machine Learning application designed for automotive data analysis.

It uses vehicle parameters such as:

* 🚘 Vehicle Mass
* ⚙️ Engine Capacity
* 🔋 Engine Power
* ⛽ Fuel Type

to classify the vehicle's expected fuel-efficiency category as:

**High • Medium • Low**

The trained Machine Learning model is integrated with a **Flask web application**, allowing users to interact with the model through a modern web interface.

---

## 🧠 AI / Machine Learning Workflow

```text
┌─────────────────────────┐
│   Automotive Dataset    │
└────────────┬────────────┘
             ↓
┌─────────────────────────┐
│     Data Cleaning       │
└────────────┬────────────┘
             ↓
┌─────────────────────────┐
│ Feature Engineering     │
└────────────┬────────────┘
             ↓
┌─────────────────────────┐
│   Feature Selection     │
└────────────┬────────────┘
             ↓
┌─────────────────────────┐
│ Random Forest Classifier│
└────────────┬────────────┘
             ↓
┌─────────────────────────┐
│    Model Evaluation     │
└────────────┬────────────┘
             ↓
┌─────────────────────────┐
│      Flask API/App      │
└────────────┬────────────┘
             ↓
┌─────────────────────────┐
│   Fuel Efficiency       │
│   High / Medium / Low   │
└─────────────────────────┘
```

---

## 📊 Model Performance

| Metric          |                   Result |
| --------------- | -----------------------: |
| Algorithm       | Random Forest Classifier |
| Number of Trees |                      300 |
| Input Features  |                        4 |
| Output Classes  |                        3 |
| Test Accuracy   |                  **94%** |
| Random State    |                       42 |

> The reported accuracy is based on the test evaluation performed during model development.

---

## 🚘 Input Features

| Feature            | Description               |
| ------------------ | ------------------------- |
| 🚗 Vehicle Mass    | Vehicle mass in kilograms |
| ⚙️ Engine Capacity | Engine displacement in CC |
| 🔋 Engine Power    | Engine power in kW        |
| ⛽ Fuel Type        | Diesel / Petrol           |

---

## 🎯 Prediction Classes

The model classifies vehicles into three categories:

```text
🟢 HIGH
🟡 MEDIUM
🔴 LOW
```

---

## 💻 Application Preview

### Vehicle Fuel Intelligence Dashboard

<p align="center">
  <img src="assets/capture.png" alt="Flask application prediction result" width="900">
</p>

The interface allows the user to enter vehicle specifications and obtain an AI-powered prediction without interacting directly with the Python model.

---

## 🛠️ Technology Stack

### Programming

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge\&logo=python)

### Machine Learning

![Scikit-learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange?style=for-the-badge\&logo=scikit-learn)

![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-150458?style=for-the-badge\&logo=pandas)

![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-013243?style=for-the-badge\&logo=numpy)

### Web Application

![Flask](https://img.shields.io/badge/Flask-Web%20Application-black?style=for-the-badge\&logo=flask)

![HTML5](https://img.shields.io/badge/HTML5-Interface-E34F26?style=for-the-badge\&logo=html5)

![CSS3](https://img.shields.io/badge/CSS3-Styling-1572B6?style=for-the-badge\&logo=css3)

### Development

![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge\&logo=jupyter)

![Git](https://img.shields.io/badge/Git-Version%20Control-F05032?style=for-the-badge\&logo=git)

![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge\&logo=github)

---

## 📂 Project Architecture

```text
VEHICLE-FUEL-INTELLIGENCE-SYSTEM/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── assets/
│   └── capture.png
│
├── models/
│   ├── rf_model.sav
│   ├── target_encoder.sav
│   └── model_columns.sav
│
├── src/
│   ├── __init__.py
│   └── prediction.py
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── notebooks/
│   ├── 1.CLASSIFY OUTPUT VARIABLE.ipynb
│   ├── 2.MODEL SELECTION.ipynb
│   └── 3.BEST MODEL.ipynb
│
├── data/
│
└── docs/
    └── Automotive Efficiency Intelligence.pdf
```

---

## 🔄 Prediction Pipeline

```text
User
 │
 │ Vehicle Parameters
 ↓
Flask Web Interface
 │
 ↓
Input Validation
 │
 ↓
Feature Preparation
 │
 ↓
Random Forest Model
 │
 ↓
Class Prediction
 │
 ↓
High / Medium / Low
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/mohanraj-Ai/vehicle-fuel-intelligence-system.git
```

### 2. Enter the project directory

```bash
cd vehicle-fuel-intelligence-system
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the Flask application:

```bash
python app.py
```

Open your browser:

```text
http://127.0.0.1:5000
```

---

## 🧪 Example Input

```text
Vehicle Mass:       1500 kg
Engine Capacity:    2000 cc
Engine Power:       100 kW
Fuel Type:          Diesel
```

The application processes the input through the trained Random Forest model and returns the predicted fuel-efficiency class.

---

## 📓 Machine Learning Development

The project contains three development notebooks.

### 01 — Classify Output Variable

Preparation and classification of the target variable.

### 02 — Model Selection

Evaluation and comparison of Machine Learning approaches.

### 03 — Best Model

Final Random Forest training, evaluation, and model serialization.

---

## 🔐 Dataset & Model Files

Large datasets and serialized model artifacts are intentionally excluded from the public GitHub repository.

Excluded:

```text
*.csv
*.sav
*.pkl
*.joblib
```

This keeps the repository lightweight and avoids committing large data and model artifacts.

---

## 🚀 Future Improvements

* 🌐 Cloud deployment
* 📡 REST API
* 📈 Interactive analytics dashboard
* 🎯 Prediction confidence/probability
* 🔍 SHAP-based model explainability
* 🐳 Docker deployment
* 🧪 Automated testing
* 📊 Additional automotive features
* 🔄 Model monitoring
* 🗄️ Database integration

---

## 👨‍💻 Author

### Mohanraj P

**Generative AI Engineer | AI/ML Engineer | LLM & RAG Developer**

🔗 GitHub:
https://github.com/mohanraj-Ai

🔗 LinkedIn:
https://linkedin.com/in/mohan-raj-p-2bb994217

---

## ⭐ If You Find This Project Interesting

Feel free to explore the repository and the Machine Learning workflow behind the application.

<p align="center">

**Built with Python • Machine Learning • Flask • Automotive AI**

</p>

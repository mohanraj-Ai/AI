# ⛽ Fuel Efficiency Prediction

A Machine Learning project that predicts vehicle fuel efficiency (km/L) using vehicle specifications such as engine capacity, engine power, vehicle mass, and fuel type. The model is trained using Random Forest Regression with feature engineering and hyperparameter tuning to achieve high prediction accuracy.

---

## 🚀 Project Overview

Fuel efficiency is one of the most important performance indicators in the automotive industry. This project leverages Machine Learning to predict a vehicle's fuel efficiency based on its technical specifications. The solution helps analyze vehicle performance and supports data-driven decision-making.

---

## ✨ Features

- 📊 Exploratory Data Analysis (EDA)
- 🧹 Data Cleaning & Preprocessing
- 🔧 Feature Engineering
- 🔄 Categorical Encoding
- 🌲 Random Forest Regression
- 🎯 Hyperparameter Tuning
- 📈 Model Evaluation
- 💾 Model Serialization for Deployment

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Joblib
- Jupyter Notebook

---

## 📂 Dataset

The dataset contains various vehicle specifications, including:

- Vehicle Mass (kg)
- Engine Capacity (cc)
- Engine Power (kW)
- Fuel Type (Petrol/Diesel)
- Fuel Efficiency Class

### 🎯 Target Variable

- Fuel Efficiency (km/L)

---

## 🏗️ Machine Learning Pipeline

```
Dataset
   │
   ▼
Data Cleaning
   │
   ▼
Exploratory Data Analysis
   │
   ▼
Feature Engineering
   │
   ▼
Encoding & Scaling
   │
   ▼
Train/Test Split
   │
   ▼
Random Forest Regression
   │
   ▼
Hyperparameter Tuning
   │
   ▼
Model Evaluation
   │
   ▼
Fuel Efficiency Prediction
```

---

## 📊 Model Performance

| Metric | Result |
|--------|--------|
| Algorithm | Random Forest Regression |
| R² Score | **0.96** |

The model achieved an **R² Score of 0.96**, demonstrating excellent predictive performance and the ability to accurately estimate vehicle fuel efficiency based on input features.

---

## 📈 Key Input Features

- Engine Power (kW)
- Vehicle Mass (kg)
- Engine Capacity (cc)
- Fuel Type
- Fuel Efficiency Class

---

## 📁 Project Structure

```
Fuel_Efficiency_Prediction/
│
├── data/
├── notebooks/
├── model/
├── fuel_pipeline.joblib
├── requirements.txt
├── README.md
└── app.py
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/mohanraj-Ai/Fuel_Efficiency_Prediction.git
```

### Navigate to the Project

```bash
cd Fuel_Efficiency_Prediction
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Project

```bash
jupyter notebook
```

or

```bash
python app.py
```

---

## 📸 Project Demo

Include screenshots such as:

- Dataset Overview
- Data Visualization
- Model Training
- Prediction Results
- Feature Importance

---

## 🔮 Future Enhancements

- Compare with XGBoost and LightGBM
- Deploy using Streamlit or FastAPI
- Real-time prediction API
- Cloud deployment on AWS
- Model explainability with SHAP

---

## 👨‍💻 Author

**Mohanraj P**

**AI Engineer | Generative AI | Machine Learning | Computer Vision**

🔗 LinkedIn: https://www.linkedin.com/in/mohanraj-p-2bb994217/

💻 GitHub: https://github.com/mohanraj-Ai

---

⭐ If you found this project useful, consider giving it a **Star** on GitHub!

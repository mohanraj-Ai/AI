
# 🚗 Vehicle Fuel Efficiency Predictor

> **Data-Driven Intelligence for the Modern Road**

A machine learning project that predicts **vehicle fuel efficiency (km/L)** using key automotive specifications such as vehicle mass, engine power, engine capacity, and fuel type.

The project develops an end-to-end machine learning pipeline covering **large-scale data engineering, exploratory analysis, model benchmarking, validation, and prediction**.

---

## 📌 Project Overview

Fuel efficiency is influenced by several mechanical characteristics of a vehicle. This project uses machine learning to identify the relationship between vehicle specifications and fuel efficiency and build a predictive model capable of estimating mileage for unseen vehicles.

The project processes a large-scale dataset containing **10M+ vehicle records** and focuses on important internal-combustion-engine attributes.

### Key Objectives

* Analyze vehicle specifications affecting fuel efficiency
* Clean and preprocess large-scale automotive data
* Handle missing values and abnormal observations
* Engineer a more intuitive fuel-efficiency target
* Compare multiple regression algorithms
* Select the best-performing model
* Validate predictions on unseen data
* Predict vehicle mileage in **km/L**

---

## 🏗️ Project Pipeline

```text
Raw Vehicle Dataset
        │
        ▼
Data Cleaning & Preprocessing
        │
        ├── Feature Sanitization
        ├── Missing Value Imputation
        ├── Feature Pruning
        └── Outlier Handling
        │
        ▼
Feature Engineering
        │
        ▼
Exploratory Data Analysis
        │
        ▼
Model Benchmarking
        │
        ├── Linear Regression
        ├── Ridge / Lasso
        ├── SVR
        ├── Decision Tree
        ├── KNN
        ├── XGBoost
        └── Random Forest
        │
        ▼
Best Model Selection
        │
        ▼
Random Forest Regressor
        │
        ▼
Validation & Prediction
        │
        ▼
Fuel Efficiency (km/L)
```

---

## 📊 Dataset

The project uses a large automotive dataset containing **10M+ vehicle records**.

### Main Features

| Feature                    | Description                  |
| -------------------------- | ---------------------------- |
| `vehicle_mass_kg`          | Vehicle mass in kilograms    |
| `engine_power_kw`          | Engine power in kilowatts    |
| `engine_capacity_cc`       | Engine displacement/capacity |
| `fuel_type`                | Petrol/Diesel category       |
| `fuel_efficiency_km_per_l` | Target variable              |

Electric-specific metrics were removed so that the analysis could focus on **internal-combustion engine efficiency**.

---

## 🧹 Data Preprocessing

The preprocessing pipeline consists of several stages.

### 1. Feature Sanitization

* Cleaned technical feature names
* Removed unnecessary whitespace
* Standardized feature representation

### 2. Missing Value Handling

Missing numerical technical specifications were handled using a **median-based imputation strategy**.

### 3. Feature Pruning

Electric-specific metrics were removed to keep the model focused on petrol and diesel internal-combustion vehicles.

### 4. Outlier Handling

Extreme vehicle specifications were handled using **IQR-based clipping**.

The project used a **1.5 × IQR** boundary to constrain extreme technical specifications.

---

## 🎯 Target Engineering

The original dataset provided fuel consumption in:

```text
L/100km
```

This was transformed into a more intuitive fuel-efficiency metric:

```text
km/L
```

This makes the final prediction easier to understand from a consumer and automotive perspective.

---

## 🔍 Exploratory Data Analysis

The analysis identified several important relationships between vehicle characteristics and fuel efficiency.

### Vehicle Mass

Efficiency decreases significantly as vehicle mass increases, with the analysis highlighting a strong decline beyond approximately **1600 kg**.

### Engine Power

Engine power was identified as one of the strongest predictive variables.

The analysis identified an efficiency range around **70–110 kW**.

### Fuel Type

Diesel vehicles showed higher average thermal efficiency in heavier vehicle segments.

---

## ⭐ Feature Importance

The analysis identified the following major predictive signals:

1. **Engine Power (kW)** — strongest
2. **Vehicle Mass (kg)** — high importance

These features play a major role in predicting vehicle fuel efficiency.

---

# 🤖 Model Benchmarking

Multiple regression algorithms were evaluated to identify the most suitable model.

| Model                       | R² Score |
| --------------------------- | -------: |
| Linear Regression           |     0.54 |
| Ridge / Lasso               |     0.54 |
| Support Vector Regression   |     0.53 |
| Decision Tree               |     0.88 |
| KNN (k=9)                   |     0.90 |
| XGBoost Regressor           |     0.91 |
| **Random Forest Regressor** | **0.96** |

## The tree-based and ensemble models significantly outperformed the linear baselines.

# 🏆 Final Model — Random Forest Regressor

The **Random Forest Regressor** was selected as the final model because of its strong R² score and ability to handle variance across different vehicle classes.

### Model Configuration

```text
Algorithm: Random Forest Regressor
n_estimators: 200
max_depth: 20
criterion: squared_error
```

### Performance

```text
R² Score: 0.96
Mean Absolute Error: 0.35 km/L
```

---

## 📈 Model Performance

| Metric              | Linear Baseline | Random Forest |
| ------------------- | --------------: | ------------: |
| R² Score            |            0.54 |      **0.96** |
| Mean Absolute Error |        3.8 km/L | **0.35 km/L** |

The validation results indicate strong predictive performance on unseen test data.

---

## 🚘 Sample Predictions

| Vehicle        | Real Mileage | Predicted Mileage | Accuracy |
| -------------- | -----------: | ----------------: | -------: |
| Maruti Swift   |   22.00 km/L |        19.71 km/L |    89.6% |
| Honda City     |   17.80 km/L |        18.52 km/L |    95.9% |
| Honda Civic    |   16.50 km/L |        16.59 km/L |    99.5% |
| Toyota Corolla |   16.00 km/L |        17.07 km/L |    93.3% |
| VW Polo        |   18.20 km/L |        18.52 km/L |    98.2% |

---

# 🛠️ Tech Stack

### Programming

* Python

### Machine Learning

* Scikit-learn
* Random Forest
* Decision Tree
* KNN
* Support Vector Regression
* Linear Regression
* Ridge / Lasso
* XGBoost

### Data Processing

* Pandas
* NumPy

### Data Visualization

* Matplotlib
* Seaborn

### Development

* Jupyter Notebook
* VS Code
* Git
* GitHub

---

# 📁 Project Structure

```text
FUEL-EFFICIENCY-PREDICTOR/
│
├── data/
│   └── vehicle_fuel_efficiency.csv
│
├── notebooks/
│   ├── data_analysis.ipynb
│   ├── preprocessing.ipynb
│   └── model_training.ipynb
│
├── models/
│   └── random_forest_model.pkl
│
├── src/
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── train.py
│   └── predict.py
│
├── requirements.txt
├── README.md
└── LICENSE
```

> Adjust the folder names above to match the actual files in your repository.

---

# 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/mohanraj-Ai/FUEL-EFFICIENCY-PREDICTOR.git
cd FUEL-EFFICIENCY-PREDICTOR
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Usage

After installing the dependencies, run the prediction pipeline:

```bash
python src/predict.py
```

Provide the required vehicle specifications:

```text
Vehicle Mass
Engine Capacity
Engine Power
Fuel Type
```

The model returns the estimated:

```text
Fuel Efficiency: XX.XX km/L
```

---

# 💡 Example Prediction

### Input

```text
Vehicle Mass: 1200 kg
Engine Capacity: 1197 cc
Engine Power: 65 kW
Fuel Type: Petrol
```

### Output

```text
Predicted Fuel Efficiency: XX.XX km/L
```

---

# 📊 Business / Automotive Applications

This project can be extended for:

* 🚗 Vehicle mileage estimation
* 🛒 New vehicle comparison
* 💰 Fuel-cost estimation
* 🔧 Automotive service advisory systems
* 📊 Fleet efficiency analysis
* 🌱 Fuel consumption optimization
* 🤖 Automotive AI assistants

---

# 🔮 Future Improvements

* Deploy the model as a **FastAPI REST API**
* Build an interactive **Streamlit dashboard**
* Add real-time vehicle specification input
* Add SHAP-based explainability
* Integrate the model into an automotive AI assistant
* Add automated ML retraining pipelines
* Containerize the application using Docker
* Deploy the prediction API to cloud infrastructure

---

# 📌 Key Results

```text
Dataset Size      : 10M+ vehicle records
Best Algorithm    : Random Forest Regressor
R² Score          : 0.96
MAE               : 0.35 km/L
Estimators        : 200
Max Depth         : 20
Target            : Fuel Efficiency (km/L)
Fuel Categories   : Petrol / Diesel
```

---

# 👨‍💻 Author

**Mohanraj P**

Automobile Engineer | Machine Learning Engineer | AI Engineer

Interested in building **AI/ML solutions for the automotive industry**.

---

# 🔗 Repository

GitHub Repository:

**https://github.com/mohanraj-Ai/FUEL-EFFICIENCY-PREDICTOR**

---

## ⭐ If you find this project useful

Give the repository a ⭐ and feel free to explore, improve, and contribute to the project.

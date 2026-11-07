import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load saved model and scaler
scaler = joblib.load("scaler.pkl")
kmeans = joblib.load("kmeans_model.pkl")

st.title("Employee AI Layoff Risk Cluster Predictor")
st.write("Enter employee details to find their cluster.")

# Input fields
routine_task = st.slider("Routine Task Percentage", 0, 100, 50)
creativity = st.slider("Creativity Requirement", 0, 100, 50)
tasks_automated = st.slider("Tasks Automated Percentage", 0, 100, 30)
human_interaction = st.slider("Human Interaction Level", 0, 100, 50)
ai_training_hours = st.number_input("AI Training Hours", 0, 500, 20)
ai_usage_hours = st.number_input("AI Usage Hours Per Week", 0, 100, 5)
years_experience = st.number_input("Years of Experience", 0, 40, 5)
ai_tools_used = st.number_input("Number of AI Tools Used", 0, 20, 2)

job_level = st.selectbox("Job Level", ["Entry", "Mid", "Senior"])
ai_adoption = st.selectbox("AI Adoption Level", ["Low", "Medium", "High"])

# Encode ordered categories
job_level_map = {"Entry": 0, "Mid": 1, "Senior": 2}
ai_adoption_map = {"Low": 0, "Medium": 1, "High": 2}

job_level_encoded = job_level_map[job_level]
ai_adoption_encoded = ai_adoption_map[ai_adoption]

# Same feature order as training
input_data = pd.DataFrame([[
    routine_task,
    creativity,
    tasks_automated,
    job_level_encoded,
    human_interaction,
    ai_training_hours,
    ai_usage_hours,
    years_experience,
    ai_adoption_encoded,
    ai_tools_used
]], columns=[
    "Routine_Task_Percentage",
    "Creativity_Requirement",
    "Tasks_Automated_Percentage",
    "Job_Level_Encoded",
    "Human_Interaction_Level",
    "AI_Training_Hours",
    "AI_Usage_Hours_Per_Week",
    "Years_of_Experience",
    "AI_Adoption_Level_Encoded",
    "Number_of_AI_Tools_Used"
])

if st.button("Predict Cluster"):
    input_scaled = scaler.transform(input_data)
    cluster = kmeans.predict(input_scaled)[0]

    st.success(f"This employee belongs to Cluster {cluster}")

    cluster_risk = {
        0: "High Layoff Risk",
        1: "Moderate to High Layoff Risk",
        2: "Relatively Low Layoff Risk"
    }

    st.info(f"Cluster Interpretation: {cluster_risk[cluster]}")
import os
import pickle
import pandas as pd


# Project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Model paths
MODEL_PATH = os.path.join(BASE_DIR, "models", "rf_model.sav")
ENCODER_PATH = os.path.join(BASE_DIR, "models", "target_encoder.sav")
COLUMNS_PATH = os.path.join(BASE_DIR, "models", "model_columns.sav")


# Load trained model
with open(MODEL_PATH, "rb") as file:
    model = pickle.load(file)

# Load target encoder
with open(ENCODER_PATH, "rb") as file:
    target_encoder = pickle.load(file)

# Load model columns
with open(COLUMNS_PATH, "rb") as file:
    model_columns = pickle.load(file)


def predict_fuel_efficiency(
    vehicle_mass_kg,
    engine_capacity_cc,
    engine_power_kw,
    fuel_type_diesel
):
    """
    Predict vehicle fuel efficiency class.
    """

    # Create input DataFrame using the same feature names
    input_data = pd.DataFrame([{
        "vehicle_mass_kg": vehicle_mass_kg,
        "engine_capacity_cc": engine_capacity_cc,
        "engine_power_kw": engine_power_kw,
        "fuel_type_diesel": fuel_type_diesel
    }])

    # Ensure the exact same column order as training
    input_data = input_data[model_columns]

    # Predict encoded class
    prediction = model.predict(input_data)

    # Convert encoded class back to original label
    predicted_class = target_encoder.inverse_transform(prediction)[0]

    return predicted_class
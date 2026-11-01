from flask import Flask, render_template, request

from src.prediction import predict_fuel_efficiency


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None
    error = None

    if request.method == "POST":
        try:
            # Get values from the HTML form
            vehicle_mass_kg = float(request.form["vehicle_mass_kg"])
            engine_capacity_cc = float(request.form["engine_capacity_cc"])
            engine_power_kw = float(request.form["engine_power_kw"])

            fuel_type = request.form["fuel_type"]

            # Convert fuel type into the same encoding used during training
            fuel_type_diesel = 1 if fuel_type == "diesel" else 0

            # Make prediction
            prediction = predict_fuel_efficiency(
                vehicle_mass_kg,
                engine_capacity_cc,
                engine_power_kw,
                fuel_type_diesel
            )

        except (ValueError, KeyError):
            error = "Please enter valid values."

    return render_template(
        "index.html",
        prediction=prediction,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)
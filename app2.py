import streamlit as st
import joblib
import pandas as pd

# Load the trained model and preprocessing component
model = joblib.load("random_forest_model.pkl")
preprocessor = joblib.load("preprocessing.pkl")

# Page configuration
st.set_page_config(
    page_title="Machine Failure Prediction",
    page_icon="🏭",
    layout="centered"
)

st.title("🏭 Industrial Machine Failure Prediction")
st.write(
    "Enter the machine's operating conditions to predict "
    "whether it is likely to experience a failure."
)

st.divider()

# Input fields
machine_type = st.selectbox(
    "Machine Type",
    ["L", "M", "H"]
)

air_temp = st.number_input(
    "Air Temperature (K)",
    min_value=290.0,
    max_value=310.0,
    value=300.0,
    step=0.1
)

process_temp = st.number_input(
    "Process Temperature (K)",
    min_value=300.0,
    max_value=320.0,
    value=310.0,
    step=0.1
)

rotational_speed = st.number_input(
    "Rotational Speed (rpm)",
    min_value=1000,
    max_value=3000,
    value=1500,
    step=10
)

torque = st.number_input(
    "Torque (Nm)",
    min_value=0.0,
    max_value=100.0,
    value=40.0,
    step=0.1
)

tool_wear = st.number_input(
    "Tool Wear (min)",
    min_value=0,
    max_value=300,
    value=100,
    step=1
)

st.divider()

# Prediction
if st.button("Predict Machine Failure", use_container_width=True):

    input_data = pd.DataFrame({
        "Type": [machine_type],
        "Air temperature [K]": [air_temp],
        "Process temperature [K]": [process_temp],
        "Rotational speed [rpm]": [rotational_speed],
        "Torque [Nm]": [torque],
        "Tool wear [min]": [tool_wear]
    })

    # Apply the saved preprocessing
    transformed_data = preprocessor.transform(input_data)

    # Predict using the Random Forest model
    prediction = model.predict(transformed_data)[0]

    if prediction == 1:
        st.error("⚠️ Machine Failure Predicted")
        st.write(
            "The model predicts that the machine may experience a failure."
        )
    else:
        st.success("✅ No Machine Failure Predicted")
        st.write(
            "The model predicts that the machine is unlikely to experience a failure."
        )

st.caption(
    "Machine learning model: Random Forest | Dataset: AI4I 2020 Predictive Maintenance"
)
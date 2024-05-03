import streamlit as st
import skops.io as sio

model = sio.load("./model.skops", trusted=True)

def predict_score(
        fixed_acidity, volatile_acidity, citric_acid, residual_sugar, 
        chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, 
        ph, sulphates, alcohol
        ):

    features = [fixed_acidity, volatile_acidity, citric_acid, residual_sugar, 
    chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, 
    ph, sulphates, alcohol]

    predicted_quality = model.predict([features])[0]

    score = f"Predicted Quality Score: {int(round(predicted_quality, 0))}"
    return score

def main():
    st.title("Legal NER Classifier")
    st.write("Enter the details to correctly identify Legal Classes")

    fixed_acidity = st.slider("Fixed Acidity", 4.0, 16.0, step=0.1)
    volatile_acidity = st.slider("Volatile Acidity", 0.01, 2.0, step=0.01)
    citric_acid = st.slider("Citric Acid", 0.0, 1.0, step=0.01)
    residual_sugar = st.slider("Residual Sugar", 0.5, 16.0, step=0.1)
    chlorides = st.slider("Chlorides", 0.001, 0.7, step=0.001)
    free_sulfur_dioxide = st.slider("Free Sulfur Dioxide", 1.0, 72.0, step=1.0)
    total_sulfur_dioxide = st.slider("Total Sulfur Dioxide", 5.0, 290.0, step=2.0)
    density = st.slider("Density", 0.00001, 1.0, step=0.0001)
    ph = st.slider("pH Value", 2.0, 4.0, step=0.01)
    sulphates = st.slider("Sulphates", 0.3, 2.0, step=0.01)
    alcohol = st.slider("Alcohol", 4.0, 16.0, step=0.1)

    if st.button("Predict"):
        prediction = predict_score(
            fixed_acidity, volatile_acidity, citric_acid, residual_sugar, 
            chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, 
            ph, sulphates, alcohol
        )
        st.write(prediction)

if __name__ == "__main__":
    main()
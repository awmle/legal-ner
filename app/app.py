import gradio as gr
import skops.io as sio

model = sio.load("./models/model.skops", trusted=True)


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

inputs = [
    gr.Slider(4, 16, step=0.1, label="Fixed Acidity"),
    gr.Slider(0.01, 2, step=0.01, label="Volatile Acidity"),
    gr.Slider(0.0, 1.0, step=0.01, label="Citric Acid"),
    gr.Slider(0.5, 16, step=0.1, label="Residual Sugar"),
    gr.Slider(0.001, 0.7, step=0.001, label="Chlorides"),
    gr.Slider(1.0, 72.0, step=1.0, label="Free Sulfur Dioxide"),
    gr.Slider(5.0, 290.0, step=2.0, label="Total Sulfur Dioxide"),
    gr.Slider(0.00001, 1.0, step=0.0001, label="Density"),
    gr.Slider(2, 4, step=0.01, label="pH Value"),
    gr.Slider(0.3, 2.0, step=0.01, label="Sulphates"),
    gr.Slider(4, 16, step=0.1, label="Alcohol")
]

examples = [
    [7.4,0.7,0.0,1.9,0.076,11.0,34.0,0.9978,3.51,0.56,9.4],
    [11.2,0.28,0.56,1.9,0.075,17.0,60.0,0.998,3.16,0.58,9.8],
    [7.3,0.65,0.0,1.2,0.065,15.0,21.0,0.9946,3.39,0.47,10.0],
]


title = "Wine Quality Predictor"
description = "Enter the details to correctly identify Wine Quality?"

gr.Interface(
    fn=predict_score,
    inputs=inputs,
    outputs="text",
    examples=examples,
    title=title,
    description=description,
    theme=gr.themes.Soft(),
).launch()

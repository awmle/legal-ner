import plotly.graph_objects as go
import pandas as pd
import numpy as np

import mlflow
import mlflow.spacy
import spacy

import configparser

def read_metrics_file(file_path):
    """Read the contents of the text file."""
    with open(file_path, 'r') as file:
        content = file.readlines()
    return content

def extract_ner_metrics(content):
    """Extract NER metrics from the text content."""
    data = {"NER Type": [], "Precision": [], "Recall": [], "F1 Score": []}
    start_index = content.index("=============================== NER (per type) ===============================\x1b[0m\n")
    for line in content[start_index + 1:]:
        if line.strip():  # Skip empty lines
            parts = line.split()
            if len(parts) == 4:  # Ensure each line contains all four parts
                data["NER Type"].append(parts[0])
                data["Precision"].append(float(parts[1]))
                data["Recall"].append(float(parts[2]))
                data["F1 Score"].append(float(parts[3]))
    return data

def compute_average_metrics(data):
    """Compute average metrics and add them as the 'Average' row."""
    avg_row = {
        "NER Type": "Average",
        "Precision": round(np.mean(data['Precision']), 2),
        "Recall": round(np.mean(data['Recall']), 2),
        "F1 Score": round(np.mean(data['F1 Score']), 2)
    }
    for key, value in avg_row.items():
        data[key].append(value)
    return data

def create_table_figure(data):
    """Create the table figure using Plotly."""
    df = pd.DataFrame(data)
    fig = go.Figure(data=[go.Table(
        header=dict(values=list(df.columns),
                    fill_color='lightblue',
                    align=['left', 'center', 'center', 'center']),  # Align header text
        cells=dict(values=[df["NER Type"], df["Precision"], df["Recall"], df["F1 Score"]],
                   fill_color='white',
                   align=['left', 'center', 'center', 'center']))
    ])
    return fig

def save_table_image(fig, file_path):
    """Save the table image as a PNG file."""
    fig.update_layout(width=800, height=600)
    fig.write_image(file_path)

def track_experiment(data):
    """Track the experiment metrics and model using MLflow"""
    config_file = './src/models/config.cfg'
    config = configparser.ConfigParser()
    config.read(config_file)

    # MLflow Tracking
    nlp = spacy.load('./models/model-last')
    with mlflow.start_run(run_name='Spacy'):
        mlflow.set_tag('model_flavor', 'spacy')
        mlflow.spacy.log_model(spacy_model=nlp, artifact_path='model')
        mlflow.log_metric('Precision', data['Precision'][-1])
        mlflow.log_metric('Recall', data['Recall'][-1])
        mlflow.log_metric('F1 Score', data['F1 Score'][-1])
        mlflow.log_param('max_epochs', config['training'].get('max_epochs'))
        mlflow.log_param('dropout', config['training'].get('dropout'))
        mlflow.log_param('learn_rate', config['training.optimizer'].get('learn_rate'))
        my_run_id = mlflow.active_run().info.run_id

if __name__ == "__main__":
    file_path = './reports/test_metrics.txt'
    content = read_metrics_file(file_path)
    data = extract_ner_metrics(content)
    data = compute_average_metrics(data)
    track_experiment(data)
    fig = create_table_figure(data)
    save_table_image(fig, "./reports/figures/test_metrics.png")
    



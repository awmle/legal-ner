import pytest
import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from src.visualization.visualize import (
    extract_ner_metrics,
    compute_average_metrics,
    read_metrics_file)

@pytest.fixture
def sample_metrics_file(tmp_path):
    content = """=============================== NER (per type) ===============================\x1b[0m
ORG      0.85  0.82  0.83
PERSON   0.78  0.75  0.76"""
    file_path = tmp_path / "test_metrics.txt"
    with open(file_path, 'w') as file:
        file.write(content)
    return file_path

def test_read_metrics_file(sample_metrics_file):
    content = read_metrics_file(sample_metrics_file)
    assert content == ["=============================== NER (per type) ===============================\x1b[0m\n",
                       "ORG      0.85  0.82  0.83\n",
                       "PERSON   0.78  0.75  0.76"]

def test_extract_ner_metrics():
    content = ["=============================== NER (per type) ===============================\x1b[0m\n",
               "ORG      0.85  0.82  0.83\n",
               "PERSON   0.78  0.75  0.76"]
    data = extract_ner_metrics(content)
    assert data == {"NER Type": ["ORG", "PERSON"],
                    "Precision": [0.85, 0.78],
                    "Recall": [0.82, 0.75],
                    "F1 Score": [0.83, 0.76]}

def test_compute_average_metrics():
    data = {"NER Type": ["ORG", "PERSON"],
            "Precision": [0.85, 0.78],
            "Recall": [0.82, 0.75],
            "F1 Score": [0.83, 0.76]}
    avg_data = compute_average_metrics(data)
    assert avg_data["NER Type"] == ["ORG", "PERSON", "Average"]
    assert avg_data["Precision"] == [0.85, 0.78, 0.82]
    assert avg_data["Recall"] == [0.82, 0.75, 0.78]
    assert avg_data["F1 Score"] == [0.83, 0.76, 0.8]
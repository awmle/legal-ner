import pytest
import os

@pytest.fixture
def get_path_figures():
    return "./reports/figures"

@pytest.fixture
def get_path_models():
    return "./models"

# def test_figure_files(get_path_figures):
#     assert 'feature_importance.png' in os.listdir(get_path_figures)
#     assert 'residuals.png' in os.listdir(get_path_figures)

def test_metric_file(get_path_figures):
    assert 'train_metrics.txt' in os.listdir(get_path_figures.rsplit('/',1)[0])

def test_model_file(get_path_models):
    assert 'model-last' in os.listdir(get_path_models)
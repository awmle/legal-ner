import pytest
import os

def test_testmetric_file():
    assert 'test_metrics.txt' in os.listdir('./reports')

def test_trainmetric_file():
    assert 'train_metrics.txt' in os.listdir('./reports')

def test_eval_png():
    assert 'test_metrics.png' in os.listdir('./reports/figures')

def test_model_file():
    assert 'model-last' in os.listdir('./models')

def test_interim_data():
    assert 'NER_DEV.json' in os.listdir('./data/interim')
    assert 'NER_TEST.json' in os.listdir('./data/interim')
    assert 'NER_TRAIN.json' in os.listdir('./data/interim')

def test_processed_data():
    assert 'DEV.spacy' in os.listdir('./data/processed')
    assert 'TEST.spacy' in os.listdir('./data/processed')
    assert 'TRAIN.spacy' in os.listdir('./data/processed')

def test_ci_config():
    assert 'ci.yml' in os.listdir('./.github/workflows')

def test_cd_config():
    assert 'cd.yml' in os.listdir('./.github/workflows')

def test_train_config():
    assert 'config.cfg' in os.listdir('./src/models')
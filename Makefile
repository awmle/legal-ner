install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black ./src/data/*.py
	black ./src/features/*.py
	black ./src/models/*.py
	black ./src/visualization/*.py
	black ./app/*.py

train:
	python ./src/models/train_model.py

eval:
	echo "## Model Metrics" > report.md
	cat ./reports/metrics.txt >> report.md

	echo "## Data Visualization" >> ./reports/report.md
	echo '![Feature Importance](./reports/figures/feature_importance.png)' >> report.md
	echo '![Residuals](./reports/figures/residuals.png)' >> report.md
   
	cml comment create report.md

hf-login:
    git pull origin dev
    git switch dev
    pip install -U "huggingface_hub[cli]"
    huggingface-cli login --token $(HF_TOKEN) --add-to-git-credential

push-to-hf:
    huggingface-cli upload ali-waheed-aw/wine-ml ./app --repo-type=space --commit-message="Sync App files"
    huggingface-cli upload ali-waheed-aw/wine-ml ./models --repo-type=space --commit-message="Sync Model"
    huggingface-cli upload ali-waheed-aw/wine-ml ./reports --repo-type=space --commit-message="Sync Metrics"

deploy: hf-login push-to-hf

unit_test:
	pytest
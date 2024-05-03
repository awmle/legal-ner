install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black ./src/data/*.py
	black ./src/features/*.py
	black ./src/models/*.py
	black ./src/visualization/*.py

train:
	python ./src/models/train_model.py

eval:
	echo "## Model Metrics" > report.md
	cat ./reports/metrics.txt >> report.md

	echo "## Data Visualization" >> ./reports/report.md
	echo '![Feature Importance](./reports/figures/feature_importance.png)' >> report.md
	echo '![Residuals](./reports/figures/residuals.png)' >> report.md
   
	cml comment create report.md

update-prod:
	git config --global user.name $(USER_NAME)
	git config --global user.email $(USER_EMAIL)
	git commit -am "Updated prod"
	git push --force origin HEAD:prod

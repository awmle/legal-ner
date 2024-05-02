install:
    pip install --upgrade pip &&\
        pip install -r requirements.txt

format:
    black *.py

train:
    python ./src/models/train_model.py

eval:
    echo "## Model Metrics" > report.md
    cat ./reports/metrics.txt >> report.md
   
    echo "## Data Visualization" >> ./reports/report.md
    echo '![Feature Importance](./reports/figures/feature_importance.png)' >> report.md
	echo '![Residuals](./reports/figures/residuals.png)' >> report.md
   
    cml comment create report.md

	# echo "## Model Metrics" > ./reports/report.md
	# cat ./reports/metrics.txt >> ./reports/report.md
	# echo "## Data Visualization" >> ./reports/report.md
	# cml-publish ./reports/figures/feature_importance.png --md >> ./reports/report.md
	# cml-publish ./reports/figures/residuals.png --md >> ./reports/report.md
	# cml-send-comment ./reports/report.md
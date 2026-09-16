# Earlier Stages of Alzheimer's Disease Prediction Project

![Alzheimer's Screener Prediction Interface](docs/screenshots/prediction.png)

## Overview

This project is an **Educational and Research Prototype** designed to predict the likelihood of the earlier stages of Alzheimer's disease based on patient biomarkers using Machine Learning. The prototype accepts inputs for specific proteins and enzymes and utilizes trained models to output a probability percentage.

### ⚠️ Medical Disclaimer
This project is an educational and research prototype for Alzheimer's disease prediction/screening. It is **not a medical diagnostic device** and should not be used as a substitute for professional evaluation by a qualified healthcare provider. 

## Features
- **Machine Learning Backend**: Employs `LinearSVC` and `LogisticRegression` to calculate risk probability.
- **Reproducible Pipeline**: Includes a training script (`train.py`) to reproducibly train the models and save them.
- **Modern Web Interface**: A clean, responsive Bootstrap 5 based web interface for inputting biomarkers.
- **REST API via Flask**: A lightweight Python backend connecting the ML models to the user interface.

## Technology Stack
- **Backend**: Python 3.11, Flask
- **Machine Learning**: scikit-learn, pandas, numpy
- **Frontend**: HTML5, CSS3 (Bootstrap 5)
- **Deployment Ready**: Configured with `Procfile` and `gunicorn`

## Project Structure
```text
.
├── app.py                                   # Flask web server and prediction routing
├── train.py                                 # Script to train and serialize the ML models
├── dataset-test-train-with-3-features.csv   # The biomarker dataset
├── requirements.txt                         # Python dependencies
├── Procfile                                 # Heroku deployment configuration
├── runtime.txt                              # Heroku Python runtime version
├── models/                                  # Directory containing serialized models
│   ├── linear_svm.pkl
│   ├── logistic_regression.pkl
│   └── scaler.pkl
└── templates/
    └── index.html                           # The frontend user interface
```

## Dataset
The dataset contains three specific biomarkers collected for Alzheimer's disease screening:
1. **Cystatin C** (Protein)
2. **MMP10** (Enzyme)
3. **Tau** (Protein)

## Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/kashish09121/Earlier-Stages-of-Alzheimer-s-disease-prodiction-project.git
cd Earlier-Stages-of-Alzheimer-s-disease-prodiction-project
```

### 2. Create and Activate a Virtual Environment
```bash
# On Windows
python -m venv .venv
.\.venv\Scripts\activate

# On macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Train the Models
Generate the modern, reproducible model files (`.pkl`) locally:
```bash
python train.py
```
*This will parse `dataset-test-train-with-3-features.csv` and save the serialized models into the `models/` directory.*

### 5. Start the Application
Run the Flask development server:
```bash
python app.py
```

### 6. Open the Application
Navigate to `http://127.0.0.1:5000` in your web browser.

## Limitations
- **Feature Set**: The model is trained on a highly restricted feature set (only 3 biomarkers).
- **Clinical Validation**: The model has not been clinically validated and must not be used for actual medical diagnosis.
- **Dataset Size**: The provided dataset is small and may not represent the general population accurately.

## Author
**Kashish**
- Email: [kashish09121@gmail.com](mailto:kashish09121@gmail.com)
- GitHub: [kashish09121](https://github.com/kashish09121)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements
- Dataset provided for educational and machine learning research purposes.
- Frontend developed using Bootstrap 5.

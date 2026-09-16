import os
import math
import pickle
import numpy as np
from flask import Flask, request, render_template

app = Flask(__name__)

def sigmoid(x):
    """Sigmoid activation function to convert decision boundary values to probabilities."""
    return 1 / (1 + math.exp(-x))

# Load the scaler and models
models_dir = os.path.join(os.path.dirname(__file__), 'models')

try:
    with open(os.path.join(models_dir, "scaler.pkl"), "rb") as fp:
        scaler = pickle.load(fp)
    with open(os.path.join(models_dir, "linear_svm.pkl"), "rb") as fp:
        model1 = pickle.load(fp)
    with open(os.path.join(models_dir, "logistic_regression.pkl"), "rb") as fp:
        model2 = pickle.load(fp)
except FileNotFoundError:
    print("Warning: Model files not found. Please run train.py first.")
    scaler, model1, model2 = None, None, None

@app.route('/')
def home():
    """Render the homepage."""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """
    Handle prediction requests from the HTML GUI.
    """
    if scaler is None or model1 is None or model2 is None:
        return render_template('index.html', prediction_text='Error: Models are not trained yet. Run train.py first.')

    try:
        # Extract features (Cystatin C, MMP10, tau)
        # request.form values come in order of the inputs in the HTML form
        features = [float(x) for x in request.form.values()]
        
        if len(features) != 3:
            return render_template('index.html', prediction_text='Error: Expected exactly 3 features.')
            
        final_features = scaler.transform([features])
        
        # Convert linear svm's prediction to probability using sigmoid on decision_function
        dec_func = model1.decision_function(final_features)
        # Check if decision_function returned a scalar or array
        dec_val = dec_func[0] if isinstance(dec_func, np.ndarray) else dec_func
        out1 = sigmoid(dec_val)
        
        # Get prediction probability for class 1 from logistic regression
        out2 = model2.predict_proba(final_features)[0][1]

        # Their average is the final output probability
        final_output = np.mean([out1, out2])
        chance = round(final_output * 100, 2)
        
        prediction_text = f"Chance of Alzheimer's disease is {chance}%"
        
    except ValueError:
        prediction_text = "Error: Please enter valid numerical values for all fields."
    except Exception as e:
        prediction_text = f"Error processing request: {str(e)}"
        
    return render_template('index.html', prediction_text=prediction_text)

if __name__ == "__main__":
    app.run(debug=True)
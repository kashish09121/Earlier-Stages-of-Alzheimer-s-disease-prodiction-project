import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
import pickle
import os

def main():
    # Load dataset
    print("Loading dataset...")
    df = pd.read_csv('dataset-test-train-with-3-features.csv')
    
    # Features and target
    X = df[['Cystatin_C', 'MMP10', 'tau']]
    y = df['Class']

    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Scale the features
    print("Scaling features...")
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Train Linear SVC
    print("Training Linear SVM...")
    model1 = LinearSVC(random_state=42, max_iter=10000)
    model1.fit(X_train_scaled, y_train)

    # Train Logistic Regression
    print("Training Logistic Regression...")
    model2 = LogisticRegression(random_state=42, max_iter=10000)
    model2.fit(X_train_scaled, y_train)

    # Evaluate models
    score1 = model1.score(X_test_scaled, y_test)
    score2 = model2.score(X_test_scaled, y_test)
    print(f"Linear SVM Test Accuracy: {score1:.4f}")
    print(f"Logistic Regression Test Accuracy: {score2:.4f}")

    # Create models directory
    os.makedirs('models', exist_ok=True)

    # Save models and scaler
    print("Saving models to models/ ...")
    with open('models/scaler.pkl', 'wb') as f:
        pickle.dump(scaler, f)
    with open('models/linear_svm.pkl', 'wb') as f:
        pickle.dump(model1, f)
    with open('models/logistic_regression.pkl', 'wb') as f:
        pickle.dump(model2, f)
    
    print("Done! Models have been successfully trained and serialized.")

if __name__ == "__main__":
    main()

import joblib
import numpy as np

# Load the models
logistic_model_path = 'logistic_regression_model.pkl'
rf_model_path = 'random_forest_model.pkl'

logistic_model = joblib.load(logistic_model_path)
rf_model = joblib.load(rf_model_path)

def make_prediction(features, model):
    # Convert features to the correct shape
    features = np.array(features).reshape(1, -1)
    # Make prediction
    prediction = model.predict(features)
    return int(prediction[0])

if __name__ == "__main__":
    # Example features (replace these with actual feature values)
    example_features = [
        30,      # Age in years
        50000,   # Annual income in dollars
        2,       # Number of dependents
        0,       # Owns house (0 = No, 1 = Yes)
        1,       # Owns car (0 = No, 1 = Yes)
        5,       # Years at current job
        2,       # Number of credit cards
        1,       # Previously defaulted (0 = No, 1 = Yes)
        1000,    # Current debt in dollars
        750,     # Monthly mortgage/rent in dollars
        20,      # Monthly expenses in dollars
        1,       # Active loans (0 = No, 1 = Yes)
        0,       # Previously bankrupt (0 = No, 1 = Yes)
        700,     # Credit score
        1,       # Employed (0 = No, 1 = Yes)
        2,       # Education level (0 = None, 1 = High School, 2 = College)
        3,       # Marital status (0 = Single, 1 = Married, 2 = Divorced, 3 = Widowed)
        0.5      # Loan to value ratio
    ]

    # Make predictions using both models
    logistic_prediction = make_prediction(example_features, logistic_model)
    rf_prediction = make_prediction(example_features, rf_model)

    print(f"Input Features: {example_features}")
    print(f"Logistic Regression Prediction: {logistic_prediction}")
    print(f"Random Forest Prediction: {rf_prediction}")

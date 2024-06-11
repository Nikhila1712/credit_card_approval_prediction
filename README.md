# credit_card_approval_prediction

This project aims to predict credit card approval using a logistic regression model. The process involves several key steps:

Data Collection and Preparation:

The dataset, containing various financial and personal attributes, is cleaned and preprocessed.
Missing values are handled, duplicates are removed, and categorical variables are encoded for machine-learning compatibility.

Source: https://www.kaggle.com/datasets/rikdifos/credit-card-approval-prediction

Feature Engineering:

New features are created, such as AGE, YEARS_EMPLOYED, and INCOME_PER_FAM_MEMBER, to improve model performance.
Data is split into training and testing sets, and features are scaled for uniformity.

Handling Imbalanced Data:

The class imbalance issue is addressed using SMOTE (Synthetic Minority Over-sampling Technique) to ensure balanced training data.

Model Building and Evaluation:

A logistic regression model is trained and evaluated using metrics like accuracy, precision, recall, and F1 score.
Hyperparameter tuning is performed using GridSearchCV to optimize model parameters.

Model Deployment with Flask:

A Flask API is created to serve the model, with an endpoint to handle prediction requests.
The Flask server is run locally for testing and can be deployed to a production environment.

Interactive Web Interface with Streamlit:

A Streamlit app provides an interactive web interface for users to input data and receive predictions.
The Streamlit app communicates with the Flask API to fetch prediction results and display them.

Deployment on Streamlit Community Cloud:
The Streamlit app is deployed on the Streamlit Community Cloud, providing a public interface for the model.

GitHub Repository:
The project is version-controlled using Git and hosted on GitHub, ensuring reproducibility and collaboration.

Instructions for Running the Project Locally:
1. Clone the repository.
2. Set up a virtual environment and install dependencies.
3. Run the Flask server.
4. Run the Streamlit app.

Instructions for Running the Project Locally
Clone the Repository:

git clone "Local Repository'
cd credit_card_analysis

Set Up Virtual Environment:
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

Install Dependencies:
pip install -r requirements.txt

Run Flask Server:
python app.py

Run Streamlit App:
streamlit run app-1.py





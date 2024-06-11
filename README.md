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

# Key Insights 
Performance Metrics:
Training Accuracy: 56.36%
Test Accuracy: 59.06%
Other metrics such as precision, recall, and F1 score were also evaluated, with the best logistic regression model achieving:
Precision: 0.15%
Recall: 49.09%
F1

1. Annual income and income per family member were significant factors. Applicants with higher incomes and higher income per family member were more likely to be approved for credit cards.
   Visualization revealed a clear trend where higher income groups had higher approval rates.

2. Years of employment had a positive impact on approval rates. Applicants with longer employment durations were favored, indicating stability and reliability.
   The data showed that applicants with over five years of employment had notably higher approval rates.

3. Credit score was one of the most critical factors. Higher credit scores are strongly correlated with higher approval chances.
   Additionally, applicants with fewer defaults and active loans were more likely to be approved, highlighting the importance of a clean credit history.

4. The ratio of current debt to income was a crucial metric. Lower debt-to-income ratios were associated with higher approval rates.
   Applicants with lower monthly mortgage/rent and overall debt levels had better approval odds.

5. Age and marital status also played roles. Middle-aged applicants and those who were married or widowed tended to have higher approval rates.
   Younger applicants and those with multiple dependents had lower approval probabilities, likely due to perceived higher financial risk.








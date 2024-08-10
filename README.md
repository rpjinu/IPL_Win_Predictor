# IPL_Win_Predictor
whole project analysis ,building model and deployment
## Images Deploment
Include images or screenshots of the application and visualizations.

<img src="https://github.com/rpjinu/IPL_Win_Predictor/blob/main/deploy_image1.png" width="900">

#deploy image 2
<img src="https://github.com/rpjinu/IPL_Win_Predictor/blob/main/deploy_image2.png" width="900">

IPL Win Prediction
This project aims to predict the outcome of IPL matches using a machine learning model deployed on Heroku. The project includes data preprocessing, model training, and deployment in a web application using Streamlit.

Table of Contents
Project Overview
Installation
Data Description
Model Training
Web App Deployment
Heroku Deployment
Usage
License
Acknowledgements
Project Overview
The IPL Win Prediction project predicts the outcome of cricket matches based on several features such as the batting team, bowling team, current run rate (CRR), required run rate (RRR), and others. The model is built using Logistic Regression, and the web application is developed using Streamlit and deployed on Heroku.

Installation
Clone the Repository
bash
Copy code
git clone https://github.com/your-username/ipl-win-prediction.git
cd ipl-win-prediction
Set Up a Virtual Environment
bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install Dependencies
bash
Copy code
pip install -r requirements.txt
Data Description
The dataset used for this project contains the following features:

batting_team: The team currently batting.
bowling_team: The team currently bowling.
city: The city where the match is being played.
runs_left: Runs needed to win the match.
balls_left: Balls remaining in the match.
wickets: Wickets remaining for the batting team.
total_runs_x: Total runs scored so far by the batting team.
crr: Current Run Rate of the batting team.
rrr: Required Run Rate needed to win.
result: The outcome of the match (win/lose).
Model Training
Data Preprocessing:

Handling missing values.
Encoding categorical variables.
Splitting the data into training and test sets.
Pipeline Setup:

Using ColumnTransformer to preprocess the data.
Implementing LogisticRegression as the base model.
Training the model using the training dataset.
Model Evaluation:

Evaluating model performance using accuracy, precision, recall, and F1-score.
Fine-tuning the model for better performance.
Web App Deployment
The web application is developed using Streamlit, which provides an interactive interface for users to input data and get predictions.

Create the Streamlit App:

Develop the app interface.
Integrate the trained model with the app to make predictions.
Test the Application Locally:

bash
Copy code
streamlit run app.py
Heroku Deployment
Step 1: Create a Procfile
Create a Procfile in the root directory with the following content:

text
Copy code
web: streamlit run app.py
Step 2: Set Up Heroku CLI
Install the Heroku CLI from Heroku's official site.
Step 3: Login to Heroku
bash
Copy code
heroku login
Step 4: Create a New Heroku App
bash
Copy code
heroku create ipl-win-prediction-app
Step 5: Add Git Remote
bash
Copy code
git remote add heroku https://git.heroku.com/ipl-win-prediction-app.git
Step 6: Deploy to Heroku
bash
Copy code
git push heroku main
Step 7: Open the App
bash
heroku open

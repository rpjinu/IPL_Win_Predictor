import streamlit as st
import pickle
import pandas as pd

# Define teams and cities
teams = ['Sunrisers Hyderabad', 'Mumbai Indians', 'Royal Challengers Bangalore', 'Kolkata Knight Riders',
         'Kings XI Punjab', 'Chennai Super Kings', 'Rajasthan Royals', 'Delhi Capitals']

cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi', 'Chandigarh', 'Jaipur',
          'Chennai', 'Cape Town', 'Port Elizabeth', 'Durban', 'Centurion', 'East London', 'Johannesburg',
          'Kimberley', 'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala', 'Visakhapatnam',
          'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi', 'Sharjah', 'Mohali', 'Bengaluru']

# Load the trained model pipeline
pipe = pickle.load(open('pipeline.pkl', 'rb'))

# Set the title of the app
st.title('IPL Win Predictor')

# Create two columns
col1, col2 = st.columns(2)

# Input for batting team
with col1:
    batting_team = st.selectbox('Select the batting team', sorted(teams))

# Input for bowling team
with col2:
    bowling_team = st.selectbox('Select the bowling team', sorted(teams))

# Input for the city
selected_city = st.selectbox('Select host city', sorted(cities))

# Input for the target
target = st.number_input('Target')

# Create three columns for score, overs, and wickets
col3, col4, col5 = st.columns(3)

# Input for score
with col3:
    score = st.number_input('Score')

# Input for overs completed
with col4:
    overs = st.number_input('Overs completed')

# Input for wickets out
with col5:
    wickets = st.number_input('Wickets out')

# Predict button
if st.button('Predict Probability'):
    # Calculating additional features
    runs_left = target - score
    balls_left = 120 - (overs * 6)
    remaining_wickets = 10 - wickets
    crr = score / overs if overs > 0 else 0
    rrr = (runs_left * 6) / balls_left if balls_left > 0 else 0

    # Creating the input dataframe for prediction
    input_df = pd.DataFrame({
        'batting_team': [batting_team],
        'bowling_team': [bowling_team],
        'city': [selected_city],
        'runs_left': [runs_left],
        'balls_left': [balls_left],
        'wickets': [remaining_wickets],
        'total_runs_x': [target],
        'crr': [crr],
        'rrr': [rrr]
    })

    result=pipe.predict_proba(input_df)
    st.text(result)
    loss = result[0][0]
    win = result[0][1]
    st.header(batting_team + "- " + str(round(win * 100)) + "%")
    st.header(bowling_team + "- " + str(round(loss * 100)) + "%")



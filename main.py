import streamlit as st
import requests
import subprocess

# Streamlit UI
st.title('Simple Streamlit App')

# Get user input for the Flask app's base URL
flask_base_url = st.text_input('Enter Flask App Base URL', 'http://127.0.0.1:5000')


subprocess.run(['python', 'app.py'])

# Button to send request to the Flask API
if st.button('Send Request'):
    try:
        # Make a GET request to the Flask API
        flask_base_url = "http://192.168.2.192:5000"
        response = requests.get(f'{flask_base_url}/api/demo')
        
        # Display the response
        st.text(f'Response Status Code: {response.status_code}')
        st.json(response.json())
    except requests.RequestException as e:
        st.text(f'Error: {e}')

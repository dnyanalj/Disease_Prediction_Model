import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menuf

# loading the saved models

diabetes_model = pickle.load(open(r'C:\\Users\\dnyan\\OneDrive\\Desktop\\projects\\HCI PROJECT\\saved_models\\diabetes_model.sav','rb'))

heart_disease_model = pickle.load(open(r'C:\\Users\\dnyan\\OneDrive\\Desktop\\projects\\HCI PROJECT\\saved_models\\heart_disease_model.sav','rb'))

parkinsons_model = pickle.load(open(r'C:\\Users\\dnyan\\OneDrive\\Desktop\\projects\\HCI PROJECT\\saved_models\\parkinsons_model.sav','rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',

                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person'],
                           default_index=0)
    
if selected == 'Diabetes Prediction':
    # page title
    st.title('Diabetes Prediction using ML')
if selected == 'Heart Disease Prediction':

    # page title
    st.title('Heart Disease Prediction using ML')
if selected == "Parkinsons Prediction":

    # page title
    st.title("Parkinson's Disease Prediction using ML")
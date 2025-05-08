# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import time

# Set page configuration
st.set_page_config(
    page_title="Health Predictor AI",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stApp {
        background-image: linear-gradient(to bottom right, #f8f9fa, #e9ecef);
    }
    .css-18e3th9 {
        padding-top: 2rem;
    }
    .stButton>button {
        background-color: #3498db;
        color: white;
        border-radius: 10px;
        padding: 0.5rem 1rem;
        font-weight: bold;
        border: none;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #2980b9;
    }
    .prediction-box {
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
        font-weight: bold;
        text-align: center;
        font-size: 18px;
    }
    .positive-prediction {
        background-color: #fadbd8;
        border: 2px solid #e74c3c;
        color: #c0392b;
    }
    .negative-prediction {
        background-color: #d5f5e3;
        border: 2px solid #2ecc71;
        color: #27ae60;
    }
    .stSlider>div>div>div {
        background-color: #3498db;
    }
    h1 {
        color: #2c3e50;
        text-align: center;
        margin-bottom: 30px;
        padding-bottom: 10px;
        border-bottom: 2px solid #3498db;
    }
    .disease-icon {
        font-size: 3rem;
        text-align: center;
        display: block;
        margin-bottom: 20px;
    }
    .info-box {
        background-color: #e8f4f8;
        padding: 15px;
        border-radius: 5px;
        border-left: 5px solid #3498db;
        margin-bottom: 20px;
    }
    .sidebar .css-1d391kg {
        background-color: #2c3e50;
    }
    </style>
""", unsafe_allow_html=True)

# Custom container for predictions
def show_prediction(prediction_text, positive):
    style_class = "positive-prediction" if positive else "negative-prediction"
    st.markdown(f"""
        <div class="prediction-box {style_class}">
            {prediction_text}
        </div>
    """, unsafe_allow_html=True)

# Info box for displaying helpful information
def info_box(text):
    st.markdown(f"""
        <div class="info-box">
            {text}
        </div>
    """, unsafe_allow_html=True)

# Loading animation
def loading_animation():
    with st.spinner('Analyzing your data...'):
        progress_bar = st.progress(0)
        for i in range(100):
            time.sleep(0.01)
            progress_bar.progress(i + 1)

# Loading the saved models
@st.cache_resource
def load_models():
    try:
        # Update these paths to match your actual file locations
        heart_model = pickle.load(open('HeartDisease_model.sav', 'rb'))
        parkinsons_model = pickle.load(open('Parkinson_model.sav', 'rb'))
        return heart_model, parkinsons_model
    except FileNotFoundError:
        st.error("Model files not found. Please check the file paths.")
        return None, None

HeartDisease_model, Parkinson_model = load_models()

# Sidebar with logo and menu
with st.sidebar:
    st.markdown('<h1 style="text-align: center; color: #3498db;">Health Predictor AI</h1>', unsafe_allow_html=True)
    
    st.markdown('---')
    
    selected = option_menu(
        'Disease Prediction System',
        ['Home', 'Heart Disease Prediction', 'Parkinsons Prediction', 'About'],
        icons=['house', 'heart-pulse', 'person-walking', 'info-circle'],
        menu_icon='hospital',
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "#3498db", "font-size": "25px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#3498db"},
        }
    )
    
    st.markdown('---')
    st.markdown('### Contact')
    st.markdown('📧 nmniffco28@gmail.com')
    st.markdown('🌐 www.healthpredictor.example')

# Home page
if selected == 'Home':
    st.title('Welcome to Disease Predictor AI')
    
    col1, col2, col3 = st.columns([1,2,1])

    st.markdown("""
    ## About The Platform
    
    Disease Predictor AI is a machine learning-powered platform designed to provide preliminary 
    health assessments. Our system can help identify potential risks for:
    
    - **Heart Disease** - Using cardiovascular parameters and health indicators
    - **Parkinson's Disease** - Based on voice recording analysis parameters
    
    ### How It Works
    
    1. Select the disease prediction tool you want to use
    2. Enter the required health parameters
    3. Get an instant preliminary assessment
    
    ### Important Disclaimer
    
    This tool is for educational and informational purposes only. It should not replace 
    professional medical advice, diagnosis, or treatment. Always consult with qualified 
    healthcare providers for any health concerns.
    """)
    

# Heart Disease Prediction Page
elif selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')
    
    st.markdown('<span class="disease-icon">❤️</span>', unsafe_allow_html=True)
    
    info_box("""
        <strong>Heart Disease Prediction</strong><br>
        Please enter the required values to predict potential heart disease risk.
        All fields are required for accurate prediction.
    """)
    
    # Create two columns for inputs
    col1, col2 = st.columns(2)
    
    # Left column inputs
    with col1:
        age = st.text_input('Age')
        sex = st.text_input('Sex')
        cp = st.text_input('Chest Pain types')
        trestbps = st.text_input('Resting Blood Pressure')
        chol = st.text_input('Serum Cholestoral in mg/dl')
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        restecg = st.text_input('Resting Electrocardiographic results')
    
    # Right column inputs
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        exang = st.text_input('Exercise Induced Angina')
        oldpeak = st.text_input('ST depression induced by exercise')
        slope = st.text_input('Slope of the peak exercise ST segment')
        ca = st.text_input('Major vessels colored by flourosopy')
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # Centered button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        predict_button = st.button('Heart Disease Test Result')
        
    # Prediction section
    heart_diagnosis = ''
    
    if predict_button:
        loading_animation()
        
        try:
            user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
            user_input = [float(x) for x in user_input]
            
            heart_prediction = HeartDisease_model.predict([user_input])
            
            st.subheader("Analysis Results")
            
            if heart_prediction[0] == 1:
                heart_diagnosis = 'The person is having heart disease'
                show_prediction(heart_diagnosis, True)
            else:
                heart_diagnosis = 'The person does not have any heart disease'
                show_prediction(heart_diagnosis, False)
                
        except ValueError:
            st.error("Please ensure all fields are filled with valid numerical values")
        except Exception as e:
            st.error(f"An error occurred: {e}")

# Parkinsons Prediction Page
elif selected == 'Parkinsons Prediction':
    st.title("Parkinson's Disease Prediction using ML")
    
    st.markdown('<span class="disease-icon">🧠</span>', unsafe_allow_html=True)
    
    info_box("""
        <strong>Parkinson's Disease Prediction</strong><br>
        Please enter all the required values from voice recording analysis to predict potential Parkinson's disease.
    """)
    
    # Create 5 columns as in the original code
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # Centered button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        predict_button = st.button("Parkinson's Test Result")
    
    # Prediction section
    parkinsons_diagnosis = ''
    
    if predict_button:
        loading_animation()
        
        try:
            user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                        RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5,
                        APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]
                        
            user_input = [float(x) for x in user_input]
            
            parkinsons_prediction = Parkinson_model.predict([user_input])
            
            st.subheader("Analysis Results")
            
            if parkinsons_prediction[0] == 1:
                parkinsons_diagnosis = "The person has Parkinson's disease"
                show_prediction(parkinsons_diagnosis, True)
            else:
                parkinsons_diagnosis = "The person does not have Parkinson's disease"
                show_prediction(parkinsons_diagnosis, False)
                
        except ValueError:
            st.error("Please ensure all fields are filled with valid numerical values")
        except Exception as e:
            st.error(f"An error occurred: {e}")

# About Page
elif selected == 'About':
    st.title('About Health Predictor AI')
    
    st.markdown("""
    ## Our Mission
    
    Health Predictor AI aims to make preliminary health assessments accessible through 
    advanced machine learning algorithms. Our tools are designed to help identify potential 
    health risks early, encouraging timely medical consultation and intervention.
    
    ## The Technology
    
    Our prediction models are built using supervised machine learning algorithms trained on 
    medically validated datasets. The models analyze patterns in health parameters to identify 
    potential risk indicators.
    
    ### Heart Disease Prediction
    
    The heart disease prediction model analyzes 13 key cardiovascular parameters, including:
    - Age and gender
    - Blood pressure and cholesterol levels
    - ECG results
    - Exercise-induced indicators
    
    ### Parkinson's Disease Prediction
    
    The Parkinson's prediction model analyzes 22 voice recording parameters, including:
    - Frequency variations
    - Jitter and shimmer measurements
    - Nonlinear dynamics indicators
    
    ## Disclaimer
    
    Health Predictor AI is intended for educational and informational purposes only. 
    Our predictions should not be considered medical diagnoses or treatment recommendations. 
    Always consult with qualified healthcare professionals for proper medical advice, diagnosis, 
    and treatment.
    """)
    
    st.subheader("References")
    
    st.markdown("""
    1. World Health Organization. (2021). Cardiovascular diseases (CVDs). WHO.
    2. American Heart Association. (2022). Heart Disease and Stroke Statistics Update.
    3. Parkinson's Foundation. (2022). Statistics on Parkinson's Disease.
    4. Little, M. A., McSharry, P. E., Roberts, S. J., Costello, D. A., & Moroz, I. M. (2007). 
       Exploiting nonlinear recurrence and fractal scaling properties for voice disorder detection. 
       BioMedical Engineering OnLine, 6, 23.
    """)

import streamlit as st
import pandas as pd
import pickle
from PIL import Image

model_path = "decision_tree_model.pkl"
with open(model_path, 'rb') as file:
    model = pickle.load(file)

# Set background image
def set_background(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url({image_url});
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

background_image_url = "https://github.com/SriKumar1313/Sloan_app/raw/main/assets/pexels-minan1398-813269.jpg"
set_background(background_image_url)

# Add welcome page with GLTF model
if "page" not in st.session_state:
    st.session_state.page = "welcome"

if st.session_state.page == "welcome":
    st.markdown("""
    <style>
    .welcome-container {
        text-align: center;
        color: white;
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .welcome-title {
        font-size: 3em;
        animation: sparkles 2s infinite;
    }
    .welcome-subtitle {
        font-size: 1.5em;
    }
    .welcome-button {
        margin-top: 20px;
    }
    @keyframes sparkles {
        0% { text-shadow: 0 0 5px #ffffff; }
        50% { text-shadow: 0 0 20px #ffffff; }
        100% { text-shadow: 0 0 5px #ffffff; }
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="welcome-container">
        <div class="welcome-title">✨ Welcome to the Galaxy App! ✨</div>
        <div class="welcome-subtitle">Discover and classify celestial objects: Stars, Galaxies, or Quasars</div>
        <iframe src="https://sketchfab.com/models/dbb2f075329747a09cc8add2ad05acad/embed?autostart=0" width="800" height="600" frameborder="0" allow="autoplay; fullscreen; vr" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
        <div class="welcome-button">
            <br>
            <button onclick="document.location.reload()">Click Here to Begin 🚀</button>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Click Here to Begin 🚀"):
        st.session_state.page = "main"


if st.session_state.page == "main":
    
    st.title("🌌 Sloan Digital Sky Survey (SDSS) Classifier ✨")


    st.markdown("## Classify Celestial Objects: Stars, Galaxies, or Quasars 🌠")
    st.markdown("""
    Welcome to the SDSS classifier app! This app helps you classify celestial objects into stars, galaxies, or quasars based on their photometric and spectral features. Please enter the parameters below to get started.
    """)

    
    st.markdown("### 🚀 Input Parameters 👇")

    
    with st.expander("Manual Entry"):
        with st.form(key='manual_entry_form'):
            st.markdown("#### 📐 Coordinates")
            ra = st.text_input('Right Ascension (ra)', value='0.0')
            dec = st.text_input('Declination (dec)', value='0.0')

            st.markdown("#### 📊 Magnitudes")
            u = st.text_input('u-band magnitude', value='0.0')
            g = st.text_input('g-band magnitude', value='0.0')
            r = st.text_input('r-band magnitude', value='0.0')
            i = st.text_input('i-band magnitude', value='0.0')
            z = st.text_input('z-band magnitude', value='0.0')

            st.markdown("#### 🌌 Redshift")
            redshift = st.text_input('Redshift', value='0.0')

            manual_submit_button = st.form_submit_button(label='Classify 🔭')


    with st.expander("Upload CSV File"):
        uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
        if uploaded_file is not None:
            input_data = pd.read_csv(uploaded_file)
            st.write("Uploaded Data Preview:")
            st.write(input_data)
            file_submit_button = st.button("Classify from File 🔭")


    if manual_submit_button:
        with st.spinner('Classifying... 🚀'):
            input_data = pd.DataFrame([[float(ra), float(dec), float(u), float(g), float(r), float(i), float(z), float(redshift)]], columns=['ra', 'dec', 'u', 'g', 'r', 'i', 'z', 'redshift'])
            prediction = model.predict(input_data)[0]
        st.success(f"### 🛸 Predicted Object Type: **{prediction}**")
        st.balloons()
        st.markdown("### 🌟 Thank you for using the SDSS Classifier! 🌟")


    if 'file_submit_button' in locals() and file_submit_button and uploaded_file is not None:
        with st.spinner('Classifying... 🚀'):
            predictions = model.predict(input_data)
            input_data['Predicted Class'] = predictions
            st.write("Classification Results:")
            st.write(input_data)
        st.success("### 🛸 Classification Completed!")
        st.balloons()
        st.markdown("### 🌟 Thank you for using the SDSS Classifier! 🌟")


    st.markdown("""
    <style>
        .stApp {
            color: #ffffff;
        }
        .stTextInput>div>input {
            border: 2px solid #ff4b4b;
            background-color: #ffffff;
            color: #000000;
            font-size: 16px;
            padding: 5px;
            border-radius: 10px;
            box-shadow: 0 0 5px #ff4b4b;
            animation: inputglow 1.5s infinite;
        }
        .stButton>button {
            background-color: #ff4b4b;
            color: white;
            border-radius: 10px;
            border: 2px solid #ff4b4b;
            font-size: 20px;
            font-weight: bold;
            animation: glow 1.5s infinite;
        }
        .stButton>button:hover {
            background-color: white;
            color: #ff4b4b;
        }
        @keyframes glow {
            0% { box-shadow: 0 0 5px #ff4b4b; }
            50% { box-shadow: 0 0 20px #ff4b4b; }
            100% { box-shadow: 0 0 5px #ff4b4b; }
        }
        @keyframes inputglow {
            0% { box-shadow: 0 0 5px #ff4b4b; }
            50% { box-shadow: 0 0 10px #ff4b4b; }
            100% { box-shadow: 0 0 5px #ff4b4b; }
        }
    </style>
    """, unsafe_allow_html=True)

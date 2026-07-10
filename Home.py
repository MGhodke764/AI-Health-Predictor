import streamlit as st


# Page configuration

st.set_page_config(
    page_title="AI Health Predictor",
    page_icon="🩺",
    layout="wide"
)


# Custom CSS

st.markdown(
    """
    <style>

    .main-title {
        font-size:55px;
        font-weight:800;
        color:#0B6E99;
        text-align:center;
        margin-top:20px;
        margin-bottom:10px;
    }


    .subtitle {
        font-size:22px;
        text-align:center;
        color:#555;
        margin-bottom:40px;
    }


    .card {

        padding:25px;
        border-radius:15px;
        background-color:#f5f9fc;
        text-align:center;
        box-shadow:0px 4px 12px rgba(0,0,0,0.1);

    }


    .section-title {

        font-size:30px;
        font-weight:700;
        color:#0B6E99;

    }


    </style>
    """,
    unsafe_allow_html=True
)



# ---------------- HEADER ----------------


st.markdown(
    '<div class="main-title">🩺 AI Health Predictor</div>',
    unsafe_allow_html=True
)


st.markdown(
    '<div class="subtitle">Smart Disease Prediction using Machine Learning</div>',
    unsafe_allow_html=True
)



st.write(
    """
    Welcome to an AI-powered healthcare assistant that predicts
    possible diseases based on symptoms using a trained
    Random Forest Machine Learning model.
    """
)



st.divider()



# ---------------- FEATURE CARDS ----------------


st.markdown(
    '<div class="section-title">✨ Features</div>',
    unsafe_allow_html=True
)


col1, col2, col3 = st.columns(3)



with col1:

    st.markdown(
        """
        <div class="card">

        🧠

        <h3>AI Powered</h3>

        Machine Learning based disease prediction

        </div>
        """,
        unsafe_allow_html=True
    )



with col2:

    st.markdown(
        """
        <div class="card">

        📊

        <h3>Confidence Score</h3>

        Probability based prediction results

        </div>
        """,
        unsafe_allow_html=True
    )



with col3:

    st.markdown(
        """
        <div class="card">

        📖

        <h3>Health Information</h3>

        Disease details and precautions

        </div>
        """,
        unsafe_allow_html=True
    )



st.divider()



# ---------------- PROJECT STATS ----------------


st.markdown(
    '<div class="section-title">📈 Project Overview</div>',
    unsafe_allow_html=True
)


col1, col2, col3 = st.columns(3)


with col1:

    st.metric(
        "Algorithm",
        "Random Forest"
    )


with col2:

    st.metric(
        "Input Features",
        "132 Symptoms"
    )


with col3:

    st.metric(
        "Application",
        "Healthcare AI"
    )



st.divider()



# ---------------- HOW TO USE ----------------


st.markdown(
    '<div class="section-title">🚀 How To Use</div>',
    unsafe_allow_html=True
)



st.markdown(
    """
    **Step 1:** Go to the Prediction page from the sidebar 👈

    **Step 2:** Select your symptoms

    **Step 3:** Click on Predict Disease

    **Step 4:** View prediction, confidence score, and precautions


    ⚠️ This application is for educational purposes only and does not replace professional medical advice.
    """
)



st.divider()



st.success(
    "Use the sidebar to explore Prediction, Model Performance, and About Project pages."
)

import streamlit as st


st.set_page_config(
    page_title="About Project",
    page_icon="ℹ️",
    layout="wide"
)


st.markdown(
    """
    <style>

    .title {
        font-size:50px;
        font-weight:800;
        color:#0B6E99;
        text-align:center;
    }


    .subtitle {
        text-align:center;
        font-size:20px;
        color:#555;
    }


    .card {

        padding:25px;
        border-radius:15px;
        background:#f5f9fc;
        text-align:center;
        box-shadow:0px 4px 10px rgba(0,0,0,0.1);

    }

    </style>
    """,
    unsafe_allow_html=True
)



st.markdown(
    '<div class="title">ℹ️ About Project</div>',
    unsafe_allow_html=True
)


st.markdown(
    '<div class="subtitle">AI based healthcare prediction system</div>',
    unsafe_allow_html=True
)



st.divider()



st.subheader(
    "🎯 Project Overview"
)


st.write(
"""
The AI Disease Prediction System is a Machine Learning application
that predicts possible diseases based on symptoms.

The system uses a Random Forest Classifier to analyze user inputs
and provide disease predictions with confidence scores.
"""
)



st.divider()



st.subheader(
    "🛠️ Technologies Used"
)


c1,c2,c3 = st.columns(3)


with c1:
    st.markdown(
        """
        <div class="card">
        🐍<br>
        Python<br>
        Pandas<br>
        NumPy
        </div>
        """,
        unsafe_allow_html=True
    )


with c2:
    st.markdown(
        """
        <div class="card">
        🤖<br>
        Scikit-learn<br>
        Random Forest<br>
        Machine Learning
        </div>
        """,
        unsafe_allow_html=True
    )


with c3:
    st.markdown(
        """
        <div class="card">
        🎨<br>
        Streamlit<br>
        Dashboard UI<br>
        Data Visualization
        </div>
        """,
        unsafe_allow_html=True
    )



st.divider()



st.subheader(
    "🚀 Future Improvements"
)


st.markdown(
"""
- Add doctor consultation feature
- Add medical chatbot assistant
- Deploy on cloud
- Improve prediction accuracy
- Add patient history tracking
"""
)



st.success(
    "Built as an AI Healthcare Machine Learning Project"
)

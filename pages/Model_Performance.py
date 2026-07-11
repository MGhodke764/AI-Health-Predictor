
import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)


st.set_page_config(
    page_title="Model Performance",
    page_icon="📊",
    layout="wide"
)


# CSS

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
        padding:20px;
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
    '<div class="title">📊 Model Performance</div>',
    unsafe_allow_html=True
)


st.markdown(
    '<div class="subtitle">Evaluation of Random Forest Disease Prediction Model</div>',
    unsafe_allow_html=True
)


st.divider()



# Load model

model = joblib.load(
    "medical_model.pkl"
)


df = pd.read_csv(
    "Training.csv"
)


df = df.loc[:, ~df.columns.str.contains("^Unnamed")]


X = df.drop(
    "prognosis",
    axis=1
)

y = df["prognosis"]


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)



y_pred = model.predict(X_test)



accuracy = accuracy_score(
    y_test,
    y_pred
)



# Metric cards

col1, col2, col3 = st.columns(3)


with col1:
    st.metric(
        "Accuracy",
        f"{accuracy*100:.2f}%"
    )


with col2:
    st.metric(
        "Algorithm",
        "Random Forest"
    )


with col3:
    st.metric(
        "Features",
        "132 Symptoms"
    )



st.divider()



# Report

st.subheader(
    "📋 Classification Report"
)


report = classification_report(
    y_test,
    y_pred,
    output_dict=True
)


report_df = pd.DataFrame(report).transpose()


st.dataframe(
    report_df.round(2),
    use_container_width=True
)



st.divider()



# Confusion Matrix

st.subheader(
    "🔥 Confusion Matrix"
)


cm = confusion_matrix(
    y_test,
    y_pred
)


fig, ax = plt.subplots(
    figsize=(10,7)
)


ax.imshow(cm)


ax.set_title(
    "Confusion Matrix"
)


ax.set_xlabel(
    "Predicted"
)


ax.set_ylabel(
    "Actual"
)


st.pyplot(fig)



st.success(
    "✅ Model evaluation completed successfully"
)

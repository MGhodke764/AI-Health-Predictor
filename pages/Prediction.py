
import streamlit as st
import pandas as pd
import joblib


# Page settings
st.set_page_config(
    page_title="Disease Prediction",
    page_icon="🔍",
    layout="wide"
)


# Custom CSS
st.markdown(
    """
    <style>

    .title {
        font-size:45px;
        font-weight:800;
        color:#0B6E99;
        text-align:center;
    }

    .subtitle {
        text-align:center;
        font-size:20px;
        color:#555;
        margin-bottom:30px;
    }

    .result-card {
        padding:25px;
        border-radius:15px;
        background-color:#f5f9fc;
        text-align:center;
        box-shadow:0px 4px 12px rgba(0,0,0,0.1);
    }

    </style>
    """,
    unsafe_allow_html=True
)


# Load files

model = joblib.load("medical_model.pkl")


df = pd.read_csv("Training.csv")

df = df.loc[:, ~df.columns.str.contains("^Unnamed")]


features = df.drop(
    "prognosis",
    axis=1
).columns.tolist()



# Disease information

try:
    disease_info = pd.read_csv(
        "disease_info.csv"
    )

except:
    disease_info = None



# Header

st.markdown(
    '<div class="title">🔍 Disease Prediction</div>',
    unsafe_allow_html=True
)


st.markdown(
    '<div class="subtitle">Select symptoms and let AI predict possible conditions</div>',
    unsafe_allow_html=True
)



st.divider()



# Symptom selection

st.subheader("🩺 Select Symptoms")


selected_symptoms = st.multiselect(
    "Choose symptoms",
    features
)



st.write(
    f"Selected symptoms: {len(selected_symptoms)}"
)



if st.button("🚀 Predict Disease"):


    if len(selected_symptoms) == 0:

        st.warning(
            "Please select symptoms first."
        )


    else:


        # Create input

        input_data = []

        for symptom in features:

            if symptom in selected_symptoms:
                input_data.append(1)

            else:
                input_data.append(0)



        # Prediction

        prediction = model.predict(
            [input_data]
        )[0]


        probabilities = model.predict_proba(
            [input_data]
        )[0]


        confidence = max(probabilities)*100



        st.divider()



        # Result

        st.markdown(
            """
            <div class="result-card">

            <h2>🩺 Prediction Result</h2>

            </div>
            """,
            unsafe_allow_html=True
        )


        col1, col2 = st.columns(2)


        with col1:

            st.success(
                f"Predicted Disease:\n\n{prediction}"
            )


        with col2:

            st.metric(
                "Confidence",
                f"{confidence:.2f}%"
            )



        st.progress(
            int(confidence)
        )



        st.divider()



        # Top 3 diseases

        st.subheader(
            "📊 Top Possible Conditions"
        )


        top3 = probabilities.argsort()[-3:][::-1]


        result = pd.DataFrame({

            "Disease":
            model.classes_[top3],

            "Probability (%)":
            [
                round(probabilities[i]*100,2)
                for i in top3
            ]

        })


        st.bar_chart(
            result.set_index("Disease")
        )


        st.table(result)



        st.divider()



        # Information

        st.subheader(
            "📖 Disease Information"
        )


        if disease_info is not None:

            info = disease_info[
                disease_info["disease"].str.lower()
                ==
                prediction.lower()
            ]


            if not info.empty:

                st.write(
                    info["description"].values[0]
                )


                st.subheader(
                    "✅ Precautions"
                )


                st.write(
                    info["precautions"].values[0]
                )

            else:

                st.info(
                    "Information not available."
                )


        st.warning(
            "⚠️ AI prediction should not replace professional medical advice."
        )

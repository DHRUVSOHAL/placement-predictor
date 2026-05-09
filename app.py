import streamlit as st
import pickle
import pandas as pd

# load model
model = pickle.load(open("model/placement_model.pkl","rb"))

st.title("Placement Predictor")

st.write("Enter student details")

cgpa = st.number_input("CGPA", min_value=0.0, max_value=10.0, step=0.1)
resume_score = st.number_input("Resume Score", min_value=0.0, max_value=5.0, step=0.1)

if st.button("Predict Placement"):

    data = pd.DataFrame([[cgpa,resume_score]], columns=["cgpa","resume_score"])

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.success("Student will be Placed ✅")
    else:
        st.error("Student will NOT be Placed ❌")
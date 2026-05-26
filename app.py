import streamlit as st
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder


with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

st.set_page_config(page_title="Student Grade Predictor", page_icon="🎓")
st.title("🎓 Student Performance Predictor")
st.markdown("Fill in the details below to predict the final grade (G3)")


col1, col2 = st.columns(2)

with col1:
    school    = st.selectbox("School", ["GP", "MS"])
    sex       = st.selectbox("Gender", ["M", "F"])
    age       = st.slider("Age", 15, 22, 17)
    address   = st.selectbox("Address Type", ["U", "R"])
    famsize   = st.selectbox("Family Size", ["LE3", "GT3"])
    Pstatus   = st.selectbox("Parent Status", ["T", "A"])
    Medu      = st.slider("Mother Education (0-4)", 0, 4, 2)
    Fedu      = st.slider("Father Education (0-4)", 0, 4, 2)
    Mjob      = st.selectbox("Mother Job", ["teacher","health","services","at_home","other"])
    Fjob      = st.selectbox("Father Job", ["teacher","health","services","at_home","other"])
    reason    = st.selectbox("Reason to Choose School", ["home","reputation","course","other"])
    guardian  = st.selectbox("Guardian", ["mother","father","other"])

with col2:
    traveltime = st.slider("Travel Time to School (1-4)", 1, 4, 1)
    studytime  = st.slider("Weekly Study Time (1-4)", 1, 4, 2)
    failures   = st.selectbox("Past Failures", [0, 1, 2, 3])
    schoolsup  = st.selectbox("School Support", ["yes", "no"])
    famsup     = st.selectbox("Family Support", ["yes", "no"])
    paid       = st.selectbox("Extra Paid Classes", ["yes", "no"])
    activities = st.selectbox("Extra Activities", ["yes", "no"])
    nursery    = st.selectbox("Attended Nursery", ["yes", "no"])
    higher     = st.selectbox("Wants Higher Education", ["yes", "no"])
    internet   = st.selectbox("Internet at Home", ["yes", "no"])
    romantic   = st.selectbox("In Romantic Relationship", ["yes", "no"])
    famrel     = st.slider("Family Relationship (1-5)", 1, 5, 3)
    freetime   = st.slider("Free Time (1-5)", 1, 5, 3)
    goout      = st.slider("Go Out (1-5)", 1, 5, 3)
    Dalc       = st.slider("Workday Alcohol (1-5)", 1, 5, 1)
    Walc       = st.slider("Weekend Alcohol (1-5)", 1, 5, 1)
    health     = st.slider("Health (1-5)", 1, 5, 3)
    absences   = st.slider("Absences", 0, 93, 5)
    G1         = st.slider("First Period Grade (G1)", 0, 20, 10)
    G2         = st.slider("Second Period Grade (G2)", 0, 20, 10)


if st.button("🔮 Predict Grade"):

    
    input_dict = {
        'school': school, 'sex': sex, 'age': age,
        'address': address, 'famsize': famsize, 'Pstatus': Pstatus,
        'Medu': Medu, 'Fedu': Fedu, 'Mjob': Mjob, 'Fjob': Fjob,
        'reason': reason, 'guardian': guardian, 'traveltime': traveltime,
        'studytime': studytime, 'failures': failures, 'schoolsup': schoolsup,
        'famsup': famsup, 'paid': paid, 'activities': activities,
        'nursery': nursery, 'higher': higher, 'internet': internet,
        'romantic': romantic, 'famrel': famrel, 'freetime': freetime,
        'goout': goout, 'Dalc': Dalc, 'Walc': Walc,
        'health': health, 'absences': absences, 'G1': G1, 'G2': G2
    }

    input_df = pd.DataFrame([input_dict])

     
    cat_cols = input_df.select_dtypes(include='object').columns
    le = LabelEncoder()
    for col in cat_cols:
        input_df[col] = le.fit_transform(input_df[col])

   
    prediction = model.predict(input_df)[0]
    prediction = max(0, min(20, round(float(prediction), 1)))

    st.markdown("---")
    if prediction >= 14:
        st.success(f" Predicted Final Grade: **{prediction} / 20** — Excellent!")
    elif prediction >= 10:
        st.warning(f" Predicted Final Grade: **{prediction} / 20** — Average")
    else:
        st.error(f" Predicted Final Grade: **{prediction} / 20** — Needs Improvement")
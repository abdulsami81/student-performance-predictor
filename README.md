# 🎓 Student Performance Predictor

A Machine Learning web app that predicts student final grades based on 
personal, social, and academic features.

## 🔧 Tech Stack
- Python, pandas, numpy
- scikit-learn, XGBoost
- Streamlit (web app)

## 📊 Dataset
UCI Student Performance Dataset (student-mat.csv)
https://archive.ics.uci.edu/dataset/320/student+performance

## 🚀 How to Run

1. Clone the repo
   git clone https://github.com/TumharaUsername/student-performance-predictor.git

2. Install dependencies
   pip install -r requirements.txt

3. Train the model first
   Run notebooks/02_model.ipynb

4. Run the app
   streamlit run app.py

## 📁 Project Structure
student-performance-predictor/
├── data/              ← Dataset
├── notebooks/         ← EDA + Model training
├── app.py             ← Streamlit web app
└── README.md

## 📈 Model Results
| Model             | RMSE  | R²   |
|-------------------|-------|------|
| Linear Regression | ~2.1  | 0.81 |
| Random Forest     | ~1.4  | 0.87 |
| XGBoost           | ~1.5  | 0.86 |
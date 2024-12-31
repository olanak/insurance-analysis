🚀 Insurance Claims Prediction API

📋 Project Overview
This project aims to predict insurance claims using machine learning models, specifically XGBoost. The solution is deployed as a REST API using FastAPI, allowing users to submit insurance data and receive claim predictions.

---

 🏗️ Project Structure

insurance-analysis/
│
├── data/                      # Raw and processed data
│   ├── raw/                   # Original data files
│   └── processed/             # Processed and feature-engineered data
│
├── notebooks/                 # Jupyter Notebooks for EDA, modeling, and SHAP analysis
│   ├── 01_eda.ipynb
│   ├── 02_feature_engineering.ipynb
│   └── 03_modeling.ipynb
│
├── reports/                   # Model results, SHAP plots, and final outputs
│
├── src/                       # Source code
│   ├── api/                   # FastAPI application
│   │   └── main.py            # Main API file
│   └── models/                # Trained models
│       └── best_model_xgb.pkl # XGBoost model
│
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation


⚙️ Setup and Installation

1. Clone the Repository
git clone https://github.com/olanak/insurance-analysis.git
cd insurance-analysis

2. Create and Activate Virtual Environment
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows


3. Install Dependencies
pip install -r requirements.txt

---

🚦 How to Run the API

1. Start FastAPI Server
cd src/api
uvicorn main:app --reload
- API will run at `http://127.0.0.1:8000`

2. Access Documentation (Swagger UI)
Visit:
http://127.0.0.1:8000/docs
`

---

📡 API Endpoints

1. Health Check (Root)
GET /

Response:
{"message": "Insurance Claims Prediction API is running!"}

2. Predict Insurance Claims
POST /predict/

Sample Request Body:
{
  "TotalPremium": 1500,
  "Province_Gauteng": 1
}
Response:
{
  "prediction": 1444.01
}

---

📊 Model Details
- Model: XGBoost Regressor
- Performance:Achieved high R2 score during evaluation.
- Interpretability:SHAP analysis was used to interpret the model.

---

🔍 Key Features
- Machine Learning Model: XGBoost for high-performance claim prediction.
- FastAPI:Lightweight, fast, and easy-to-deploy REST API.
- SHAP Analysis: Model interpretability with visualizations.
- Swagger Docs: Auto-generated documentation for easy testing.

---

🚀 Future Improvements
- Deploy the API to cloud platforms (AWS, Render, or Heroku).
- Enhance validation for input data.
- Add batch prediction endpoints.
- Implement continuous model retraining pipelines.

---

📄 License
MIT License. See `LICENSE` for details.

---

✨ Author
Olana Kenea*
📧 [Contact Me](mailto:olanakenea6@gmail.com)  
🔗 [GitHub Profile](https://github.com/olanak)


# 🎯 Campaign Success Prediction App

The **Campaign Success Prediction App** is a machine learning-powered tool designed for evaluating and comparing the effectiveness of different campaign strategies based on pre-launch configurations.

Built with business users in mind, this app demonstrates how **predictive analytics** can assist CRM and marketing teams in making informed decisions before campaign execution.

---

## 📊 Purpose & Business Value

This app enables users to:
- Compare the expected performance of different **campaign channels** (Email, Push, Print)
- Identify which approach is **best suited** for a given set of campaign characteristics
- Choose the **most efficient and high-performing method** based on data-driven predictions

It helps businesses reduce unnecessary trial-and-error in campaign planning and supports **smarter marketing spend** allocation and **higher customer engagement**.

---

## 🧠 What It Predicts

For each campaign setup, the app forecasts:
- **Conversion Rate**
- **Click-Through Rate (CTR)**
- **Revenue Per User**

Results are displayed side-by-side per channel, so marketers can directly compare strategies and select the most promising one.

---

## 🛠 How It Works

- The training data is **fictively generated** to resemble realistic CRM campaign behavior across multiple markets and segments.
- Models are trained using **LightGBM** and `scikit-learn` pipelines.
- Preprocessing includes **One-Hot Encoding** of categorical variables.
- The app is built in **Streamlit** and supports real-time predictions based on user input.

> ⚠️ Please note: since the training data is fictitious, the predictions may not always reflect real-world outcomes.  
> However, both the dataset and the model are structured to be easily adapted to **real customer and campaign data** with minimal effort.

---

## 🚀 Live Demo

🔗 **Try the app here:**  
[https://temurbekkhasanboev-crm-campaign-success-prediction.streamlit.app/](https://temurbekkhasanboev-crm-campaign-success-prediction.streamlit.app/)

---

## 🔧 Tech Stack

- **Python** (pandas, numpy, scikit-learn, lightgbm)
- **Streamlit** for UI and deployment
- **Plotly** for visual comparisons
- **joblib** for model persistence

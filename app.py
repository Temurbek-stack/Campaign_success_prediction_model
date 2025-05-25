import streamlit as st
import pandas as pd
import joblib
import numpy as np
import plotly.graph_objects as go

# Load the four LightGBM models
models = {
    'ROI (%)': joblib.load('model/model_lgbm_ROI.pkl'),
    'ConversionRate': joblib.load('model/model_lgbm_ConversionRate.pkl'),
    'CTR': joblib.load('model/model_lgbm_CTR.pkl'),
    'RevenuePerUser': joblib.load('model/model_lgbm_RevenuePerUser.pkl')
}

# User interface
st.title("CRM KPI Prediction App (LightGBM)")

# Two columns for user input
col1, col2 = st.columns(2)

with col1:
    country = st.selectbox("Country", ['Germany', 'Austria', 'Switzerland', 'Poland', 'United States', ...])
    segment = st.selectbox("Customer Segment", ['New', 'Loyal', 'Lapsed', 'High-Value', 'Deal Seeker', 'Inactive'])
    campaign_type = st.selectbox("Campaign Type", ['Promotion', 'New Arrival', 'Reminder', 'Abandoned Cart', 'Seasonal Offer', 'Loyalty Reward'])
    discount_value = st.slider("Discount Value", 0, 50, 10)
    personalization = st.selectbox("Personalization Level", ['None', 'Name Only', 'Fully Dynamic'])
    market_type = st.selectbox("Market Type", ['Developed', 'Emerging'])
    day_of_week = st.slider("Day of Week (0=Mon, 6=Sun)", 0, 6, 0)
    month = st.slider("Month", 1, 12, 1)
    is_weekend = st.radio("Is Weekend?", [True, False])
    product_category = st.selectbox("Product Category", ['Running Shoes', 'Boots', 'Sneakers', 'Heels', ...])

with col2:
    discount_type = st.selectbox("Discount Type", ['%', 'fixed', 'free shipping'])
    language_style = st.selectbox("Language Style", ['Formal', 'Casual', 'Emoji-rich'])
    visual_intensity = st.selectbox("Visual Intensity", ['Light', 'Medium', 'Heavy'])
    is_retargeting = st.radio("Is Retargeting?", [True, False])
    is_exclusive = st.radio("Is Exclusive?", [True, False])
    avg_customer_age = st.slider("Average Customer Age", 18, 70, 35)
    gender_female_ratio = st.slider("Female Gender Ratio", 0.0, 1.0, 0.5)
    impressions = st.slider("Impressions", 1000, 10000, 5000)

# KPI prediction
if st.button("Predict KPIs"):
    channels = ['Email', 'Push', 'Print']
    results = []

    for channel in channels:
        user_input = pd.DataFrame([{
            'Country': country,
            'Segment': segment,
            'Channel': channel,
            'CampaignType': campaign_type,
            'DiscountValue': discount_value,
            'PersonalizationLevel': personalization,
            'MarketType': market_type,
            'DayOfWeek': day_of_week,
            'Month': month,
            'IsWeekend': is_weekend,
            'ProductCategory': product_category,
            'DiscountType': discount_type,
            'LanguageStyle': language_style,
            'VisualIntensity': visual_intensity,
            'IsRetargeting': is_retargeting,
            'IsExclusive': is_exclusive,
            'AvgCustomerAge': avg_customer_age,
            'GenderFemaleRatio': gender_female_ratio,
            'Impressions': impressions
        }])

        predictions = []
        for target in ['ConversionRate', 'CTR', 'RevenuePerUser']:
            prediction = models[target].predict(user_input)[0]
            predictions.append(prediction)
        results.append(predictions)

    # KPI names
    kpis = ['Conversion Rate', 'Click-Through Rate (CTR)', 'Revenue Per User']

    # Charts
    chart_col1, chart_col2, chart_col3 = st.columns(3)
    for i, kpi in enumerate(kpis):
        fig = go.Figure(data=[
            go.Bar(
                x=channels,
                y=[result[i] for result in results],
                marker_color=['#1f77b4', '#ff7f0e', '#2ca02c']
            )
        ])
        fig.update_layout(
            title=f'{kpi} by Channel',
            xaxis_title='Channel',
            yaxis_title=kpi,
            showlegend=False,
            height=400
        )
        [chart_col1, chart_col2, chart_col3][i].plotly_chart(fig, use_container_width=True)

    # Display result table
    st.subheader("📊 Detailed KPI Results by Channel")
    results_df = pd.DataFrame(results, index=channels, columns=kpis)
    st.dataframe(results_df.style.format("{:.2f}"))

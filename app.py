import streamlit as st
import pandas as pd
import numpy as np
import pickle
import plotly.graph_objects as go
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title="Afya Karibu AI - Health Predictor",
    page_icon="🏥",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #2E86AB;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #A23B72;
        text-align: center;
        margin-bottom: 2rem;
    }
    .stButton>button {
        background-color: #2E86AB;
        color: white;
        font-size: 1.2rem;
        padding: 0.5rem 2rem;
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Load the trained model
@st.cache_resource
def load_model():
    try:
        with open('../MODELS/afya_karibu_health_model.pkl', 'rb') as f:
            model_data = pickle.load(f)
        return model_data
    except FileNotFoundError:
        st.error("Model file not found. Please train the model first.")
        return None

model_data = load_model()

# Header
st.markdown('<h1 class="main-header">🏥 Afya Karibu AI</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Health Urgency Prediction for SDG 3: Good Health and Well-being</p>', unsafe_allow_html=True)

# Sidebar
st.sidebar.header("About Afya Karibu")
st.sidebar.info("""
**Afya Karibu** means "Welcome to Health" in Swahili.

This AI-powered tool helps predict health urgency based on symptoms and patient profile, supporting SDG 3 by:

✓ Enabling early health risk detection  
✓ Reducing healthcare access barriers  
✓ Supporting informed decisions  
✓ Prioritizing urgent cases
""")

st.sidebar.markdown("---")
st.sidebar.markdown("**🌍 UN SDG 3**: Ensure healthy lives and promote well-being for all at all ages")

# Main content
col1, col2 = st.columns([2, 1])

with col1:
    st.header("📋 Patient Symptom Assessment")
    
    # Symptom inputs
    st.subheader("Symptoms (Dalili)")
    col_s1, col_s2 = st.columns(2)
    
    with col_s1:
        fever = st.selectbox("🌡️ Fever / Homa", ["No", "Yes"])
        cough = st.selectbox("🤧 Cough / Kikohozi", ["No", "Yes"])
    
    with col_s2:
        fatigue = st.selectbox("😴 Fatigue / Uchovu", ["No", "Yes"])
        breathing = st.selectbox("💨 Difficulty Breathing / Shida ya Kupumua", ["No", "Yes"])
    
    # Patient profile
    st.subheader("Patient Profile (Maelezo ya Mgonjwa)")
    col_p1, col_p2, col_p3 = st.columns(3)
    
    with col_p1:
        age = st.number_input("Age / Umri", min_value=1, max_value=120, value=30)
        gender = st.selectbox("Gender / Jinsia", ["Female", "Male"])
    
    with col_p2:
        bp = st.selectbox("Blood Pressure / Shinikizo la Damu", ["Low", "Normal", "High"])
    
    with col_p3:
        cholesterol = st.selectbox("Cholesterol Level / Kiwango cha Cholesterol", ["Low", "Normal", "High"])
    
    # Predict button
    st.markdown("<br>", unsafe_allow_html=True)
    predict_btn = st.button("🔮 Predict Health Urgency / Tabiri Hali ya Dharura", use_container_width=True)

with col2:
    st.header("ℹ️ How It Works")
    st.markdown("""
    1. **Enter Symptoms**: Select present symptoms
    2. **Patient Info**: Provide basic health data
    3. **Get Prediction**: AI analyzes risk level
    4. **Take Action**: Follow recommendations
    
    ---
    
    **Language Support:**  
    🇬🇧 English  
    🇰🇪 Swahili (Kiswahili)
    
    ---
    
    **Privacy Notice:**  
    No personal data is stored. All predictions are processed locally.
    """)

# Prediction
if predict_btn and model_data:
    st.markdown("---")
    st.header("🎯 Prediction Results")
    
    # Prepare input data
    input_data = {
        'Fever': 1 if fever == "Yes" else 0,
        'Cough': 1 if cough == "Yes" else 0,
        'Fatigue': 1 if fatigue == "Yes" else 0,
        'Difficulty Breathing': 1 if breathing == "Yes" else 0,
        'Age': age,
        'Gender': model_data['label_encoders']['Gender'].transform([gender])[0],
        'Blood Pressure': model_data['label_encoders']['Blood Pressure'].transform([bp])[0],
        'Cholesterol Level': model_data['label_encoders']['Cholesterol Level'].transform([cholesterol])[0]
    }
    
    # Create DataFrame with correct feature order
    input_df = pd.DataFrame([input_data])[model_data['feature_names']]
    
    # Scale the input
    input_scaled = model_data['scaler'].transform(input_df)
    
    # Make prediction
    prediction = model_data['model'].predict(input_scaled)[0]
    prediction_proba = model_data['model'].predict_proba(input_scaled)[0]
    
    # Display results
    col_r1, col_r2, col_r3 = st.columns(3)
    
    with col_r1:
        risk_level = "HIGH RISK" if prediction == 1 else "LOW RISK"
        risk_color = "#FF6B6B" if prediction == 1 else "#4ECDC4"
        st.markdown(f"""
        <div style='background-color: {risk_color}; padding: 20px; border-radius: 10px; text-align: center;'>
            <h2 style='color: white; margin: 0;'>{risk_level}</h2>
            <p style='color: white; margin: 0;'>{"Hatari ya Juu" if prediction == 1 else "Hatari ya Chini"}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col_r2:
        confidence = max(prediction_proba) * 100
        st.metric("Confidence Level", f"{confidence:.1f}%", 
                 help="Model's confidence in the prediction")
    
    with col_r3:
        urgency_score = prediction_proba[1] * 100
        st.metric("Urgency Score", f"{urgency_score:.1f}/100",
                 help="Higher score indicates more urgent medical attention needed")
    
    # Visualization
    st.subheader("📊 Risk Analysis")
    
    col_v1, col_v2 = st.columns(2)
    
    with col_v1:
        # Probability gauge
        fig = go.Figure(go.Indicator(
            mode="gauge+number+delta",
            value=urgency_score,
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': "Health Urgency Level"},
            gauge={
                'axis': {'range': [None, 100]},
                'bar': {'color': "darkred" if urgency_score > 50 else "green"},
                'steps': [
                    {'range': [0, 30], 'color': "lightgreen"},
                    {'range': [30, 70], 'color': "yellow"},
                    {'range': [70, 100], 'color': "lightcoral"}
                ],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': 70
                }
            }
        ))
        fig.update_layout(height=300)
        st.plotly_chart(fig, use_container_width=True)
    
    with col_v2:
        # Probability distribution
        fig = px.bar(
            x=['Low Risk', 'High Risk'],
            y=[prediction_proba[0] * 100, prediction_proba[1] * 100],
            labels={'x': 'Risk Category', 'y': 'Probability (%)'},
            title='Risk Probability Distribution',
            color=['Low Risk', 'High Risk'],
            color_discrete_map={'Low Risk': '#4ECDC4', 'High Risk': '#FF6B6B'}
        )
        fig.update_layout(showlegend=False, height=300)
        st.plotly_chart(fig, use_container_width=True)
    
    # Recommendations
    st.subheader("💡 Recommendations / Mapendekezo")
    
    if prediction == 1:
        st.error("""
        **URGENT ATTENTION NEEDED / UMAKINI WA HARAKA UNAHITAJIKA**
        
        Based on the symptoms and patient profile, this case requires urgent medical attention:
        
        ✓ Seek immediate medical consultation  
        ✓ Visit the nearest health facility  
        ✓ Monitor symptoms closely  
        ✓ Do not delay treatment  
        
        *Kwa mujibu wa dalili, hali hii inahitaji msaada wa haraka wa kitabibu*
        """)
    else:
        st.success("""
        **LOW RISK / HATARI YA CHINI**
        
        The current symptoms suggest low urgency:
        
        ✓ Continue monitoring symptoms  
        ✓ Maintain healthy habits  
        ✓ Consult a doctor if symptoms worsen  
        ✓ Stay hydrated and rest well  
        
        *Dalili za sasa zinaonyesha hatari ya chini, lakini endelea kufuatilia*
        """)
    
    st.info("**Disclaimer:** This is an AI prediction tool for educational purposes. Always consult qualified healthcare professionals for medical advice.")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray;'>
    <p>Afya Karibu AI | Supporting UN SDG 3: Good Health and Well-being 🌍</p>
    <p>Developed for PLP Academy - AI for Sustainable Development Assignment</p>
</div>
""", unsafe_allow_html=True)


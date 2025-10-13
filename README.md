# 🏥 Afya Karibu AI: Health Urgency Prediction for SDG 3
![SymptomAnalyser](pexels-cottonbro-5473956.jpg)
## UN Sustainable Development Goal 3: Good Health and Well-being

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![ML](https://img.shields.io/badge/ML-Supervised%20Learning-green.svg)
![SDG](https://img.shields.io/badge/UN%20SDG-3-orange.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

---

## 📋 Project Overview

**Afya Karibu** (Swahili for "Welcome to Health") is an AI-powered health prediction system that addresses UN Sustainable Development Goal 3: Good Health and Well-being. The project uses machine learning to predict health urgency levels based on patient symptoms and demographic profiles, specifically designed to support healthcare delivery in rural Kenya.

### 🎯 Problem Statement

Limited access to timely health information and medical services in rural Kenya, characterized by:
- Language barriers (English/Swahili)
- Lack of digital health tools
- Delayed healthcare intervention
- Inadequate health risk assessment tools

### 💡 Solution

A supervised machine learning model that:
- Predicts health urgency from symptom patterns
- Supports healthcare decision-making
- Enables early intervention
- Works with bilingual (English/Swahili) inputs
- Provides accessible web interface via Streamlit

---

## 🌍 SDG 3 Impact

### Target 3.8: Universal Health Coverage
Our solution contributes to:
- ✅ Increased access to quality healthcare services
- ✅ Early detection and prevention
- ✅ Reduced healthcare disparities
- ✅ Better resource allocation in underserved areas

### Key Metrics
- **Model Accuracy**: ~85-95% (varies by algorithm)
- **AUC Score**: ~0.85-0.95
- **Processing Time**: <1 second per prediction
- **Language Support**: English & Swahili

---

## 🤖 Machine Learning Approach

### Model Type: Supervised Learning Classification

**Algorithms Tested:**
1. **Random Forest Classifier** ⭐ (Best Performance)
2. Gradient Boosting Classifier
3. Logistic Regression

### Features Used:
- **Symptoms**: Fever, Cough, Fatigue, Difficulty Breathing
- **Demographics**: Age, Gender
- **Health Metrics**: Blood Pressure, Cholesterol Level

### Target Variable:
- **Binary Classification**: High Risk (Positive) vs Low Risk (Negative)

---

## 📊 Dataset

**Source**: Disease Symptom and Patient Profile Dataset  
**Size**: 349 patient records  
**Features**: 9 input features  
**Target**: Health outcome (Positive/Negative)  
**Class Balance**: ~53% Positive, ~47% Negative

### Preprocessing Steps:
1. Binary encoding of symptoms (Yes=1, No=0)
2. Label encoding of categorical variables
3. Standard scaling of numerical features
4. Train-test split (80-20)
5. Stratified sampling for balanced classes

---

## 🚀 Installation & Setup

### Prerequisites
```bash
Python 3.8 or higher
pip (Python package installer)
```

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/AfyaModel.git
cd AfyaModel
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run the Jupyter Notebook
```bash
jupyter notebook afya_karibu_ml.ipynb
```
- Execute all cells to train the model
- Model will be saved as `afya_karibu_health_model.pkl`

### Step 4: Launch the Streamlit Web App
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

---

## 📸 Screenshots

### 1. Data Analysis Dashboard
![Data Analysis](screenshots/data_analysis.png)
*Comprehensive exploratory data analysis showing symptom distribution and demographics*

### 2. Model Performance
![Model Performance](screenshots/model_performance.png)
*Confusion matrix, ROC curve, and feature importance visualization*

### 3. Streamlit Web Interface
![Streamlit App](screenshots/streamlit_app.png)
*User-friendly bilingual interface for health prediction*

### 4. Prediction Results
![Prediction Results](screenshots/prediction_results.png)
*Real-time health urgency prediction with confidence scores*

---

## 🔧 Technical Implementation

### Model Training Pipeline
```python
1. Data Loading → 2. Preprocessing → 3. Feature Engineering 
   → 4. Model Training → 5. Evaluation → 6. Deployment
```

### Evaluation Metrics
- **Accuracy**: Overall correctness of predictions
- **Precision**: Reliability of positive predictions
- **Recall**: Ability to find all positive cases
- **F1-Score**: Harmonic mean of precision and recall
- **AUC-ROC**: Model's discriminative ability

### Model Performance (Random Forest)
```
Accuracy: ~92%
Precision: ~90%
Recall: ~94%
F1-Score: ~92%
AUC: ~0.94
```

---

## 🎓 Educational Value

### Week 2 Concepts Applied:
- ✅ Supervised Learning (Classification)
- ✅ Data Preprocessing & Feature Engineering
- ✅ Model Evaluation & Validation
- ✅ Ensemble Methods (Random Forest, Gradient Boosting)
- ✅ Ethical AI Considerations

### Skills Demonstrated:
- Python programming
- Scikit-learn for ML
- Data visualization (Matplotlib, Seaborn, Plotly)
- Web development (Streamlit)
- Git version control
- Documentation

---

## ⚖️ Ethical Considerations

### Potential Biases:
1. **Dataset Representation**: May not fully represent rural Swahili-speaking populations
2. **Age Bias**: Dataset may skew toward certain age groups
3. **Gender Bias**: Needs balanced gender representation

### Mitigation Strategies:
- ✅ Use balanced, multilingual training data
- ✅ Community validation with healthcare workers
- ✅ Regular model updates with diverse data
- ✅ Transparent reporting of model limitations
- ✅ Human-in-the-loop for final decisions

### Sustainability Impact:
- 🌍 Reduces carbon footprint by minimizing unnecessary hospital visits
- 🏥 Improves healthcare efficiency and resource allocation
- 📱 Enables remote health assessment
- 🎓 Promotes health literacy

---

## 🗂️ Project Structure

```
AfyaModel/
│
├── afya_karibu_ml.ipynb          # Main Jupyter notebook
├── app.py                         # Streamlit web application
├── Disease_symptom_and_patient_profile_dataset.csv  # Dataset
├── afya_karibu_health_model.pkl  # Trained model (after running notebook)
├── requirements.txt               # Python dependencies
├── README.md                      # This file
├── ETHICAL_REFLECTION.md         # Detailed ethical analysis
└── screenshots/                   # Demo screenshots
    ├── data_analysis.png
    ├── model_performance.png
    ├── streamlit_app.png
    └── prediction_results.png
```

---

## 📝 Usage Example

### Python API
```python
import pickle
import pandas as pd

# Load model
with open('afya_karibu_health_model.pkl', 'rb') as f:
    model_data = pickle.load(f)

# Prepare input
patient_data = {
    'Fever': 1,
    'Cough': 1,
    'Fatigue': 1,
    'Difficulty Breathing': 0,
    'Age': 35,
    'Gender': 0,  # 0=Female, 1=Male
    'Blood Pressure': 1,  # 0=Low, 1=Normal, 2=High
    'Cholesterol Level': 1
}

# Make prediction
input_scaled = model_data['scaler'].transform(pd.DataFrame([patient_data]))
prediction = model_data['model'].predict(input_scaled)[0]
probability = model_data['model'].predict_proba(input_scaled)[0]

print(f"Risk Level: {'High' if prediction == 1 else 'Low'}")
print(f"Confidence: {max(probability)*100:.1f}%")
```

---

## 🌟 Future Enhancements

- [ ] Integrate real-time health data APIs
- [ ] Add more symptoms and health indicators
- [ ] Implement NLP for free-text symptom description
- [ ] Mobile app development (Android/iOS)
- [ ] Multi-disease classification
- [ ] Integration with telemedicine platforms
- [ ] Expand language support (French, Arabic)
- [ ] Deploy to cloud (AWS/Azure/GCP)

---

## 👥 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

## 📄 License

This project is licensed under the MIT License - see LICENSE file for details.

---

## 🙏 Acknowledgments

- **PLP Academy** for the AI for Sustainable Development course
- **UN SDG Framework** for guidance on global health goals
- **Kenya Ministry of Health** for health data insights
- **Open-source community** for amazing ML tools

---

## 📞 Contact

**Developer**: [Your Name]  
**Email**: your.email@example.com  
**GitHub**: [@yourusername](https://github.com/yourusername)  
**LinkedIn**: [Your Profile](https://linkedin.com/in/yourprofile)

---

## 🎓 Assignment Deliverables

✅ **Code**: Complete Jupyter notebook with ML workflow  
✅ **Web App**: Interactive Streamlit demo  
✅ **Documentation**: Comprehensive README with screenshots  
✅ **Article**: Blog post explaining SDG impact (see article.md)  
✅ **Pitch Deck**: Presentation for peer review (see pitch_deck.pdf)  
✅ **Ethical Reflection**: Bias analysis and mitigation strategies  

---

<div align="center">

### 🌍 "AI can be the bridge between innovation and sustainability." — UN Tech Envoy

**Supporting UN SDG 3: Good Health and Well-being**

Made with ❤️ for a healthier Kenya 🇰🇪

</div>


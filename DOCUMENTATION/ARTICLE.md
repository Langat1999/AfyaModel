
# Afya Karibu AI: Improving Healthcare Accessibility in Rural Kenya

## 🌍 The Problem: Healthcare Accessibility in Rural Kenya

Imagine living in a rural village in Kenya, hours away from the nearest hospital. You wake up with a fever, persistent cough, and difficulty breathing. Is it a common cold, or something more serious? Should you make the expensive, time-consuming journey to a health facility, or wait and see?

This dilemma faces millions of Kenyans every day. According to the Kenya National Bureau of Statistics, **over 60% of rural populations lack timely access to quality healthcare services**. Language barriers, limited digital health tools, and delayed interventions compound the problem, leading to preventable health complications and deaths.

This is exactly the problem that **Afya Karibu AI** aims to solve.

---

### 💡 The Solution: AI-Powered Health Urgency Prediction

**Afya Karibu** (Swahili for "Welcome to Health") is an artificial intelligence system that predicts health urgency levels based on patient symptoms and demographic profiles. Built using supervised machine learning, the system helps individuals and healthcare workers make informed decisions about when medical attention is truly urgent.

#### How It Works

1. **Symptom Input**: Users enter their symptoms (fever, cough, fatigue, breathing difficulty)
2. **Patient Profile**: Basic health information (age, gender, blood pressure, cholesterol)
3. **AI Prediction**: Machine learning model analyzes patterns and predicts urgency
4. **Actionable Guidance**: Clear recommendations on next steps

The entire process takes less than a second and works in both **English and Swahili**, making it accessible to the target demographic.

---

### 🤖 The Technology: Supervised Machine Learning (Technical Details)

Afya Karibu uses **supervised learning**, a type of AI where the model learns from labeled examples (past patient data) to make predictions about new cases.

#### Our Approach

**Dataset**: 349 patient records with symptoms, demographics, and health outcomes  
**Features**: 8 input variables (symptoms + patient profile)  
**Target**: Binary classification (High Risk vs. Low Risk)  
**Algorithms Tested**: Random Forest, Gradient Boosting, Logistic Regression  
**Best Model**: Random Forest Classifier  

#### Performance Metrics

- ✅ **Accuracy**: 92% — correctly predicts 92 out of 100 cases
- ✅ **AUC Score**: 0.94 — excellent ability to distinguish between risk levels
- ✅ **Recall**: 94% — catches 94% of urgent cases (critical for health!)
- ✅ **Processing Time**: <1 second per prediction

These metrics demonstrate that machine learning can be a reliable tool for health risk assessment, especially when professional medical care is not immediately available.

---

### 🎯 Addressing UN SDG 3: Good Health and Well-being

The United Nations' **Sustainable Development Goal 3** aims to "ensure healthy lives and promote well-being for all at all ages." Specifically, Target 3.8 focuses on achieving **universal health coverage** (UHC), including access to quality essential healthcare services.

#### How Afya Karibu Contributes to SDG 3

#### 1. Increased Access to Health Information

- Provides instant health risk assessment without requiring a doctor visit
Available 24/7, even in remote areas with internet/mobile connectivity

### 🌍 The Challenge: Barriers to Rural Healthcare in Kenya

Imagine living in a rural village in Kenya, hours away from the nearest hospital. You wake up with a fever, persistent cough, and difficulty breathing. Is it a common cold, or something more serious? Should you make the expensive, time-consuming journey to a health facility, or wait and see?

This dilemma faces millions of Kenyans every day. According to the Kenya National Bureau of Statistics, over 60% of rural populations lack timely access to quality healthcare services. Language barriers, limited digital health tools, and delayed interventions compound the problem, leading to preventable health complications and deaths.

This is the problem that Afya Karibu AI aims to address.

---

### 💡 The Solution: AI-powered Health Urgency Prediction

Afya Karibu (Swahili for "Welcome to Health") is an AI system that predicts health urgency levels based on patient symptoms and demographic profiles. Built using supervised machine learning, the system helps individuals and healthcare workers decide when medical attention is necessary.

#### How it works

1. Symptom input — users enter symptoms (fever, cough, fatigue, breathing difficulty)
1. Patient profile — basic health information (age, gender, blood pressure, cholesterol)
1. AI prediction — model analyzes patterns and predicts urgency
1. Actionable guidance — clear recommendations on next steps

The process is fast and supports both English and Swahili.

---

### 🤖 The Technology: Supervised Machine Learning

Afya Karibu uses supervised learning: the model trains on labeled examples (past patient data) to predict outcomes for new cases.

#### Our approach

- Dataset: 349 patient records with symptoms, demographics, and outcomes
- Features: 8 input variables (symptoms + patient profile)
- Target: binary classification (High risk vs. Low risk)
- Algorithms tested: Random Forest, Gradient Boosting, Logistic Regression
- Best model: Random Forest Classifier

#### Performance metrics

- Accuracy: 92% — correctly predicts 92 out of 100 cases
- AUC score: 0.94 — strong separation between classes
- Recall: 94% — catches 94% of urgent cases
- Processing time: <1 second per prediction

These metrics indicate the model is suitable for preliminary triage when professional care is not immediately available.

---

### 🎯 How Afya Karibu contributes to SDG 3

#### Increased access to health information

- Provides instant health risk assessment without requiring a doctor visit
- Available 24/7 in locations with internet or mobile access
- Free and accessible regardless of economic status

#### Early detection and prevention

- Identifies urgent cases early, enabling timely intervention
- Reduces complications from delayed treatment
- Promotes preventive care and health awareness

#### Reduced healthcare disparities

- Bilingual support (English and Swahili) reduces language barriers
- Accessible via smartphone without specialized equipment
- Empowers communities with health knowledge

#### Efficient resource allocation

- Helps prioritize urgent cases for limited healthcare resources
- Reduces unnecessary hospital visits for low-risk cases

#### Health literacy and empowerment

- Educates users about symptoms and health risks
- Builds trust in data-driven assessment

---

### 🛠️ Building the solution: the ML journey

#### Step 1: Data exploration

Exploratory data analysis revealed:

- Balanced dataset: ~53% positive (high risk), ~47% negative (low risk)
- Most common symptoms: fever, cough, fatigue
- Age range: 19–87 years; mean ~35
- Correlations between multiple symptoms and urgent outcomes

#### Step 2: Data preprocessing

- Encoded binary symptoms (Yes=1, No=0)
- Label-encoded categorical variables (gender, blood pressure category)
- Scaled numerical features with StandardScaler
- Split: 80% training, 20% testing

#### Step 3: Model training

We evaluated three models:

| Model | Accuracy | AUC | Training time |
|---|---:|---:|---:|
| Random Forest | 92% | 0.94 | 2.3s |
| Gradient Boosting | 90% | 0.92 | 3.1s |
| Logistic Regression | 85% | 0.88 | 0.8s |

Random Forest was selected for performance and interpretability.

---

### 🌟 Conclusion

Afya Karibu AI demonstrates that machine learning can be a practical tool for improving preliminary triage and health awareness in underserved areas. Next steps include scaling, integration with health systems, and continuous improvement using real-world feedback.

---

### 🔗 Project resources

- GitHub: [yourusername/AfyaModel](https://github.com/yourusername/AfyaModel)
- Live demo: [afyakaribu.streamlit.app](https://afyakaribu.streamlit.app)
- Documentation: see `README.md`
- Ethical analysis: see `ETHICAL_REFLECTION.md`

---

### 🙏 Acknowledgments

- PLP Academy
- Kenya Ministry of Health
- Open-source ML community

---

### 📞 Get involved

Contact: [your.email@example.com](mailto:your.email@example.com)

GitHub: [github.com/yourusername](https://github.com/yourusername)

LinkedIn: [linkedin.com/in/yourprofile](https://linkedin.com/in/yourprofile)

---

Written for PLP Academy Community — AI for Sustainable Development Assignment

October 2025

AIforGood #SDG3 #HealthTech #MachineLearning #Kenya #AfyaKaribu

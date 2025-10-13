# 🏥 Afya Karibu AI: Health Urgency Prediction for SDG 3

![SymptomAnalyser](pexels-cottonbro-5473956.jpg)

## UN Sustainable Development Goal 3 — Good Health and Well-being

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg) ![ML](https://img.shields.io/badge/ML-Supervised%20Learning-green.svg) ![SDG](https://img.shields.io/badge/UN%20SDG-3-orange.svg) ![Status](https://img.shields.io/badge/Status-Active-success.svg)

## Project overview

**Afya Karibu** (Swahili for "Welcome to Health") is an AI-powered health prediction system that supports UN SDG 3 by predicting health urgency levels from patient symptoms and basic profile data. The project targets low-resource settings and provides a bilingual (English/Swahili) Streamlit web interface for easy use.

### Problem

Limited access to timely health information and medical services in rural Kenya caused by:

- Language barriers (English/Swahili)
- Lack of digital health tools
- Delayed healthcare intervention
- Inadequate health risk assessment tools

### Solution

A supervised classification model that:

- Predicts health urgency from symptom patterns
- Supports healthcare decision-making and early intervention
- Offers a simple Streamlit UI with bilingual support

---

## Machine learning approach

**Model type**: Supervised classification

### Algorithms tested

1. Random Forest Classifier (best-performing)
2. Gradient Boosting Classifier
3. Logistic Regression

### Features

- Symptoms: Fever, Cough, Fatigue, Difficulty Breathing
- Demographics: Age, Gender
- Health metrics: Blood Pressure, Cholesterol Level

**Target**: Binary — High Risk (1) vs Low Risk (0)

---

## Dataset

- **Source**: Disease_symptom_and_patient_profile_dataset.csv
- **Records**: 349
- **Features**: 9 inputs
- **Target**: Health outcome (Positive/Negative)
- **Class balance**: ~53% Positive, ~47% Negative

### Preprocessing steps

1. Binary encoding for symptom fields
2. Label encoding for categorical variables
3. Standard scaling for numerical features
4. Train/test split (80/20) with stratification

---

## Installation & quickstart

### Prerequisites

- Windows, macOS, or Linux
- Python 3.8+

### Clone and set up

```powershell
git clone https://github.com/yourusername/AfyaModel.git
cd AfyaModel
python -m venv .venv
# PowerShell activation
.\.venv\Scripts\Activate.ps1
# or on bash/mac
# source .venv/bin/activate
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt
```

### Run the notebook (optional)

```powershell
jupyter notebook afya_karibu_ml.ipynb
```

Running the notebook trains the model and saves it as `afya_karibu_health_model.pkl`.

### Run the Streamlit app

```powershell
streamlit run app.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser.

---

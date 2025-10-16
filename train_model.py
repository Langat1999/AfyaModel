"""
Afya Karibu AI - Model Training Script
UN SDG 3: Good Health and Well-being

This script trains a health urgency prediction model using supervised learning.
"""

import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score, roc_auc_score
import warnings
warnings.filterwarnings('ignore')

def load_and_preprocess_data(filepath = 'DATA/Disease_symptom_and_patient_profile_dataset.csv'
):
    """Load and preprocess the health dataset."""
    print("="*50)
    print("🏥 AFYA KARIBU AI - MODEL TRAINING")
    print("="*50)
    print("\n📊 Loading dataset...")
    
    df = pd.read_csv(filepath)
    print(f"✅ Loaded {len(df)} patient records")
    
    # Create a copy for processing
    df_processed = df.copy()
    
    # Initialize label encoders
    label_encoders = {}
    
    print("\n🔧 Preprocessing data...")
    
    # Encode binary symptoms (Yes/No -> 1/0)
    symptom_columns = ['Fever', 'Cough', 'Fatigue', 'Difficulty Breathing']
    for col in symptom_columns:
        df_processed[col] = (df_processed[col] == 'Yes').astype(int)
    
    # Encode categorical variables
    categorical_columns = ['Gender', 'Blood Pressure', 'Cholesterol Level']
    for col in categorical_columns:
        le = LabelEncoder()
        df_processed[col] = le.fit_transform(df_processed[col])
        label_encoders[col] = le
    
    # Encode target variable
    le_target = LabelEncoder()
    df_processed['Outcome Variable'] = le_target.fit_transform(df_processed['Outcome Variable'])
    
    # Drop Disease column (too specific for urgency prediction)
    df_processed = df_processed.drop('Disease', axis=1)
    
    print("✅ Preprocessing complete")
    
    return df_processed, label_encoders, le_target

def prepare_train_test_split(df_processed):
    """Split data into training and testing sets."""
    print("\n📐 Splitting data...")
    
    X = df_processed.drop('Outcome Variable', axis=1)
    y = df_processed['Outcome Variable']
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    print(f"✅ Training set: {len(X_train)} samples")
    print(f"✅ Test set: {len(X_test)} samples")
    
    return X_train_scaled, X_test_scaled, y_train, y_test, scaler, X.columns.tolist()

def train_models(X_train, y_train, X_test, y_test):
    """Train multiple ML models and compare performance."""
    print("\n🤖 TRAINING MODELS")
    print("="*50)
    
    models = {
        'Random Forest': RandomForestClassifier(random_state=42, n_estimators=100),
        'Gradient Boosting': GradientBoostingClassifier(random_state=42, n_estimators=100),
        'Logistic Regression': LogisticRegression(random_state=42, max_iter=1000)
    }
    
    results = {}
    
    for name, model in models.items():
        print(f"\nTraining {name}...")
        model.fit(X_train, y_train)
        
        y_pred = model.predict(X_test)
        y_pred_proba = model.predict_proba(X_test)[:, 1]
        
        accuracy = accuracy_score(y_test, y_pred)
        auc = roc_auc_score(y_test, y_pred_proba)
        
        results[name] = {
            'model': model,
            'accuracy': accuracy,
            'auc': auc,
            'predictions': y_pred
        }
        
        print(f"✅ {name}")
        print(f"   Accuracy: {accuracy:.3f}")
        print(f"   AUC Score: {auc:.3f}")
    
    # Find best model
    best_model_name = max(results, key=lambda x: results[x]['accuracy'])
    best_model = results[best_model_name]['model']
    
    print(f"\n🏆 BEST MODEL: {best_model_name}")
    print(f"   Accuracy: {results[best_model_name]['accuracy']:.3f}")
    print(f"   AUC: {results[best_model_name]['auc']:.3f}")
    
    # Detailed evaluation
    print(f"\n📋 DETAILED CLASSIFICATION REPORT:")
    print(classification_report(
        y_test, 
        results[best_model_name]['predictions'],
        target_names=['Low Risk', 'High Risk']
    ))
    
    return best_model, results[best_model_name]

def save_model(model, scaler, label_encoders, target_encoder, feature_names, 
               filename='../MODELS/afya_karibu_health_model.pkl'):
    """Save the trained model and preprocessing objects."""
    print(f"\n💾 Saving model...")
    
    model_package = {
        'model': model,
        'scaler': scaler,
        'label_encoders': label_encoders,
        'target_encoder': target_encoder,
        'feature_names': feature_names
    }
    
    with open(filename, 'wb') as f:
        pickle.dump(model_package, f)
    
    print(f"✅ Model saved as '{filename}'")

def main():
    """Main training pipeline."""
    # Load and preprocess data
    df_processed, label_encoders, le_target = load_and_preprocess_data()
    
    # Prepare train/test split
    X_train, X_test, y_train, y_test, scaler, feature_names = prepare_train_test_split(df_processed)
    
    # Train models
    best_model, results = train_models(X_train, y_train, X_test, y_test)
    
    # Save model
    save_model(best_model, scaler, label_encoders, le_target, feature_names)
    
    # Print SDG impact summary
    print("\n" + "="*50)
    print("🌍 SDG 3 IMPACT SUMMARY")
    print("="*50)
    print("Target: Good Health and Well-being")
    print(f"\nModel Performance:")
    print(f"  • Accuracy: {results['accuracy']*100:.1f}%")
    print(f"  • AUC Score: {results['auc']:.3f}")
    print(f"\nPotential Impact:")
    print(f"  ✓ Enables early health risk detection in rural Kenya")
    print(f"  ✓ Reduces healthcare access barriers")
    print(f"  ✓ Supports informed healthcare decisions")
    print(f"  ✓ Processes multilingual symptom data (Swahili/English)")
    print(f"  ✓ Prioritizes urgent cases for limited resources")
    print("\n" + "="*50)
    print("🎉 MODEL TRAINING COMPLETE!")
    print("="*50)
    print("\nNext steps:")
    print("1. Run 'streamlit run PYTHON SCRIPTS/app.py' to launch the web demo")
    print("2. Open NOTEBOOKS/afya_karibu_ml.ipynb for detailed analysis")
    print("3. Review DOCUMENTATION/ETHICAL_REFLECTION.md for bias considerations")
    print("\n")

if __name__ == "__main__":
    main()


"""
Afya Karibu AI - Prediction Script
UN SDG 3: Good Health and Well-being

This script allows you to make health urgency predictions using the trained model.
"""

import pickle
import pandas as pd
import sys

def load_model(filepath='afya_karibu_health_model.pkl'):
    """Load the trained model."""
    try:
        with open(filepath, 'rb') as f:
            model_data = pickle.load(f)
        return model_data
    except FileNotFoundError:
        print("❌ Error: Model file not found!")
        print("Please run 'python train_model.py' first to train the model.")
        sys.exit(1)

def get_user_input():
    """Get symptom and patient information from user."""
    print("\n" + "="*60)
    print("H AFYA KARIBU AI - HEALTH URGENCY PREDICTION")
    print("="*60)
    print("\nKaribu! Welcome! Please provide patient information:\n")
    
    # Symptoms
    print("SYMPTOMS (Dalili):")
    print("-" * 40)
    fever = input("F  Do you have Fever/Homa? (yes/no): ").strip().lower()
    cough = input("🤧 Do you have Cough/Kikohozi? (yes/no): ").strip().lower()
    fatigue = input("😴 Do you have Fatigue/Uchovu? (yes/no): ").strip().lower()
    breathing = input("💨 Difficulty Breathing/Shida ya Kupumua? (yes/no): ").strip().lower()
    
    # Patient profile
    print("\nPATIENT PROFILE (Maelezo ya Mgonjwa):")
    print("-" * 40)
    age = int(input("👤 Age/Umri (years): "))
    gender = input("⚥  Gender/Jinsia (Male/Female): ").strip().capitalize()
    bp = input("🩺 Blood Pressure (Low/Normal/High): ").strip().capitalize()
    cholesterol = input("💉 Cholesterol Level (Low/Normal/High): ").strip().capitalize()
    
    return {
        'Fever': fever,
        'Cough': cough,
        'Fatigue': fatigue,
        'Difficulty Breathing': breathing,
        'Age': age,
        'Gender': gender,
        'Blood Pressure': bp,
        'Cholesterol Level': cholesterol
    }

def prepare_input(user_data, model_data):
    """Prepare user input for model prediction."""
    # Convert symptoms to binary
    input_dict = {
        'Fever': 1 if user_data['Fever'] == 'yes' else 0,
        'Cough': 1 if user_data['Cough'] == 'yes' else 0,
        'Fatigue': 1 if user_data['Fatigue'] == 'yes' else 0,
        'Difficulty Breathing': 1 if user_data['Difficulty Breathing'] == 'yes' else 0,
        'Age': user_data['Age'],
        'Gender': model_data['label_encoders']['Gender'].transform([user_data['Gender']])[0],
        'Blood Pressure': model_data['label_encoders']['Blood Pressure'].transform([user_data['Blood Pressure']])[0],
        'Cholesterol Level': model_data['label_encoders']['Cholesterol Level'].transform([user_data['Cholesterol Level']])[0]
    }
    
    # Create DataFrame with correct feature order
    input_df = pd.DataFrame([input_dict])[model_data['feature_names']]
    
    # Scale the input
    input_scaled = model_data['scaler'].transform(input_df)
    
    return input_scaled

def make_prediction(model_data, input_scaled):
    """Make prediction using the trained model."""
    prediction = model_data['model'].predict(input_scaled)[0]
    probabilities = model_data['model'].predict_proba(input_scaled)[0]
    
    return prediction, probabilities

def display_results(prediction, probabilities):
    """Display prediction results to user."""
    print("\n" + "="*60)
    print("🎯 PREDICTION RESULTS / MATOKEO")
    print("="*60)
    
    risk_level = "HIGH RISK !" if prediction == 1 else "LOW RISK OK"
    risk_swahili = "HATARI YA JUU" if prediction == 1 else "HATARI YA CHINI"
    confidence = max(probabilities) * 100
    urgency_score = probabilities[1] * 100
    
    print(f"\n🔔 Risk Level: {risk_level}")
    print(f"   {risk_swahili}")
    print(f"\n📊 Confidence: {confidence:.1f}%")
    print(f"   Imani: {confidence:.1f}%")
    print(f"\n⚡ Urgency Score: {urgency_score:.1f}/100")
    print(f"   Kiwango cha Dharura: {urgency_score:.1f}/100")
    
    print("\n" + "-"*60)
    print("* RECOMMENDATIONS / MAPENDEKEZO:")
    print("-"*60)
    
    if prediction == 1:
        print("""
!  URGENT ATTENTION NEEDED
    
English:
✓ Seek immediate medical consultation
✓ Visit the nearest health facility
✓ Monitor symptoms closely
✓ Do not delay treatment

Swahili:
✓ Tafuta ushauri wa kitabibu mara moja
✓ Tembelea kituo cha afya cha karibu
✓ Fuatilia dalili kwa karibu
✓ Usichelewe kupata matibabu
        """)
    else:
        print("""
OK LOW RISK - CONTINUE MONITORING
    
English:
✓ Continue monitoring symptoms
✓ Maintain healthy habits
✓ Consult a doctor if symptoms worsen
✓ Stay hydrated and rest well

Swahili:
✓ Endelea kufuatilia dalili
✓ Endelea na mazoea mazuri ya afya
✓ Tembelea daktari ikiwa dalili zinazidi
✓ Kunywa maji mengi na kupumzika vizuri
        """)
    
    print("\n" + "="*60)
    print("⚕️  DISCLAIMER:")
    print("This is an AI prediction tool for educational and")
    print("decision-support purposes. Always consult qualified")
    print("healthcare professionals for medical advice.")
    print("="*60 + "\n")

def main():
    """Main prediction pipeline."""
    # Load model
    print("Loading AI model...")
    model_data = load_model()
    print("Model loaded successfully!\n")
    
    # Get user input
    user_data = get_user_input()
    
    # Prepare input
    input_scaled = prepare_input(user_data, model_data)
    
    # Make prediction
    prediction, probabilities = make_prediction(model_data, input_scaled)
    
    # Display results
    display_results(prediction, probabilities)
    
    # Ask if user wants to make another prediction
    another = input("Would you like to make another prediction? (yes/no): ").strip().lower()
    if another == 'yes':
        main()
    else:
        print("\n🌍 Afya Karibu - Supporting SDG 3: Good Health and Well-being")
        print("Thank you for using Afya Karibu AI! Stay healthy! 💚\n")

if __name__ == "__main__":
    main()


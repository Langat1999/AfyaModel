
# Afya Karibu AI Setup Guide

This guide will walk you through setting up the Afya Karibu AI project from scratch.

---

## 📋 Table of Contents

1. [Prerequisites](#1-prerequisites)
2. [Installation](#2-installation)
3. [Training the model](#3-training-the-model)
4. [Running the web app](#4-running-the-web-app)
5. [Using the command-line interface](#5-using-the-command-line-interface)
6. [Exploring the jupyter notebook](#6-exploring-the-jupyter-notebook)
7. [Troubleshooting](#7-troubleshooting)
8. [Next steps](#8-next-steps)

---

## 1. Prerequisites

### System Requirements

- **Operating System**: Windows 10/11, macOS, or Linux
- **Python**: Version 3.8 or higher
- **RAM**: Minimum 4GB (8GB recommended)
- **Disk Space**: 500MB free space

### Required Software

1. **Python** - [Download here](https://www.python.org/downloads/)
   - During installation, check "Add Python to PATH"

2. **Git** (optional, for cloning) - [Download here](https://git-scm.com/downloads)

3. **Text Editor/IDE** (optional) - Choose one:
   - [VS Code](https://code.visualstudio.com/)
   - [PyCharm](https://www.jetbrains.com/pycharm/)
   - [Jupyter Lab](https://jupyter.org/)

---

## 2. Installation

### Step 1: Get the code

#### Option A: Download ZIP

1. Download the project ZIP file
2. Extract to your desired location
3. Open terminal/command prompt
4. Navigate to project folder:

```bash
cd path/to/AfyaModel
```markdown

#### Option B: Clone with Git

```bash
git clone https://github.com/yourusername/AfyaModel.git
cd AfyaModel
```

### Step 2: Verify Python Installation

```bash
python --version
```

You should see: `Python 3.8.x` or higher

**Windows users**: If `python` doesn't work, try `py` instead:

```bash
py --version
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

This will install all required packages:

- pandas (data manipulation)
- scikit-learn (machine learning)
- streamlit (web app)
- matplotlib, seaborn, plotly (visualization)
- jupyter (notebooks)

**Installation time**: 2-5 minutes depending on internet speed

### Step 4: Verify Installation

```bash
python -c "import pandas, sklearn, streamlit; print('✅ All packages installed successfully!')"
```

---

## 3. Training the Model

### Option 1: Using Python Script (Recommended for beginners)

```bash
python train_model.py
```

**What this does**:

- Loads the health dataset
- Preprocesses the data
- Trains 3 different ML models
- Selects the best model
- Saves the model as `afya_karibu_health_model.pkl`

**Expected output** (sample):

```
==================================================
🏥 AFYA KARIBU AI - MODEL TRAINING
==================================================

📊 Loading dataset...
✅ Loaded 349 patient records

🔧 Preprocessing data...
✅ Preprocessing complete

📐 Splitting data...
✅ Training set: 279 samples
✅ Test set: 70 samples

🤖 TRAINING MODELS
==================================================

Training Random Forest...
✅ Random Forest
   Accuracy: 0.921
   AUC Score: 0.941

...

🏆 BEST MODEL: Random Forest
   Accuracy: 0.921
   AUC: 0.941

💾 Saving model...
✅ Model saved as 'afya_karibu_health_model.pkl'
```

**Training time**: 10-30 seconds

### Option 2: Using Jupyter Notebook (For detailed analysis)

```bash
jupyter notebook afya_karibu_ml.ipynb
```

This will:

1. Open Jupyter in your browser
2. Show the complete ML workflow with visualizations
3. Allow you to experiment and modify the code

**To run**:

- Click "Cell" → "Run All"
- Or use keyboard shortcut: Shift + Enter for each cell

---

## 4. Running the Web App

### Start the Streamlit Application

```bash
streamlit run app.py
```

**Expected output**:

You can now view your Streamlit app in your browser.

Local URL: <http://localhost:8501>
Network URL: <http://192.168.x.x:8501>

```

The app will automatically open in your default browser.

### Using the Web Interface

1. **Enter Symptoms**:
   - Select Yes/No for each symptom (Fever, Cough, Fatigue, Breathing difficulty)

2. **Provide Patient Profile**:
   - Age (1-120)
   - Gender (Male/Female)
   - Blood Pressure (Low/Normal/High)
   - Cholesterol Level (Low/Normal/High)

3. **Click "Predict Health Urgency"**

4. **View Results**:
   - Risk level (High/Low)
   - Confidence score
   - Visual charts
   - Recommendations

### Stopping the App

- Press `Ctrl + C` in the terminal
- Or close the terminal window

---

## 5. Using the Command-Line Interface

### Run the Prediction Script

```bash
python predict.py
```

### Interactive Session Example

```
==================================================

🏥 AFYA KARIBU AI - HEALTH URGENCY PREDICTION
==================================================

Karibu! Welcome! Please provide patient information:

SYMPTOMS (Dalili):
----------------------------------------
🌡️  Do you have Fever/Homa? (yes/no): yes
🤧 Do you have Cough/Kikohozi? (yes/no): yes
😴 Do you have Fatigue/Uchovu? (yes/no): yes
💨 Difficulty Breathing/Shida ya Kupumua? (yes/no): no

PATIENT PROFILE (Maelezo ya Mgonjwa):
----------------------------------------
👤 Age/Umri (years): 35
⚥  Gender/Jinsia (Male/Female): Female
🩺 Blood Pressure (Low/Normal/High): Normal
💉 Cholesterol Level (Low/Normal/High): Normal

==================================================
🎯 PREDICTION RESULTS / MATOKEO
==================================================

🔔 Risk Level: HIGH RISK ⚠️
   HATARI YA JUU

📊 Confidence: 87.3%
   Imani: 87.3%

⚡ Urgency Score: 87.3/100
   Kiwango cha Dharura: 87.3/100

------------------------------------------------------------
💡 RECOMMENDATIONS / MAPENDEKEZO:
------------------------------------------------------------

⚠️  URGENT ATTENTION NEEDED
    
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
```

---

## 6. Exploring the Jupyter Notebook

### Launch Jupyter

```bash
jupyter notebook
```

### Open the Notebook

1. Click on `afya_karibu_ml.ipynb` in the file browser
2. The notebook contains:
   - Data exploration and visualization
   - Complete ML workflow
   - Model training and evaluation
   - Performance metrics and charts

### Navigate the Notebook

- **Run a cell**: Shift + Enter
- **Insert cell**: A (above) or B (below)
- **Delete cell**: DD
- **Restart kernel**: Kernel → Restart

### Key Sections

1. **Introduction**: Project overview and SDG context
2. **Data Loading**: Import and explore the dataset
3. **EDA**: Visualizations and statistical analysis
4. **Preprocessing**: Data cleaning and encoding
5. **Model Training**: Train multiple algorithms
6. **Evaluation**: Performance metrics and comparisons
7. **Interpretation**: Feature importance and insights

---

## 7. Troubleshooting

### Common Issues and Solutions

#### Issue 1: "python: command not found"

**Solution (Windows)**:

```bash
py train_model.py
```

**Solution (Mac/Linux)**:

```bash
python3 train_model.py
```

#### Issue 2: "No module named 'pandas'" (or other packages)

**Solution**:

```bash
pip install --upgrade -r requirements.txt
```

**If pip doesn't work**:

```bash
python -m pip install --upgrade -r requirements.txt
```

#### Issue 3: "Model file not found"

**Solution**: Train the model first:

```bash
python train_model.py
```

#### Issue 4: Streamlit app won't start

**Solution 1** - Check if port 8501 is already in use:

```bash
streamlit run app.py --server.port 8502
```

**Solution 2** - Clear Streamlit cache:

```bash
streamlit cache clear
```

#### Issue 5: Jupyter notebook won't open

**Solution**:

```bash
pip install --upgrade jupyter
jupyter notebook --no-browser
```

Then manually open the URL shown in terminal.

#### Issue 6: Import errors in notebook

**Solution**: Install jupyter kernel:

```bash
pip install ipykernel
python -m ipykernel install --user --name afya --display-name "Afya Karibu"
```

Then in Jupyter: Kernel → Change Kernel → Afya Karibu

---

## 8. Next Steps

### After Setup is Complete

✅ **Explore the Data**

- Open Jupyter notebook
- Examine data distributions
- Try different visualizations

✅ **Test the Model**

- Use the web app with different symptom combinations
- Test edge cases (all symptoms, no symptoms)
- Check predictions for different age groups

✅ **Customize the Project**

- Modify the Streamlit app appearance
- Add new features to the dataset
- Experiment with different ML algorithms

✅ **Share Your Work**

- Create a GitHub repository
- Take screenshots for your README
- Write your experience article
- Present to peers

### Advanced Tasks

🔧 **Improve the Model**:

- Collect more diverse data
- Try deep learning (Neural Networks)
- Implement hyperparameter tuning

🌐 **Deploy Online**:

- Streamlit Cloud (free hosting)
- Heroku
- AWS/GCP/Azure

📱 **Build Mobile App**:

- React Native
- Flutter
- Android Studio

---

## 📞 Getting Help

### Resources

- **Project Documentation**: README.md
- **Ethical Guidelines**: ETHICAL_REFLECTION.md
- **Article**: ARTICLE.md
- **Pitch Deck**: PITCH_DECK.md

### Support Channels

- **GitHub Issues**: Report bugs or ask questions
- **PLP Academy Forum**: Community support
- **Email**: <your.email@example.com>

### Useful Commands Reference

```bash
# Install packages
pip install -r requirements.txt

# Train model
python train_model.py

# Make predictions (CLI)
python predict.py

# Launch web app
streamlit run app.py

# Open Jupyter notebook
jupyter notebook afya_karibu_ml.ipynb

# Check Python version
python --version

# List installed packages
pip list

# Update all packages
pip install --upgrade -r requirements.txt
```

---

## ✅ Quick Start Checklist

- [ ] Python 3.8+ installed
- [ ] Cloned/downloaded project
- [ ] Installed dependencies (`pip install -r requirements.txt`)
- [ ] Trained model (`python train_model.py`)
- [ ] Tested web app (`streamlit run app.py`)
- [ ] Explored Jupyter notebook
- [ ] Read documentation (README.md, ETHICAL_REFLECTION.md)
- [ ] Ready to customize and extend!

---

## Congratulations! 🎉

You're now ready to use and contribute to Afya Karibu AI!

### Supporting UN SDG 3: Good Health and Well-being 🌍

---

**Last Updated**: October 2025  
**Version**: 1.0  
**Maintained by**: Afya Karibu Team

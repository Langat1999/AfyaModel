# Screenshots Directory

This directory contains screenshots for the Afya Karibu AI project documentation.

## Required Screenshots

Add the following screenshots after running the project.

### Data Analysis Dashboard

**Filename**: `data_analysis.png`

**How to capture**:

- Run the Jupyter notebook:

```bash
jupyter notebook afya_karibu_ml.ipynb
```

- Execute cells in the Data Exploration section and take screenshots of visualization outputs.

**Shows**:

- Outcome distribution chart
- Top 10 diseases bar chart
- Symptom correlation heatmap
- Demographic visualizations

---

### Model Performance

**Filename**: `model_performance.png`

**How to capture**:

- Continue through the notebook to the Model Evaluation section.
- Screenshot the confusion matrix, ROC curve, and feature importance.

**Shows**:

- Confusion matrix
- ROC curve with AUC score
- Feature importance chart
- Classification metrics

---

### Streamlit Web App

**Filename**: `streamlit_app.png`

**How to capture**:

- Run the app:

```bash
streamlit run app.py
```

- Take a full-page screenshot of the main interface showing the input form and sidebar.

**Shows**:

- Main header and branding
- Symptom input form (bilingual)
- Patient profile inputs
- Sidebar with project information

---

### Prediction Results

**Filename**: `prediction_results.png`

**How to capture**:

- In the Streamlit app, enter sample patient data and click "Predict Health Urgency".
- Screenshot the results section.

**Shows**:

- Risk level prediction
- Confidence score
- Urgency gauge visualization
- Probability distribution chart
- Recommendations

---

### Command Line Interface (Optional)

**Filename**: `cli_prediction.png`

**How to capture**:

- Run the CLI prediction:

```bash
python predict.py
```

- Complete an interactive prediction session and screenshot the terminal output.

**Shows**:

- Interactive symptom input
- Prediction results in terminal
- Bilingual output (English/Swahili)

---

## Screenshot Guidelines

### Best Practices

1. Resolution: Minimum 1920x1080 for clarity
2. Format: PNG or JPEG
3. Cropping: Include relevant information; remove unnecessary whitespace
4. Annotations: Optional — add arrows or text to highlight key features
5. Quality: Ensure text is readable

### Tools for Screenshots

**Windows**:

- Snipping Tool (Win + Shift + S)
- PowerPoint (for annotations)

**Mac**:

- Command + Shift + 3 (full screen)
- Command + Shift + 4 (selection)
- Preview (for annotations)

**Linux**:

- gnome-screenshot
- Shutter
- Flameshot

### Adding to README

After capturing screenshots, include them in `README.md`:

```markdown
![Data Analysis](screenshots/data_analysis.png)
![Model Performance](screenshots/model_performance.png)
![Streamlit App](screenshots/streamlit_app.png)
![Prediction Results](screenshots/prediction_results.png)
```

---

## Demo Video (Optional Enhancement)

Consider creating a short demo video (2–3 minutes) showing:

1. Project overview
2. Running the Streamlit app
3. Making a prediction
4. Interpreting results

**Tools**: OBS Studio, Loom, Windows Game Bar, QuickTime

---

**Status**: 📷 Awaiting screenshots

**Updated**: October 2025

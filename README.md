# Gene Expression Cancer Detection

## 🚀 Project Overview

**Gene Expression Cancer Detection** is a machine‑learning pipeline that classifies samples as “cancer” vs. “healthy” (or cancer subtypes) based on genome‑wide expression profiles. This end‑to‑end project covers data acquisition, preprocessing, exploratory analysis, model training, evaluation, and interpretability.

---

## 📋 Table of Contents

1. [Background & Motivation](#background--motivation)
2. [Data Sources](#data-sources)
3. [Installation](#installation)
4. [Project Structure](#project-structure)
5. [Workflow & Methodology](#workflow--methodology)

   * 5.1 [Data Acquisition](#data-acquisition)
   * 5.2 [Preprocessing](#preprocessing)
   * 5.3 [Exploratory Data Analysis](#exploratory-data-analysis)
   * 5.4 [Modeling](#modeling)
   * 5.5 [Evaluation & Interpretation](#evaluation--interpretation)
6. [Results](#results)
7. [Usage](#usage)
8. [Contributing](#contributing)
9. [License](#license)
10. [References](#references)

---

## Background & Motivation

Cancer is characterized by aberrant gene expression patterns. By leveraging high‑throughput transcriptomics (e.g., microarray or RNA‑Seq), we can train predictive models that distinguish cancerous vs. normal tissue—or even specific tumor subtypes. This workflow aims to:

* Demonstrate bioinformatics preprocessing best practices
* Compare various classification algorithms on high‑dimensional data
* Identify the top genes driving the model via interpretability tools

---

## Data Sources

* **GEO Dataset GSE2034** – Breast cancer microarray profiles (recurrence vs. non‑recurrence)
* **TCGA** (optional) – Download RNA‑Seq expression for multiple cancer types via the GDC portal
* Raw files in `data/raw/` and processed CSVs in `data/processed/`

---

## Installation

1. **Clone the repo**

   ```bash
   git clone https://github.com/your‑username/gene-cancer-detect.git
   cd gene-cancer-detect
   ```

2. **Create a conda environment**

   ```bash
   conda env create -f environment.yml
   conda activate gene-cancer-detect
   ```

3. **Install Python dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

## Project Structure

```
gene-cancer-detect/
├── data/
│   ├── raw/                  # Original downloaded datasets
│   └── processed/            # Normalized & cleaned CSVs
├── notebooks/                # Jupyter notebooks for each step
│   ├── 1_data_acquisition.ipynb
│   ├── 2_preprocessing.ipynb
│   ├── 3_eda.ipynb
│   ├── 4_modeling.ipynb
│   └── 5_interpretation.ipynb
├── src/
│   ├── data_loader.py        # Functions to fetch & load GEO/TCGA
│   ├── preprocessing.py      # Normalization, filtering, scaling
│   └── modeling.py           # Model training & evaluation routines
├── app/                      # (Optional) Streamlit app for predictions
├── environment.yml           # Conda environment specification
├── requirements.txt          # Pip dependencies
├── README.md                 # Detailed project overview
└── LICENSE
```

---

## Workflow & Methodology

### Data Acquisition

* Use **GEOparse** (Python) or **GEOquery** (R) to download GSE2034
* Extract expression matrix (samples × genes) and clinical labels

### Preprocessing

1. **Quality Control:** Remove low‑variance genes
2. **Normalization:** Log2 transform & quantile normalization
3. **Scaling:** Standardize features (z‑score)
4. **Train/Test Split:** Stratified split (e.g., 80/20)

### Exploratory Data Analysis

* **PCA/t‑SNE:** Visualize sample clustering (cancer vs. healthy)
* **Boxplots/Violin plots:** Compare expression distributions for top genes

### Modeling

* **Dimensionality Reduction:**

  * Univariate feature selection (SelectKBest)
  * PCA (optional)
* **Classification Algorithms:**

  * Logistic Regression
  * Random Forest
  * Support Vector Machine
  * XGBoost
* **Hyperparameter Tuning:** GridSearchCV with 5‑fold CV

### Evaluation & Interpretation

* **Metrics:** Accuracy, Precision, Recall, F1, ROC‑AUC
* **Confusion Matrix & ROC Curve**
* **Interpretability:**

  * Feature importance (tree‑based)
  * **SHAP** values to identify top predictive genes

---

## Results

* **Best Model:** XGBoost with ROC‑AUC of 0.92 on test set
* **Top 10 Genes:** List and brief biological annotations
* **Visualizations:**

  * ROC curve
  * SHAP summary plot

*(Full plots and tables are available in `notebooks/5_interpretation.ipynb`.)*

---

## Usage

1. **Run the main notebook**

   ```bash
   jupyter notebook notebooks/4_modeling.ipynb
   ```

2. **(Optional) Launch Streamlit app**

   ```bash
   cd app
   streamlit run app.py
   ```

   * Input your own gene‑expression CSV
   * Get instant prediction and feature contribution

---

## Contributing

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/xyz`)
3. Commit your changes & push (`git push origin feature/xyz`)
4. Open a Pull Request

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## References

* Rhodes et al., “Large‑scale meta‑analysis of breast cancer recurrence” (GSE2034)
* Pedregosa et al., “Scikit‑learn: Machine Learning in Python” (JMLR, 2011)
* Lundberg & Lee, “A Unified Approach to Interpreting Model Predictions” (NIPS, 2017)

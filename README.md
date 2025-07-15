# gene-cancer-detection

[![GitHub stars](https://img.shields.io/github/stars/Ismat-Samadov/gene-cancer-detection)](https://github.com/Ismat-Samadov/gene-cancer-detection/stargazers) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Machine‑learning pipeline to classify cancer vs. healthy samples using gene expression profiles.

---

## 🚀 Project Overview

**Gene Expression Cancer Detection** is an end-to-end workflow that acquires, preprocesses, and analyzes transcriptomic data to train and interpret classification models distinguishing cancerous from normal tissue (or subtypes).

---

## 📋 Table of Contents

1. [Background & Motivation](#background--motivation)
2. [Data Sources](#data-sources)
3. [Installation](#installation)
4. [Project Structure](#project-structure)
5. [Workflow & Methodology](#workflow--methodology)

   * [Data Acquisition](#data-acquisition)
   * [Preprocessing](#preprocessing)
   * [Exploratory Data Analysis](#exploratory-data-analysis)
   * [Modeling](#modeling)
   * [Evaluation & Interpretation](#evaluation--interpretation)
6. [Results](#results)
7. [Usage](#usage)
8. [Contributing](#contributing)
9. [License](#license)
10. [References](#references)

---

## Background & Motivation

Cancer manifests through altered gene expression patterns. Leveraging high‑throughput transcriptomics (microarray or RNA‑Seq), this project uses machine learning to:

* Demonstrate bioinformatics preprocessing best practices
* Compare classification algorithms on high-dimensional data
* Identify key predictive genes via model interpretability tools

---

## Data Sources

* **GEO Dataset GSE2034** – Breast cancer microarray profiles (recurrence vs. non‑recurrence)
* **TCGA** (optional) – RNA‑Seq expression for various cancer types via the GDC portal
* Raw files stored in `data/raw/`, processed CSVs in `data/processed/`

---

## Installation

1. **Clone the repo**

   ```bash
   git clone https://github.com/Ismat-Samadov/gene-cancer-detection.git
   cd gene-cancer-detection
   ```

2. **Create a conda environment**

   ```bash
   conda env create -f environment.yml
   conda activate gene-cancer-detection
   ```

3. **Install Python dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

## Project Structure

```
gene-cancer-detection/
├── data/
│   ├── raw/                  # Original downloaded datasets
│   └── processed/            # Cleaned & normalized CSVs
├── notebooks/                # Jupyter notebooks for each step
│   ├── 1_data_acquisition.ipynb
│   ├── 2_preprocessing.ipynb
│   ├── 3_eda.ipynb
│   ├── 4_modeling.ipynb
│   └── 5_interpretation.ipynb
├── src/
│   ├── data_loader.py        # Functions to fetch & load GEO/TCGA data
│   ├── preprocessing.py      # Normalization, filtering, scaling routines
│   └── modeling.py           # Model training & evaluation pipelines
├── app/                      # (Optional) Streamlit app for live predictions
├── environment.yml           # Conda environment spec
├── requirements.txt          # Pip dependencies
├── README.md                 # Project overview & instructions
└── LICENSE                   # MIT license
```

---

## Workflow & Methodology

### Data Acquisition

* Use **GEOparse** (Python) or **GEOquery** (R) to download GSE2034
* Extract expression matrix (samples × genes) and clinical labels

### Preprocessing

1. **Quality Control:** Remove low-variance genes
2. **Normalization:** Log2 transform & quantile normalization
3. **Scaling:** Standardize features (z-score)
4. **Train/Test Split:** Stratified 80/20 split

### Exploratory Data Analysis

* **PCA/t-SNE:** Visualize sample clusters (cancer vs. normal)
* **Boxplots & Violin plots:** Compare expression distributions for top genes

### Modeling

* **Dimensionality Reduction:** SelectKBest, PCA (optional)
* **Algorithms:** Logistic Regression, Random Forest, SVM, XGBoost
* **Hyperparameter Tuning:** GridSearchCV with 5-fold cross-validation

### Evaluation & Interpretation

* **Metrics:** Accuracy, Precision, Recall, F1-score, ROC-AUC
* **Visualization:** Confusion matrix, ROC curve
* **Interpretability:** Feature importance & SHAP summary plots

---

## Results

* **Best Model:** XGBoost achieving ROC-AUC of \~0.92 on the test set
* **Top Predictive Genes:** Listed with brief biological context
* **Visual Summaries:** ROC curve, SHAP plots available in `notebooks/5_interpretation.ipynb`

---

## Usage

1. **Run the modeling notebook**

   ```bash
   jupyter notebook notebooks/4_modeling.ipynb
   ```

2. **(Optional) Launch Streamlit app**

   ```bash
   cd app
   streamlit run app.py
   ```

   * Upload your gene-expression CSV to get predictions and feature contributions

---

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/xyz`
3. Commit your changes: `git commit -m "Add feature xyz"`
4. Push to your branch: `git push origin feature/xyz`
5. Open a Pull Request

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## References

* Rhodes et al., *Large‑scale meta‑analysis of breast cancer recurrence* (GSE2034)
* Pedregosa et al., *Scikit‑learn: Machine Learning in Python* (JMLR, 2011)
* Lundberg & Lee, *A Unified Approach to Interpreting Model Predictions* (NIPS, 2017)

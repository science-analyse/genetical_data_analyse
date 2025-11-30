# Gene Expression Cancer Classifier: ALL vs AML

A machine learning application for classifying Acute Lymphoblastic Leukemia (ALL) and Acute Myeloid Leukemia (AML) using gene expression data, based on the landmark study by Golub et al. (1999).

## 🚀 Quick Start with Docker

**Option 1: Using the startup script (easiest)**
```bash
# 1. First time: Run analysis notebook to train models
pip install -r notebooks/analyse_requirements.txt
jupyter notebook notebooks/analyse.ipynb  # Run all cells

# 2. Run the startup script
./start.sh
```

**Option 2: Manual Docker commands**
```bash
# 1. First time: Run analysis notebook to train models
pip install -r notebooks/analyse_requirements.txt
jupyter notebook notebooks/analyse.ipynb  # Run all cells

# 2. Deploy with Docker
docker-compose up -d

# 3. Access the app
open http://localhost:8000
```

## Project Structure

```
genetical_data_analyse/
├── notebooks/
│   ├── analyse.ipynb                    # Main analysis notebook
│   ├── prediction.ipynb                 # Prediction testing notebook
│   ├── analyse_requirements.txt         # Requirements for analysis
│   └── prediction_requirements.txt      # Requirements for prediction
├── models/                              # Saved trained models (generated)
│   ├── best_model_svm_rbf.pkl
│   ├── scaler.pkl
│   ├── top_genes_indices.pkl
│   └── gene_metadata.pkl
├── data/                                # Gene expression datasets
│   ├── data_set_ALL_AML_train.csv
│   ├── data_set_ALL_AML_independent.csv
│   └── actual.csv
├── static/                              # Web app static files
│   └── style.css
├── templates/                           # Jinja2 templates
│   └── index.html
├── app.py                               # FastAPI web application
├── predictor.py                         # Prediction module
├── requirements.txt                     # Web app requirements
├── Dockerfile                           # Docker configuration
├── docker-compose.yml                   # Docker Compose configuration
├── .dockerignore                        # Docker ignore file
├── .gitignore                           # Git ignore file
├── start.sh                             # Startup script
└── README.md                            # This file
```

## Dataset

**Source**: Golub et al. (1999) - "Molecular Classification of Cancer: Class Discovery and Class Prediction by Gene Expression Monitoring"

- **Training set**: 38 samples (27 ALL, 11 AML)
- **Test set**: 34 samples (20 ALL, 14 AML)
- **Genes**: 7,129 gene expression measurements per sample
- **Kaggle**: [Gene Expression Dataset](https://www.kaggle.com/datasets/crawford/gene-expression)

## Setup Instructions

### 1. Clone the Repository

```bash
cd genetical_data_analyse
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Run Analysis Notebook (First Time Only)

Install analysis dependencies:
```bash
pip install -r notebooks/analyse_requirements.txt
```

Open and run the analysis notebook:
```bash
jupyter notebook notebooks/analyse.ipynb
```

This will:
- Perform exploratory data analysis
- Identify differentially expressed genes
- Train multiple classification models
- Save the best model and artifacts to `models/` directory

### 4. Install Web App Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the FastAPI Application

```bash
python app.py
```

Or with uvicorn:
```bash
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

The web application will be available at: `http://localhost:8000`

## Docker Deployment (Recommended)

The easiest way to deploy the application is using Docker. This ensures consistent behavior across different environments.

### Prerequisites

- Docker installed ([Get Docker](https://docs.docker.com/get-docker/))
- Docker Compose installed (included with Docker Desktop)
- Trained models in `models/` directory (run analyse.ipynb first)

### Quick Start with Docker

1. **Build and run with Docker Compose**:
```bash
docker-compose up -d
```

This will:
- Build the Docker image
- Start the container in detached mode
- Map port 8000 to your host
- Mount the models and data directories

2. **Access the application**:
```
http://localhost:8000
```

3. **View logs**:
```bash
docker-compose logs -f
```

4. **Stop the application**:
```bash
docker-compose down
```

### Alternative: Build and Run Manually

```bash
# Build the image
docker build -t gene-classifier .

# Run the container
docker run -d \
  --name gene-classifier \
  -p 8000:8000 \
  -v $(pwd)/models:/app/models \
  -v $(pwd)/data:/app/data:ro \
  gene-classifier
```

### Docker Commands Reference

```bash
# Check container status
docker-compose ps

# Restart the service
docker-compose restart

# View container logs
docker-compose logs -f web

# Stop and remove containers
docker-compose down

# Rebuild the image
docker-compose build --no-cache

# Remove all containers and volumes
docker-compose down -v
```

### Important Notes

- **Models Directory**: Ensure `models/` directory exists with trained models before running Docker
- **First Time Setup**: Run `notebooks/analyse.ipynb` once to generate models
- **Port Conflicts**: If port 8000 is already in use, modify `docker-compose.yml`
- **Persistent Data**: Models are mounted as a volume, so they persist across container restarts

## Usage

### Web Interface

Access the web application at `http://localhost:8000` with three prediction options:

1. **Test with Sample Data**: Load a sample from the test dataset
2. **Upload CSV**: Upload a CSV file with gene expression data
3. **Manual Input**: Paste JSON data directly

#### CSV File Format

Your CSV should have:
- One row per sample
- 7,129 columns (one per gene)
- Optional first column with sample IDs

Example:
```csv
sample_id,gene1,gene2,gene3,...,gene7129
patient_1,234.5,156.2,789.1,...,456.3
patient_2,345.6,267.3,890.2,...,567.4
```

#### JSON Format

```json
{
  "gene_expressions": [val1, val2, val3, ..., val7129]
}
```

### API Endpoints

#### Get Model Information
```bash
curl http://localhost:8000/api/model-info
```

#### Make Prediction (JSON)
```bash
curl -X POST http://localhost:8000/api/predict-json \
  -H "Content-Type: application/json" \
  -d '{"gene_expressions": [...]}'
```

#### Upload CSV for Prediction
```bash
curl -X POST http://localhost:8000/api/predict-csv \
  -F "file=@your_data.csv"
```

#### Get Sample Data
```bash
curl http://localhost:8000/api/sample-data
```

#### Health Check
```bash
curl http://localhost:8000/health
```

### API Documentation

Interactive API documentation available at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Prediction Notebook

Test the prediction functionality using the notebook:

```bash
pip install -r notebooks/prediction_requirements.txt
jupyter notebook notebooks/prediction.ipynb
```

## Model Performance

The best performing model (SVM with RBF kernel):
- **Test Accuracy**: ~62%
- **Cross-Validation Accuracy**: ~97.5%
- **Features**: Top 50 differentially expressed genes
- **Classes**: ALL (Acute Lymphoblastic Leukemia), AML (Acute Myeloid Leukemia)

## Key Features

1. **Comprehensive Analysis**:
   - Differential gene expression analysis
   - PCA dimensionality reduction
   - Multiple ML models (SVM, Random Forest, Logistic Regression)

2. **Production-Ready API**:
   - FastAPI with async support
   - RESTful endpoints
   - Input validation
   - Error handling

3. **User-Friendly Interface**:
   - Beautiful, responsive web UI
   - Multiple input methods
   - Real-time predictions
   - Probability visualization

4. **Reproducible Research**:
   - Jupyter notebooks for analysis
   - Saved model artifacts
   - Clear documentation

## Technology Stack

- **Backend**: FastAPI, Python 3.8+
- **ML/Data Science**: scikit-learn, pandas, numpy
- **Visualization**: matplotlib, seaborn
- **Frontend**: HTML, CSS, JavaScript (Vanilla)
- **Templating**: Jinja2
- **Deployment**: Docker, Docker Compose

## Citation

If you use this project, please cite the original paper:

```
Golub, T.R., Slonim, D.K., Tamayo, P., et al. (1999).
Molecular Classification of Cancer: Class Discovery and Class Prediction by Gene Expression Monitoring.
Science, 286(5439), 531-537.
```

## License

This project is for educational and research purposes. Please refer to the original dataset license on Kaggle.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Contact

For questions or issues, please open an issue on GitHub.

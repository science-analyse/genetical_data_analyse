from fastapi import FastAPI, Request, UploadFile, File, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse
import pandas as pd
import numpy as np
from typing import List
import io

# Import prediction module
import predictor

# Initialize FastAPI app
app = FastAPI(
    title="Gene Expression Cancer Classifier",
    description="ALL vs AML Classification using Gene Expression Data",
    version="1.0.0"
)

# Mount static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Render the home page"""
    model_info = predictor.get_model_info()
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "model_info": model_info
        }
    )


@app.get("/api/model-info")
async def get_model_info():
    """Get model information"""
    return predictor.get_model_info()


@app.post("/api/predict")
async def predict(gene_expressions: List[float]):
    """
    Make a prediction from gene expression data

    Parameters:
    -----------
    gene_expressions : List[float]
        List of 7129 gene expression values

    Returns:
    --------
    dict : Prediction results
    """
    try:
        # Convert to numpy array
        gene_data = np.array(gene_expressions)

        # Make prediction
        result = predictor.predict_cancer_type(gene_data)

        return JSONResponse(content=result)

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")


@app.post("/api/predict-csv")
async def predict_from_csv(file: UploadFile = File(...)):
    """
    Make predictions from a CSV file containing gene expression data

    The CSV should have:
    - One row per sample
    - 7129 columns (one per gene)
    - Optional first column with sample IDs
    """
    try:
        # Read CSV file
        contents = await file.read()
        df = pd.read_csv(io.StringIO(contents.decode('utf-8')))

        # Check if first column is sample ID (non-numeric)
        if df.iloc[:, 0].dtype == 'object':
            sample_ids = df.iloc[:, 0].tolist()
            gene_data = df.iloc[:, 1:].values
        else:
            sample_ids = [f"Sample_{i+1}" for i in range(len(df))]
            gene_data = df.values

        # Validate number of genes
        if gene_data.shape[1] != 7129:
            raise ValueError(f"Expected 7129 genes, got {gene_data.shape[1]}")

        # Make predictions for each sample
        results = []
        for i, sample in enumerate(gene_data):
            prediction = predictor.predict_cancer_type(sample)
            prediction['sample_id'] = sample_ids[i]
            results.append(prediction)

        return JSONResponse(content={"predictions": results, "total_samples": len(results)})

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"CSV processing error: {str(e)}")


@app.post("/api/predict-json")
async def predict_from_json(data: dict):
    """
    Make a prediction from JSON data

    Expected format:
    {
        "gene_expressions": [val1, val2, ..., val7129]
    }
    """
    try:
        gene_expressions = data.get('gene_expressions')

        if not gene_expressions:
            raise ValueError("Missing 'gene_expressions' field")

        # Convert to numpy array
        gene_data = np.array(gene_expressions)

        # Make prediction
        result = predictor.predict_cancer_type(gene_data)

        return JSONResponse(content=result)

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")


@app.get("/api/sample-data")
async def get_sample_data():
    """
    Get sample gene expression data for testing
    """
    try:
        # Load test data
        test_df = pd.read_csv('data/data_set_ALL_AML_independent.csv')
        labels_df = pd.read_csv('data/actual.csv')

        # Get expression columns
        gene_info_cols = ['Gene Description', 'Gene Accession Number']
        test_cols = test_df.columns.tolist()
        test_expr_cols = [col for col in test_cols if col not in gene_info_cols and 'call' not in col.lower()]

        # Extract first sample
        X_test = test_df[test_expr_cols].T
        sample_data = X_test.iloc[0].values.tolist()

        # Get true label
        test_labels = labels_df[labels_df['patient'] > 38].copy()
        true_label = test_labels.iloc[0]['cancer']

        return JSONResponse(content={
            "gene_expressions": sample_data,
            "true_label": true_label,
            "num_genes": len(sample_data)
        })

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error loading sample data: {str(e)}")


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "model_loaded": True}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

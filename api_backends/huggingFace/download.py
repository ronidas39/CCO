from fastapi import FastAPI, HTTPException
from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline
import os
import shutil
from pathlib import Path

app = FastAPI()

# Directory where models are stored
MODEL_DIR = Path("./local_models")
MODEL_DIR.mkdir(parents=True, exist_ok=True)

@app.get("/")
def home():
    return {"message": "FastAPI Hugging Face Model Manager"}

# 1️⃣ **Download a Model**
@app.post("/download/")
def download_model(model_name: str):
    """
    Downloads a model from Hugging Face and saves it locally.
    """
    try:
        model_path = MODEL_DIR / model_name
        if model_path.exists():
            return {"message": f"Model '{model_name}' already exists locally."}
        
        # Download the model and tokenizer
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForSequenceClassification.from_pretrained(model_name)

        # Save to local storage
        tokenizer.save_pretrained(model_path)
        model.save_pretrained(model_path)

        return {"message": f"Model '{model_name}' downloaded and saved successfully!"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 2️⃣ **List Available Local Models**
@app.get("/models/")
def list_models():
    """
    Lists all locally downloaded Hugging Face models.
    """
    models = [str(m.name) for m in MODEL_DIR.iterdir() if m.is_dir()]
    return {"available_models": models}


# 3️⃣ **Load a Local Model and Run Inference**
@app.post("/infer/")
def infer_text(model_name: str, text: str):
    """
    Loads a locally stored model and runs inference.
    """
    try:
        model_path = MODEL_DIR / model_name
        if not model_path.exists():
            raise HTTPException(status_code=404, detail=f"Model '{model_name}' not found locally.")

        # Load the model and tokenizer
        tokenizer = AutoTokenizer.from_pretrained(model_path)
        model = AutoModelForSequenceClassification.from_pretrained(model_path)

        # Run inference
        classifier = pipeline("text-classification", model=model, tokenizer=tokenizer)
        result = classifier(text)

        return {"model": model_name, "input_text": text, "prediction": result}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 4️⃣ **Delete a Local Model**
@app.delete("/delete/")
def delete_model(model_name: str):
    """
    Deletes a locally stored Hugging Face model.
    """
    try:
        model_path = MODEL_DIR / model_name
        if not model_path.exists():
            raise HTTPException(status_code=404, detail=f"Model '{model_name}' not found locally.")

        shutil.rmtree(model_path)
        return {"message": f"Model '{model_name}' deleted successfully."}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

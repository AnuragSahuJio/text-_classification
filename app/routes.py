from pydantic import BaseModel

from fastapi import APIRouter, HTTPException

from model.predict import ModelPredictor

from model.monitor import monitor_prediction_time


class TextInput(BaseModel):

    text: str


router = APIRouter()

predictor = ModelPredictor("model/svm_model.pkl")

monitor = monitor_prediction_time()


@router.post("/predict/")

@monitor

def predict(input_data: TextInput):

    try:

        result = predictor.predict(input_data.text)

        return {"status": "success", "data": result}

    except Exception as e:

        raise HTTPException(status_code=500, detail=str(e))


from fastapi import APIRouter , HTTPException
import numpy as np 
import pandas as pd
from fastapi.responses import JSONResponse

from api.schema import UserInput
from core.transformer import user_to_model_input
from core.predictor import price_predictor , MODEL_VERSION

router = APIRouter()

# just to make sure our API is working properly 
@router.get("/")
def home():
    return JSONResponse(content={"message":"RealEstate AI API"})


# aws , kubernetes etc services hit this health url to check whether our api is working 
# or not , it is a mandatory endpoint before deploying apis on these services
@router.get("/health")
def health_check():
    return JSONResponse(content={"status":"OK" , 
                                 "version":MODEL_VERSION})


@router.post("/predict")
def predict_price(data : UserInput):
    model_input = user_to_model_input(data)
    model_input = pd.DataFrame([model_input])

    predicted_price = price_predictor(model_input)
    high = round(predicted_price+0.33,2)
    low = round(predicted_price-0.33,2)

    try:
        return JSONResponse(status_code=200 , content={
            "cost of property" : f"the estimated cost is between {low} and {high} crores.".strip()})
    
    except Exception as e:
        return JSONResponse(status_code=500,content=str(e))

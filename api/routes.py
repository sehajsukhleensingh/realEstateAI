from fastapi import APIRouter , HTTPException
import numpy as np 
import pandas as pd
from fastapi.responses import JSONResponse

from api.schema import UserInput , RecommenderInput
from core.transformer import user_to_model_input
from core.predictor import price_predictor , MODEL_VERSION
from core.predictor import recommender_system

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

@router.get('/properties')
def show_sectors():
    dt = pd.read_csv("src/data/final/flat-recomendations.csv")

    data = {}
    for i , x in dt.groupby("sector"):
        lis = []
        for idx , name in zip(x["flatName"].index , x["flatName"].values):
            lis.append({"id":idx,"flat Name":name})
        data[f"sector = {i}"] = lis

    try:
        return JSONResponse(status_code=200, content=data)
    
    except Exception as e:
        return JSONResponse(status_code=500,content=str(e))


@router.post("/recommend")
def recommender(index: RecommenderInput):
    
    try:
        dt = pd.read_csv("src/data/final/flat-recomendations.csv")
        flat_name = dt.iloc[index.id]["flatName"]
    except:
        return JSONResponse(status_code=404,content={"message":"failed to fetch the flatName"})
    
    try:
        result = recommender_system(flat_name,0.8,0.5,0.7)
        return JSONResponse(status_code=200,content={"recommended similar properties":result})
    
    except Exception as e:
        return JSONResponse(status_code=500,content=str(e))
    
@router.get("/analytics/sectorwise-price")
def sectorwise_price():
    try:
        dt = pd.read_csv('src/data/final/dataset-v6.csv')
        dt.drop(columns = 'Unnamed: 0' , inplace = True)
        latLong = pd.read_csv('src/data/final/latlong.csv')
    except:
        return JSONResponse(status_code=404,content={"message":"failed to fetch the dataset"})
    
    dt['pricePerSqft'] = round((dt['Y']*10000000)/dt['builtup'],2)
    latLong['sector'] = latLong['sector'].astype('int')

    temp = dt.merge(latLong,on='sector')
    
    temp['latitude'] = temp['coordinates'].str.replace('N','').str.replace('E','').str.replace('°','').str.split(',').str[0]
    temp['longitude'] = temp['coordinates'].str.replace('N','').str.replace('E','').str.replace('°','').str.split(',').str[1]

    temp.drop(columns = 'coordinates' , inplace = True)

    temp['latitude'] = temp['latitude'].astype('float')
    temp['longitude'] = temp['longitude'].astype('float')

    groupDt = temp.groupby('sector').mean()[['pricePerSqft','builtup','latitude','longitude']].reset_index()

    return groupDt.to_dict(orient="records")

@router.get("/analytics/area-v-price")
def area_price(flag : str):

    try:
        dt = pd.read_csv("src/data/final/dataset-v6.csv")
        dt.drop(columns='Unnamed: 0' , inplace = True)
    except:
        return JSONResponse(status_code=404,content={"message":"failed to fetch the dataset"})

    if flag == "flat":
        df = dt[dt['propertyType'] == 0.0]
        df = df[["builtup","Y"]].rename(columns={"builtup":"builtup area (in sq feet)","Y":"price (in crores)"})
    
    else:
        df = dt[dt['propertyType'] == 1.0]
        df = df[["builtup","Y"]].rename(columns={"builtup":"builtup area (in sq feet)","Y":"price (in crores)"})

    return df.to_dict(orient="records")


@router.get("/analytics/average-bedrooms")
def average_bedrooms(flag :str = "overall"):
    try:
        dt = pd.read_csv("src/data/final/dataset-v6.csv")
        dt.drop(columns="Unnamed: 0", inplace = True)
    except:
        return JSONResponse(status_code=404,content={"message":"failed to fetch the dataset"})
    
    if flag == "flat":
        df = dt[dt["propertyType"] == 0.0]
       
    elif flag == "independent house":
        df = dt[dt["propertyType"] == 1.0]
       
    else:
        df = dt[["propertyType","bedRooms"]]
       
    avg_bedrooms = df["bedRooms"].value_counts().sort_index().to_dict()

    return avg_bedrooms


@router.get("/analytics/average-price-bhk")
def average_price_bhk():
    try:
        dt = pd.read_csv("src/data/final/dataset-v6.csv")
        dt.drop(columns="Unnamed: 0", inplace = True)

    except:
        return JSONResponse(status_code=404,content={"message":"failed to fetch the dataset"})
    
    df = dt[["Y","bedRooms"]]
    df = df[df["bedRooms"] <= 6]

    return df.to_dict()

@router.get("/analytics/prices-range")
def price_ranges_wrt_property():
    try:
        dt = pd.read_csv("src/data/final/dataset-v6.csv")
        dt.drop(columns="Unnamed: 0" , inplace=True)

    except:
        return JSONResponse(status_code=404,content={"message":"failed to fetch the dataset"})
    
    flats = dt[dt['propertyType']==0.0]['Y'].to_list()
    houses = dt[dt['propertyType']==1.0]['Y'].to_list()
    
    return {"flats":flats,"houses":houses}

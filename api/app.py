from fastapi import FastAPI
from api.routes import router

app = FastAPI(
    title = "RealEstate AI (price prediction , insights , analytics and recommender system)" ,
    version = "1.0"
)

app.include_router(router)


from pydantic import BaseModel,Field
from typing import Literal,Annotated

from api.schema import ( UserInput ,  ModelInput )
from core.config import ( 
    P_AGE_MAP , P_HEIGHT_MAP , P_LUX_MAP , P_TYPE_MAP , P_UTITLITY_MAP , P_BALCONY_MAP)   
 

def user_to_model_input(user:UserInput) -> ModelInput:

    """
    This func inputs the data from user 
    and 
    converts the data into the model friendly format for the prediction 
    returns the pydantic object of it 
    """

    input = ModelInput(
        sector=user.sector,
        propertyType=P_TYPE_MAP[user.propertyType],
        builtup=user.builtup,
        bedRooms=float(user.bedRooms),
        bathRooms=float(user.bathRooms) ,
        agePossesion=P_AGE_MAP[user.agePosseesion] ,
        balcony=P_BALCONY_MAP[user.balcony],
        pooja=P_UTITLITY_MAP[user.pooja],
        servant=P_UTITLITY_MAP[user.servant],
        study=P_UTITLITY_MAP[user.study],
        others=P_UTITLITY_MAP[user.other],
        store=P_UTITLITY_MAP[user.store],
        luxCat=P_LUX_MAP[user.lux],
        heightCat=P_HEIGHT_MAP[user.height]
    )
    return input.model_dump(by_alias=True)

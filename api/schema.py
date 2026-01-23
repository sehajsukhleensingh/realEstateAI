from pydantic import BaseModel , Field
from typing import Annotated , Literal 

class UserInput(BaseModel):
    sector : Annotated[
    int , 
    Field(..., gt=0 ,description="the sector of the property (Gurgaon)")
    ]
    propertyType : Annotated[
    Literal[
        'Flat' , 
        'Independent House'
        ] ,
    Field(...,description= "The type of property you want to infer about : house of flat")
    ]
    builtup : Annotated[
    float , 
    Field(..., gt=0 ,description="the area of the property in sq. meters")
    ]
    bedRooms : Annotated[
    int , 
    Field(..., gt=0 , description="the number of bedrooms you want in property")
    ]
    bathRooms : Annotated[
    int , 
    Field(..., gt=0 ,description="the number of bathrooms requried in property")
    ]
    agePosseesion : Annotated[
    Literal[
        'new property',
        'relatively new property',
        'old property',
        'moderately old property',
        'under construction'
        ] , 
    Field(...,description="the age of the property")
    ]
    balcony : Annotated[
    Literal[
        0,
        1,
        2,
        3,
        '3+'
        ] , 
    Field(...,description="the number of balcony required in the property ")
    ]
    pooja : Annotated[
    Literal[
        "yes",
        "no"
        ] , 
    Field(...,description="if you require the pooja room in property ")
    ]
    servant : Annotated[
    Literal[
        "yes",
        "no"
        ] , 
    Field(...,description="if you require the servant room in property ")
    ]
    study : Annotated[
    Literal[
        "yes",
        "no"
        ] , 
    Field(...,description="if you require the study room in property ")
    ]
    store : Annotated[
    Literal[
        "yes",
        "no"
        ] , 
    Field(...,description="if you require the store room in property ")
    ]
    other : Annotated[
    Literal[
        "yes",
        "no"
        ] , 
    Field(...,description="if you require the any other type of surplus room in property ")
    ]
    lux : Annotated[
    Literal[
        'Budget' ,
        'Semi Luxurious',
        'Luxurious' 
        ] , 
    Field(...,description="the luxury category of the proprty ,how much extend of luxury you " \
    "require in property , Budget = Basic amenities , Semi Luxurious = has cinema room , sauna ,"
    " and central air conditioning system , Luxurious = Top end category in a property  ")
    ]
    height : Annotated[
    Literal[
        'Low Rise' , 
        'Mid Rise' , 
        'High Rise'
        ], 
    Field(..., description="height preference of the property")
    ]

class ModelInput(BaseModel):

    sector:int
    propertyType:float	
    builtup:float	
    bedRooms:float	
    bathRooms:float	
    agePossesion:float	
    balcony:float	
    pooja:Annotated[int,Field(alias="pooja room")]
    servant:Annotated[int,Field(alias = "servant room")]
    study:Annotated[int,Field(alias = "study room")]	
    others:int
    store:Annotated[int,Field(alias = "store room")]
    luxCat:float
    heightCat:float	
	
    model_config = {"populate_by_name":True}


class RecommenderInput(BaseModel):

    id:Annotated[
        int,
        Field(...,gt=-1,description="Enter the id number of flat to whom " \
    "similar properties you want to view" , examples=[134,151]) 
    ]


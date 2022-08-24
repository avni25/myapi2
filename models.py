from pydantic import BaseModel

class Flight(BaseModel):
    id: int
    flightno: str
    callsign = ""
    registration: str
    bodytype: str  


class Aircraft(BaseModel):
    name: str
    wingspan: float
    length: float
    weight: int = 0
    



    
    

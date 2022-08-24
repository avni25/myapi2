import string
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from typing import Union
from pydantic import BaseModel
from models import Flight, Aircraft
from mydb import DB

db = DB()
db.connect()


app = FastAPI()

flights = [
            {"id": 2, "flightno": "THY456", "registration": "TCJAL", "bodytype": "A333"},
            {"id": 3, "flightno": "AZV4874", "registration": "DEDLY", "bodytype": "B752"}
            ]

@app.get("/")
def root():
    return {"message": "welcome to the root"}


@app.get("/flights")
def get_posts():
    return {"data": flights}

@app.post("/create", status_code=status.HTTP_201_CREATED)
def createpost(newflight: Flight):
    print(newflight.dict())
    flights.append(newflight.dict())
    return {"data": newflight}


@app.get("/flights/{id}")
def get_flight(id: int):
    print(type(id))
    for flight in flights:
        if flight["id"] == int(id):
            return flight
    else:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail = "id is not found!!!")
        

@app.delete("/flights/{id}", status_code = status.HTTP_204_NO_CONTENT)
def removeflight(id: int):
    for flight in flights:
        if flight["id"] == int(id):
            flights.remove(flight)
            return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail = "id is not found!!!")


@app.put("/flights/{id}")
def updateflight(id: int, flight: Flight):
    print(flight.dict())
    for i in range(len(flights)):
        if flights[i]["id"] == int(id):
            flights[i] = flight.dict()
            return Response(status_code=status.HTTP_202_ACCEPTED)
    else:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail = "id is not found!!!")


























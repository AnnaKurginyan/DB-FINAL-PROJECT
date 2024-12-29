from pydantic import BaseModel
from typing import List, Optional
from datetime import date


class ShipBase(BaseModel):
    id: int
    name: str
    ship_type: Optional[str] = None
    captain: Optional[str] = None
    home_port: Optional[int] = None  
    water_displacement: Optional[int] = None


class PortBase(BaseModel):
    id: int
    daily_price: Optional[int] = None
    category: Optional[str] = None
    name: str
    country: str


class VisitBase(BaseModel):
    id: int
    purpose: Optional[str] = None
    arrival: date
    departure: date
    dock: Optional[int] = None
    ship_id: int 
    port_id: int 


class ShipDetail(ShipBase):
    port: Optional[PortBase] = None  
    visits: List["VisitBase"] = []   


class PortDetail(PortBase):
    ships: List["ShipBase"] = []  
    visits: List["VisitBase"] = []  


class VisitDetail(VisitBase):
    ship: Optional[ShipBase] = None  
    port: Optional[PortBase] = None  


from pydantic import BaseModel
from typing import Optional, List
from datetime import date

class ShipBase(BaseModel):
    name: str
    ship_type: Optional[str]
    captain: Optional[str]
    home_port: Optional[int]
    water_displacement: Optional[int]

class ShipCreate(ShipBase):
    pass

class ShipDetail(ShipBase):
    id: int
    class Config:
        orm_mode = True

class PortBase(BaseModel):
    name: str
    country: str
    daily_price: Optional[int]
    category: Optional[str]

class PortCreate(PortBase):
    pass

class PortDetail(PortBase):
    id: int
    class Config:
        orm_mode = True

class VisitBase(BaseModel):
    purpose: Optional[str]
    arrival: date
    departure: date
    dock: Optional[int]
    ship_id: int
    port_id: int

class VisitCreate(VisitBase):
    pass

class VisitDetail(VisitBase):
    id: int
    class Config:
        orm_mode = True


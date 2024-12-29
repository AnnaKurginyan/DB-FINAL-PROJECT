from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
# from database import engine, Base, get_db
from crud import Ship, Port, Visit
from schemas import ShipCreate, ShipDetail, PortCreate, PortDetail, VisitCreate, VisitDetail

app = FastAPI()


Base.metadata.create_all(bind=engine)


@app.post("/ships/", response_model=ShipDetail)
def create_ship(ship: ShipCreate, db: Session = Depends(get_db)):
    db_ship = Ship(**ship.dict())
    db.add(db_ship)
    db.commit()
    db.refresh(db_ship)
    return db_ship

@app.get("/ships/{ship_id}", response_model=ShipDetail)
def get_ship(ship_id: int, db: Session = Depends(get_db)):
    db_ship = db.query(Ship).filter(Ship.id == ship_id).first()
    if not db_ship:
        raise HTTPException(status_code=404, detail="Ship not found")
    return db_ship

@app.put("/ships/{ship_id}", response_model=ShipDetail)
def update_ship(ship_id: int, ship: ShipCreate, db: Session = Depends(get_db)):
    db_ship = db.query(Ship).filter(Ship.id == ship_id).first()
    if not db_ship:
        raise HTTPException(status_code=404, detail="Ship not found")
    for key, value in ship.dict().items():
        setattr(db_ship, key, value)
    db.commit()
    db.refresh(db_ship)
    return db_ship

@app.delete("/ships/{ship_id}")
def delete_ship(ship_id: int, db: Session = Depends(get_db)):
    db_ship = db.query(Ship).filter(Ship.id == ship_id).first()
    if not db_ship:
        raise HTTPException(status_code=404, detail="Ship not found")
    db.delete(db_ship)
    db.commit()
    return {"message": "Ship deleted successfully"}


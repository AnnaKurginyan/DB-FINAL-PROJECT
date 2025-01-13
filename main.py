from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from sqlalchemy import func, desc
from database import get_db
from sqlalchemy import select
from def_tables import Ship, Port, Visit
from schemas import ShipCreate, ShipDetail, PortCreate, PortDetail, VisitCreate, VisitDetail

app = FastAPI()

@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")

# SHIP
@app.post("/ships/", response_model=ShipDetail)
def create_ship(ship: ShipCreate, db: Session = Depends(get_db)):
    db_ship = Ship(**ship.model_dump())
    db.add(db_ship)
    db.commit()
    db.refresh(db_ship)
    return db_ship

@app.get("/ships/", response_model=list[ShipDetail])
def get_ship(db: Session = Depends(get_db), ship_id: int = None, water_displacement: int = None, page: int = 1, limit: int = 10):
    db_ship = select(Ship).limit(limit).offset((page - 1) * limit)

    if ship_id:
        db_ship = db_ship.where(Ship.id == ship_id)
    if water_displacement:
        db_ship = db_ship.where(Ship.water_displacement >= water_displacement)
   
    return db.execute(db_ship).scalars().all()

@app.put("/ships/{ship_id}", response_model=ShipDetail)
def update_ship(ship_id: int, ship: ShipCreate, db: Session = Depends(get_db)):
    db_ship = db.query(Ship).filter(Ship.id == ship_id).first()
    if not db_ship:
        raise HTTPException(status_code=404, detail="Корабль не найден")
    for key, value in ship.dict().items():
        setattr(db_ship, key, value)
    db.commit()
    db.refresh(db_ship)
    return db_ship

@app.delete("/ships/{ship_id}")
def delete_ship(ship_id: int, db: Session = Depends(get_db)):
    db_ship = db.query(Ship).filter(Ship.id == ship_id).first()
    if not db_ship:
        raise HTTPException(status_code=404, detail="Корабль не найден")
    db.delete(db_ship)
    db.commit()
    return {"message": "Данные о корабле удалены"}


# PORT
@app.post("/ports/", response_model=PortDetail)
def create_port(port: PortCreate, db: Session = Depends(get_db)):
    db_port = Port(**port.dict())
    db.add(db_port)
    db.commit()
    db.refresh(db_port)
    return db_port

@app.get("/ports/{port_id}", response_model=PortDetail)
def get_port(port_id: int, db: Session = Depends(get_db)):
    db_port = db.query(Port).filter(Port.id == port_id).first()
    if not db_port:
        raise HTTPException(status_code=404, detail="Нет информации о запрашиваемом порте")
    return db_port

@app.put("/ports/{port_id}", response_model=PortDetail)
def update_port(port_id: int, port: PortCreate, db: Session = Depends(get_db)):
    db_port = db.query(Port).filter(Port.id == port_id).first()
    if not db_port:
        raise HTTPException(status_code=404, detail="Нет информации о запрашиваемом порте")
    for key, value in port.dict().items():
        setattr(db_port, key, value)
    db.commit()
    db.refresh(db_port)
    return db_port

@app.delete("/ports/{port_id}")
def delete_port(port_id: int, db: Session = Depends(get_db)):
    db_port = db.query(Port).filter(Port.id == port_id).first()
    if not db_port:
        raise HTTPException(status_code=404, detail="Нет информации о запрашиваемом порте")
    db.delete(db_port)
    db.commit()
    return {"message": "Информация о порте удалена"}


# VISIT
@app.post("/visits/", response_model=VisitDetail)
def create_visit(visit: VisitCreate, db: Session = Depends(get_db)):
    db_visit = Visit(**visit.dict())
    db.add(db_visit)
    db.commit()
    db.refresh(db_visit)
    return db_visit

@app.get("/visits/{visit_id}", response_model=VisitDetail)
def get_visit(visit_id: int, db: Session = Depends(get_db)):
    db_visit = db.query(Visit).filter(Visit.id == visit_id).first()
    if not db_visit:
        raise HTTPException(status_code=404, detail="Нет информации о посещении")
    return db_visit

@app.put("/visits/{visit_id}", response_model=VisitDetail)
def update_visit(visit_id: int, visit: VisitCreate, db: Session = Depends(get_db)):
    db_visit = db.query(Visit).filter(Visit.id == visit_id).first()
    if not db_visit:
        raise HTTPException(status_code=404, detail="Нет информации о посещении")
    for key, value in visit.dict().items():
        setattr(db_visit, key, value)
    db.commit()
    db.refresh(db_visit)
    return db_visit

@app.delete("/visits/{visit_id}")
def delete_visit(visit_id: int, db: Session = Depends(get_db)):
    db_visit = db.query(Visit).filter(Visit.id == visit_id).first()
    if not db_visit:
        raise HTTPException(status_code=404, detail="Нет информации о посещении")
    db.delete(db_visit)
    db.commit()
    return {"message": "Информация о посещении удалена"}


# select where
@app.get("/ships/filter/")
def get_ships_by_conditions(port_id: int, min_displacement: int, db: Session = Depends(get_db)):
    return db.query(Ship).filter(
        Ship.home_port == port_id, Ship.water_displacement > min_displacement
    ).all()

# join
@app.get("/visits/details/")
def get_visit_details(db: Session = Depends(get_db)):
    return db.query(
        Visit.id, Visit.purpose, Ship.name.label("ship_name"), Port.name.label("port_name")
    ).join(Ship, Visit.ship_id == Ship.id).join(Port, Visit.port_id == Port.id).all()

# update
@app.put("/ships/update_home_port/")
def update_ships_home_port(old_port_id: int, new_port_id: int, db: Session = Depends(get_db)):
    updated = db.query(Ship).filter(Ship.home_port == old_port_id).update(
        {Ship.home_port: new_port_id}, synchronize_session="fetch"
    )
    db.commit()
    return {"updated_rows": updated}

# group by
@app.get("/ports/grouped_by_country/")
def get_ports_grouped_by_country(db: Session = Depends(get_db)):
    return db.query(
        Port.country, func.count(Port.id).label("port_count")
    ).group_by(Port.country).all()

# sorting
@app.get("/ships/sorted/")
def get_ships_sorted(order: str = "asc", db: Session = Depends(get_db)):
    if order.lower() == "desc":
        return db.query(Ship).order_by(desc(Ship.name)).all()
    return db.query(Ship).order_by(Ship.name).all()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8080)
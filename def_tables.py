from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class Ship(Base):
    __tablename__ = 'ship'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    ship_type = Column(String(100))
    captain = Column(String(100))
    home_port = Column(Integer, ForeignKey('port.id'))  
    water_displacement = Column(Integer)

    port = relationship("Port", back_populates="ships")
    visits = relationship("Visit", back_populates="ship")



class Port(Base):
    __tablename__ = 'port'

    id = Column(Integer, primary_key=True, index=True)
    daily_price = Column(Integer)
    category = Column(String(100))
    name = Column(String(100))
    country = Column(String(100))

    ships = relationship("Ship", back_populates="port")
    visits = relationship("Visit", back_populates="port")


    
class Visit(Base):
    __tablename__ = 'visit'
    
    id = Column(Integer, primary_key=True, index=True)
    purpose = Column(String(100))
    arrival = Column(Date)
    departure = Column(Date)
    dock = Column(Integer)
    
    ship_id = Column(Integer, ForeignKey('ship.id')) 
    port_id = Column(Integer, ForeignKey('port.id')) 
    
    ship = relationship("Ship", back_populates="visits")
    port = relationship("Port", back_populates="visits")
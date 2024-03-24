import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Country(Base):
    __tablename__="country"
    ID = Column(Integer, primary_key=True)
    name = Column(String(20))

class User(Base):
    __tablename__="user"
    ID = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    country = Column(Integer, ForeignKey("country.ID"))
    country_relationship = relationship(Country)
    email = Column(String(50), unique=True)
    password = Column(String(30))

class Character(Base):
    __tablename__="character"
    ID = Column(Integer, primary_key=True)
    name = Column(String(20), unique=True)
    height= Column(Integer)
    mass=Column(Integer)

class Planet(Base):
    __tablename__="palnet"
    ID = Column(Integer, primary_key=True)
    name = Column(String(20), unique=True)

class Vehicle(Base):
    __tablename__="vehicle"
    ID = Column(Integer, primary_key=True)
    model = Column(String(20), unique=True)


class FavoriteCharacter(Base):
    __tablename__="favorite_characters"
    ID = Column(Integer, primary_key=True)
    user_id=Column(Integer, ForeignKey("user.ID"))
    user_relationship=relationship (User)
    character_id=Column(Integer, ForeignKey("character.ID"))
    character_relationship=relationship (Character)

class FavoritePlanet(Base):
    __tablename__="favorite_planets"
    ID = Column(Integer, primary_key=True)
    user_id=Column(Integer, ForeignKey("user.ID"))
    user_relationship=relationship(User)
    planet_id=Column(Integer, ForeignKey ("palnet.ID"))
    planet_relationship=relationship (Planet) 

class FavoriteVehicle(Base):
    __tablename__="favorite_vehicles"
    ID = Column(Integer, primary_key=True)
    user_id=Column(Integer, ForeignKey("user.ID"))
    user_relationship=relationship(User)
    vehicle_id=Column(Integer, ForeignKey("vehicle.ID"))   
    vehicle_relationship=relationship (Vehicle) 



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

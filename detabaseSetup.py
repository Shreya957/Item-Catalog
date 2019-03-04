import os
import sys
import datetime

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base= declarative_base()

class User(Base):

  __tablename__= 'user'
  
  name= Column(String(80), nullable = False)
  id = Column(Integer , primary_key = True)
  email = Column(String(80), nullable = False)
  picture = Column(String(250))

class Category(Base):

  __tablename__ = 'category'

  name= Column(String(80), nullable = False)
  id = Column(Integer , primary_key = True)

class Item(Base):

  __tablename__ = 'item'

  name= Column(String(80), nullable = False)
  id = Column(Integer , primary_key = True)
  description = Column(String(250))
  creation_date = Column(DateTime, default=datetime.datetime.utcnow)
  cat_id = Column(Integer, ForeignKey('category.id'))
  #user_id = Column(Integer, ForeignKey('user.id'))
  category = relationship(Category)
  #user = relationship(User)
  
  

engine = create_engine('sqlite:///CatalogApplication.db')

Base.metadata.create_all(engine)
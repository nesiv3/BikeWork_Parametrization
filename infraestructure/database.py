import os 
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from dotenv import load_dotenv

# Cargar variables de ent
load_dotenv()

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class CatalogORM(Base):
    __tablename__ = "catalog"
    identity = Column(String(10), primary_key=True)
    description = Column(String(255), nullable=False)
    active = Column(Boolean, default=True)

class CatalogDataORM(Base):
    __tablename__ = "catalog_data"
    identity = Column(String(10), primary_key=True)
    catalog_identity = Column(String(100), ForeignKey("catalog.identity"), nullable=False)
    name = Column(String(255), nullable=False)
    description = Column(String(255))
    order = Column(Integer)
    active = Column(Boolean, default=True)

class DisabledDateORM(Base):
    __tablename__ = "disabled_dates"
    id = Column(Integer, primary_key=True, autoincrement=True)
    the_date = Column(String(10), unique=True, nullable=False)
    reason = Column(String(100), nullable=False)
    created_at = Column(String(50))
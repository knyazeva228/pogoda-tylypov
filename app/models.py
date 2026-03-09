from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, relationship
from datetime import datetime

class Base(AsyncAttrs, DeclarativeBase):
    pass

class APIKey(Base):
    __tablename__ = "api_keys"
    id = Column(Integer, primary_key=True, autoincrement=True)
    key = Column(String(64), unique=True, nullable=False, index=True)
    name = Column(String(100))
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    subscriptions = relationship("Subscription", back_populates="api_key")

class Subscription(Base):
    __tablename__ = "subscriptions"
    id = Column(Integer, primary_key=True, autoincrement=True)
    api_key_id = Column(Integer, ForeignKey("api_keys.id"), nullable=False)
    webhook_url = Column(String(500), nullable=False)
    trigger_type = Column(String(50))
    trigger_value = Column(Float, nullable=True)
    location_lat = Column(Float, nullable=False)
    location_lon = Column(Float, nullable=False)
    location_name = Column(String(200))
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    last_triggered_at = Column(DateTime, nullable=True)

    api_key = relationship("APIKey", back_populates="subscriptions")
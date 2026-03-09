from pydantic import BaseModel, HttpUrl
from typing import Optional, List
from datetime import datetime

class APIKeyCreate(BaseModel):
    name: Optional[str] = None

class APIKeyOut(BaseModel):
    id: int
    key: str
    name: Optional[str]
    is_active: bool
    created_at: datetime

class SubscriptionBase(BaseModel):
    webhook_url: HttpUrl
    trigger_type: str
    trigger_value: Optional[float] = None
    location_lat: float
    location_lon: float
    location_name: Optional[str] = None

class SubscriptionCreate(SubscriptionBase):
    pass

class SubscriptionOut(SubscriptionBase):
    id: int
    api_key_id: int
    is_active: bool
    created_at: datetime
    last_triggered_at: Optional[datetime]

class WeatherCurrent(BaseModel):
    temperature: float
    windspeed: float
    weathercode: int
    time: datetime

class WeatherForecast(BaseModel):
    daily: List[dict]

class GeocodeResult(BaseModel):
    lat: float
    lon: float
    display_name: str

class AirQuality(BaseModel):
    aqi: Optional[int]
    pm10: Optional[float]
    pm25: Optional[float]
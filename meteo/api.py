#Accès à l’API Open-Meteo (https://open-meteo.com)
from __future__ import annotations
from typing import List
import requests

BASE_URL = "https://api.open-meteo.com/v1/forecast"

def get_daily_max_temps(lat: float, lon: float, days: int = 7, timeout: int = 10) -> List[float]:
    # Retourne la liste des températures max journalières sur `days` jours
    params = {
        "latitude": lat,
        "longitude": lon,
        "daily": "temperature_2m_max",
        "timezone": "auto",
        "forecast_days": days,
    }
    resp = requests.get(BASE_URL, params=params, timeout=timeout)
    resp.raise_for_status()
    data = resp.json()
    return data["daily"]["temperature_2m_max"]

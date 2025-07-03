# Analyse basique des températures.
from __future__ import annotations
from statistics import mean
from typing import List, Dict

def analyse_temperatures(temps: List[float]) -> Dict[str, float]:
    #Renvoie dict(min, max, moyenne)
    if not temps:
        raise ValueError("Liste de températures vide")
    return {
        "min": min(temps), 
        "max": max(temps), 
        "moyenne": mean(temps)
        }

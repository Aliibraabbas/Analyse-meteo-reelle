#Sauvegarde et chargement JSON
from __future__ import annotations
import json
from pathlib import Path
from typing import List, Dict

def save_to_json(
        path: str | Path, 
        data: List[float], 
        analysis: Dict[str, float],
        ) -> None:
    content = {"donnees": data, "analyse": analysis}
    Path(path).write_text(
        json.dumps(content, indent=2, ensure_ascii=False), encoding="utf-8"
        )

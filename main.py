# Récupère, analyse, sauvegarde & trace la météo de Paris sur 7 jours
from pathlib import Path
from meteo import (
    get_daily_max_temps,
    analyse_temperatures,
    save_to_json,
    plot_temperatures,
)

LAT, LON = 48.85, 2.35
OUT_JSON = Path("meteo.json")
OUT_PLOT = Path("plot.png")

def run() -> None:
    print("→ Appel API Open-Meteo…")
    temps = get_daily_max_temps(LAT, LON)

    print("→ Analyse…")
    stats = analyse_temperatures(temps)

    print(f"→ Sauvegarde JSON → {OUT_JSON}")
    save_to_json(OUT_JSON, temps, stats)

    print(f"→ Génération du graphique → {OUT_PLOT}")
    plot_temperatures(temps, OUT_PLOT)

    print("Terminé ✔")

if __name__ == "__main__":
    run()

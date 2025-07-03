#Courbe des températures avec matplotlib
from __future__ import annotations
from typing import List
import matplotlib.pyplot as plt

def plot_temperatures(temps: List[float], path: str | None = "plot.png") -> None:
    jours = range(1, len(temps) + 1)
    plt.figure()
    plt.plot(jours, temps, marker="o")
    plt.title("Températures max sur 7 jours")
    plt.xlabel("Jour")
    plt.ylabel("Température (°C)")
    plt.xticks(jours, [f"Jour {j}" for j in jours])
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(path, dpi=150)
    plt.close()

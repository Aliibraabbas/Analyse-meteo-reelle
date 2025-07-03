import sys, pathlib
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))
import pytest
from meteo.analyse import analyse_temperatures
from meteo.api import get_daily_max_temps


def test_analyse_temperatures_unit():
    res = analyse_temperatures([25.0, 30.0, 27.5])
    assert res["max"] == 30.0
    assert res["min"] == 25.0
    assert res["moyenne"] == pytest.approx(27.5)

def test_analyse_temperatures_liste_vide():
    with pytest.raises(ValueError):
        analyse_temperatures([])

def test_integration_api_analyse():
    t = get_daily_max_temps(48.85, 2.35, days=3)
    assert len(t) == 3
    stats = analyse_temperatures(t)
    assert stats["max"] >= stats["min"]

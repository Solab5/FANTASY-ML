from src.fplpipe.fpl_api import fetch_bootstrap, elements_table, teams_table
import pandas as pd

def test_bootstrap_shapes():
    boot = fetch_bootstrap()
    el = elements_table(boot)
    tm = teams_table(boot)
    assert {"id","web_name","now_cost"}.issubset(set(el.columns))
    assert {"id","name"}.issubset(set(tm.columns))
    assert len(el)>300 and len(tm)==20

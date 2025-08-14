import time, requests, pandas as pd
from typing import Dict, Any, List

BASE = "https://fantasy.premierleague.com/api"

def _get(url, retries=3, pause=0.5):
    for i in range(retries):
        r = requests.get(url, timeout=30)
        if r.status_code==200: return r.json()
        time.sleep(pause*(i+1))
    raise RuntimeError(f"GET failed: {url}")

def fetch_bootstrap() -> Dict[str, Any]:
    return _get(f"{BASE}/bootstrap-static/")

def fetch_fixtures() -> pd.DataFrame:
    js = _get(f"{BASE}/fixtures/")
    return pd.DataFrame(js)

def fetch_event_live(event_id:int) -> Dict[str, Any]:
    return _get(f"{BASE}/event/{event_id}/live/")

def elements_table(bootstrap:Dict[str,Any]) -> pd.DataFrame:
    df = pd.DataFrame(bootstrap["elements"])
    keep = ["id","first_name","second_name","web_name","team","now_cost","element_type",
            "minutes","goals_scored","assists","clean_sheets","goals_conceded",
            "yellow_cards","red_cards","bps","selected_by_percent","status","chance_of_playing_next_round",
            "influence","creativity","threat","ict_index","value_season","form","points_per_game","total_points"]
    return df[keep]

def teams_table(bootstrap:Dict[str,Any]) -> pd.DataFrame:
    return pd.DataFrame(bootstrap["teams"])[["id","name","strength_overall_home","strength_overall_away","strength_attack_home","strength_attack_away","strength_defence_home","strength_defence_away"]]

def element_types_table(bootstrap:Dict[str,Any]) -> pd.DataFrame:
    return pd.DataFrame(bootstrap["element_types"])[["id","singular_name_short","squad_select","squad_min_play","squad_max_play"]]

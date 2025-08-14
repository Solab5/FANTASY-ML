from .fpl_api import fetch_bootstrap, fetch_fixtures, elements_table, teams_table, element_types_table
from .cache import save_json, save_parquet, dated_tag

def run_update():
    boot = fetch_bootstrap()
    fix = fetch_fixtures()
    save_json(boot, dated_tag("bootstrap"))
    save_parquet(fix, dated_tag("fixtures"))

    el = elements_table(boot)
    tm = teams_table(boot)
    et = element_types_table(boot)
    save_parquet(el, dated_tag("elements"))
    save_parquet(tm, dated_tag("teams"))
    save_parquet(et, dated_tag("element_types"))

if __name__=="__main__":
    run_update()

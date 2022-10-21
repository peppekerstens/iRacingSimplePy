#https://www.alpharithms.com/tabulate-json-data-python-pandas-262811/
import json
import pandas as pd 

#json consists of an overview with sub-data
"""
subsession_id             : 43720351
season_id                 : 3477
season_name               : BMW 12.0 Challenge - 2022 Season 1 - Fixed
season_short_name         : 2022 Season 1
season_year               : 2022
season_quarter            : 1
series_id                 : 397
series_name               : BMW 12.0 Challenge - Fixed
series_short_name         : BMW 12.0 Challenge - Fixed
series_logo               : bmw12-logo.png
race_week_num             : 3
session_id                : 168309194
license_category_id       : 2
license_category          : Road
private_session_id        : -1
start_time                : 2022-01-07T13:30:00Z
end_time                  : 2022-01-07T14:00:24Z
num_laps_for_qual_average : 2
num_laps_for_solo_average : 5
corners_per_lap           : 10
caution_type              : 2
event_type                : 5
event_type_name           : Race
driver_changes            : False
min_team_drivers          : 1
max_team_drivers          : 1
driver_change_rule        : 0
driver_change_param1      : -1
driver_change_param2      : -1
max_weeks                 : 12
points_type               : race
event_strength_of_field   : 2029
event_laps_complete       : 8
num_cautions              : 0
num_caution_laps          : 0
num_lead_changes          : 0
official_session          : True
heat_info_id              : -1
special_event_type        : -1
damage_model              : 0
can_protest               : False
cooldown_minutes          : 0
limit_minutes             : 0
track                     : @{track_id=199; track_name=Circuit Zolder; config_name=Grand Prix; category_id=2; category=Road}
weather                   : @{version=0; type=3; temp_units=0; temp_value=78; rel_humidity=55; fog=0; wind_dir=0; wind_units=0; wind_value=2; skies=1; weather_var_initial=0; weather_var_ongoing=0; a 
                            llow_fog=False; track_water=0; precip_option=0; time_of_day=0; simulated_start_utc_time=2022-04-01T12:15:00Z; simulated_start_utc_offset=120}
track_state               : @{leave_marbles=False; practice_rubber=-1; qualify_rubber=-1; warmup_rubber=-1; race_rubber=-1; practice_grip_compound=-1; qualify_grip_compound=-1; warmup_grip_compound= 
                            -1; race_grip_compound=-1}
                            ber=-1; simsession_type=4; simsession_type_name=Lone Qualifying; simsession_subtype=0; simsession_name=QUALIFY; results=System.Object[]}, @{simsession_number=0; simsessio 
                            n_type=6; simsession_type_name=Race; simsession_subtype=0; simsession_name=RACE; results=System.Object[]}}
race_summary              : @{subsession_id=43720351; average_lap=971542; laps_complete=8; num_cautions=0; num_caution_laps=0; num_lead_changes=0; field_strength=2029; num_opt_laps=0; has_opt_path=F 
                            alse; special_event_type=0; special_event_type_text=Not a special event}
car_classes               : {@{car_class_id=2264; cars_in_class=System.Object[]; name=BMW M4 GT4; short_name=BMW M4 GT4}}
allowed_licenses          : {@{parent_id=397; license_group=1; min_license_level=4; max_license_level=4; group_name=Rookie}, @{parent_id=397; license_group=2; min_license_level=5; max_license_level= 
                            8; group_name=Class D}, @{parent_id=397; license_group=3; min_license_level=9; max_license_level=12; group_name=Class C}, @{parent_id=397; license_group=4; min_license_le 
                            vel=13; max_license_level=16; group_name=Class B}...}
results_restricted        : False
associated_subsession_ids : {43720351, 43720352}
"""

with open('result_43720351.json', 'r') as file:
    race_result = json.load(file)


"""
#moved from hostpool
@property
def active_session_hosts(self) -> List[SessionHost]:
    return [host for host in self.session_hosts if host.is_online]
"""


def get_session_results(race_result: json, type: str):
    for session_results in race_result.session_results:
        
    return [session_results.session_results for session_results in race_result if session_results.simsession_type_name == type]

session_results = get_session_results(race_result, 'race')

#df = pd.DataFrame.from_dict(json.load(file))
df = pd.json_normalize(json.load(file))

# print first 5 records via head() method
print(df.head())


with open('result_lap_data_43720351.json', 'r') as file:
    #df = pd.DataFrame.from_dict(json.load(file))
    df = pd.json_normalize(json.load(file))

# map a function to join all list items via a single ',' character
df = df.applymap(lambda x: ",".join(x) if type(x) is list else x)

# set the index to employee id
df.set_index(['lap_number'], inplace=True)

# print first 5 records via head() method
print(df.head())
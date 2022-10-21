import json
from iracingdataapi.client import irDataClient

#https://stackabuse.com/saving-text-json-and-csv-to-a-file-in-python/

idc = irDataClient(username='', password='')

#werkt nog niet?
def get_cars(idc: irDataClient):
    all_cars = idc.cars
    cars_assets = idc.get_cars_assets()
    carclass = idc.get_carclass()
    for car in all_cars:
        a = cars_assets[str(car["car_id"])]
        for key in a.keys():
            car[key] = a[key]

    return all_cars

def get_cars_and_tracks(idc: irDataClient):
    all_cars = idc.cars
    all_tracks = idc.tracks
    with open('all_tracks.json', 'w') as json_file:
        json.dump(all_tracks, json_file)
    with open('all_cars.json', 'w') as json_file:
        json.dump(all_cars, json_file)



def get_member_data(idc: irDataClient, custid: int):
    # get generic member information
    member_data = idc.member(cust_id=custid)

    # get generic member information
    member_chart_data = idc.member_chart_data(cust_id=custid)

    # get the summary data of a member
    member_summary = idc.stats_member_summary(cust_id=custid)

    # get latest race results of a member
    member_recent_races = idc.stats_member_recent_races(cust_id=custid)

    return {
        "member": member_data ,
        "summary": member_summary ,
        "chart": member_chart_data ,
        "recent": member_recent_races
    }

#all_members = idc.member()

#get_all_cars = get_cars(idc)
#all_cars = idc.cars
#cars_assets = idc.get_cars_assets()
#car_class = idc.get_carclass()

get_cars_and_tracks(idc)

drivers = idc.lookup_drivers("peppe")


custid = 662411

member_data = get_member_data(idc, custid)

with open(f'stats_member_recent_races_{custid}', 'w') as json_file:
    json.dump(member_recent_races, json_file)

# get all laps for a specific driver in a race
result_lap_data = idc.result_lap_data(subsession_id=43720351, cust_id=209179)

# get results from a session server
result = idc.result(subsession_id=43720351)


with open('result_lap_data_43720351.json', 'w') as json_file:
    json.dump(result_lap_data, json_file)



with open('result_43720351.json', 'w') as json_file:
    json.dump(result, json_file)

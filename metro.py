import requests
import json
import sys

def fetch_metro_times(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return []

def fetch_stations():
    url = "https://metro-rti.nexus.org.uk/api/stations"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching stations: {e}")
        return {}

def parse_metro_times(data):
    parsed_results = []
    for train in data:
        parsed_results.append({
            "Train Number": train.get("trn"),
            "Status": train.get("lastEvent"),
            "Last Location": train.get("lastEventLocation"),
            "Last Time": train.get("lastEventTime"),
            "Destination": train.get("destination"),
            "Due In (mins)": train.get("dueIn"),
            "Line": train.get("line"),
            "Scheduled Time": train.get("actualScheduledTime"),
            "Predicted Time": train.get("actualPredictedTime"),
        })
    return parsed_results

def print_metro_times(parsed_data, platform):
    print(f"\nPlatform {platform}:")
    print("=" * 50)
    for train in parsed_data:
        print(f"Train {train['Train Number']} ({train['Line']} Line) to {train['Destination']}")
        print(f"  Status: {train['Status']} at {train['Last Location']} ({train['Last Time']})")
        print(f"  Due in: {train['Due In (mins)']} minutes")
        print(f"  Scheduled: {train['Scheduled Time']} | Predicted: {train['Predicted Time']}")
        print("-" * 50)

def select_station(stations):
    print("Available Stations:")
    for code, name in stations.items():
        print(f"{code}: {name}")
    
    station_code = input("Enter station code: ").strip().upper()
    if station_code in stations:
        return station_code
    else:
        print("Invalid station code.")
        sys.exit(1)

if __name__ == "__main__":
    stations = fetch_stations()
    selected_station = select_station(stations)
    
    for platform in [1, 2]:
        url = f"https://metro-rti.nexus.org.uk/api/times/{selected_station}/{platform}"
        data = fetch_metro_times(url)
        parsed_data = parse_metro_times(data)
        print_metro_times(parsed_data, platform)

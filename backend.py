import requests

API = "186e408993e2bf9c3de8c2610e152a9a"


def get_data(place, days=None):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API}"
    response = requests.get(url)
    content = response.json()
    values = 8 * days
    filtered_data = content["list"]
    filtered_data = filtered_data[:values]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Tokyo", days=3, kind="Temperature"))

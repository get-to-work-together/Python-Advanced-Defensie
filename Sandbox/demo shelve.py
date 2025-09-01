import shelve
import requests


def get_data(city):

    # openweathermap api
    url = "http://api.openweathermap.org/data/2.5/forecast/daily"
    url += "?appid=d1526a9039658a6f76950cff21823aff"
    url += "&units=metric"
    url += "&mode=json"
    url += "&lang=nl"
    url += "&cnt=14"
    url += "&q=" + city

    print(url)

    r = requests.get(url)

    if r.status_code == 200:
        return r.json()

    else:
        raise Exception('No data retrieved')



if __name__ == '__main__':
    filename = 'shelve'

    city = input('Give city: ')

    with shelve.open(filename) as sh:
        if city in sh:
            data = sh[city]

        else:
            data = get_data(city)

    print(data)

    with shelve.open(filename) as sh:
        sh[city] = data

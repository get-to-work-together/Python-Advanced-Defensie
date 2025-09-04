import httpx
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

from datetime import datetime
import json
import locale

locale.setlocale(locale.LC_ALL, 'nl_nl')

st.title('My Streamlit Weather Station')

# city = input('Welke stad? : ')
city = st.text_input('Geef locatie:')

url =  "http://api.openweathermap.org/data/2.5/forecast/daily"
url += "?appid=d1526a9039658a6f76950cff21823aff"
url += "&units=metric"
url += "&mode=json"
url += "&cnt=14"
url += "&lang=nl"
url += "&q=" + city

response = httpx.get(url)

if response.status_code == 200:
    content = response.json()

    data = []
    for day_forecast in content['list']:
        data.append(dict(
            dd = datetime.fromtimestamp(day_forecast['dt']),
            min = day_forecast['temp']['min'],
            max = day_forecast['temp']['max'],
            day = day_forecast['temp']['day'],
            night = day_forecast['temp']['night'],
            weather = day_forecast['weather'][0]['description'],
        ))

    df = pd.DataFrame(data)

    st.dataframe(df)

    fig, ax = plt.subplots()
    ax.set_title(f'Voorspelling voor {city} voor de komende 2 weken')
    ax.grid()
    ax.fill_between(df['dd'], df['min'], df['max'], color='lightblue')
    ax.plot(df['dd'], df['day'], lw=2, label='Day')
    ax.plot(df['dd'], df['night'], lw=2, label='Night')
    ax.legend()

    # plt.show()
    st.pyplot(fig=fig)

    df_city = pd.DataFrame([content['city']['coord']])
    st.map(df_city, latitude='lat', longitude='lon')

else:
    print(f'Could not get data for {city}')


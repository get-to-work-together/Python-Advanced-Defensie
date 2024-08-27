from src.models.openweathermap.get_data import get_formatted_data

data = get_formatted_data('Soesterberg')

for day_forecast in data:
    print(day_forecast)
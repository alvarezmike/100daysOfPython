"""
You are going to use dictionary comprehension to create a
 dictionary called weather_f that takes each temperature in degrees Celcius and
 converts it into degrees Farenheit
"""

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}


# converts C to Farenheit
def to_f(weather):
    weather = weather * 9/5 + 32
    return weather


weather_f = {day: to_f(w) for (day, w) in weather_c.items()}
print(weather_f)



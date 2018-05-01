
def get_weather(location_name):
    internet_status = 0
    try:
        import httplib
    except:
        import http.client as httplib
    conn = httplib.HTTPConnection("www.google.com", timeout=5)
    try:
        conn.request("HEAD", "/")
        conn.close()
        internet_status = 1
    except:
        conn.close()
        print("ERROR: Internet access not available.")

    if internet_status == 1:
        from weather import Weather
        import matplotlib.pyplot as plt

        weather = Weather(unit='c') # Change c to f for Fahrenheit

        location = weather.lookup_by_location(location_name)
        condition = location.condition

        print "Weather in " + location.location.city + ", " + location.location.country
        print "The condition is " + condition.text
        print "The temperature is " + condition.temp + " C"

        highs = []
        lows = []
        dates = []

        for forecast in location.forecast:
            highs.append(int(forecast.high))
            lows.append(int(forecast.low))
            dates.append(str(forecast.date))

        # Uncomment for debugging:
        # print highs
        # print lows
        # print dates

        plt.plot(dates, highs, color='red', label='High')
        plt.plot(dates, lows, color='blue', label='Low')
        plt.legend()
        plt.title("Weather Forecast for " + location_name)
        plt.ylabel("Temperature in Celsius")
        plt.show()

get_weather('St. Louis')

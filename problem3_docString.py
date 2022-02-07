import math
def convert(T, V):
    """compute the wind chill temperature
     wind chill : math:'T_{WC}', is based on air Temp T and wind speed V"""
    windChill = (math.sqrt(100*V) + 10.45 - V)*(33 - T)
    return windChill

print(convert(5,10))
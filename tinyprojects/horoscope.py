import pyaztro
import requests

def Horoscope():
    sign = input("sign: ")
    day = input("Day: ")
    params = (
        ('sign', sign),
        ('day', day)
    )
    url = "https://aztro.sameerkumar.website/"
    response = requests.post(url, params=params).json()
    print(response)
    
Horoscope()
    
    

# Fichier qui permet de simplifier l'acquisition des données des différents capteurs

from pycoproc_1 import *
from LIS2HH12 import LIS2HH12
from SI7006A20 import SI7006A20
from LTR329ALS01 import LTR329ALS01
from MPL3115A2 import MPL3115A2,ALTITUDE,PRESSURE

# initialisation des capteurs
py = Pycoproc(Pycoproc.PYSENSE)

#-----------------------------------------------------------------------
# ===== Capteur MPL3115A2 =====

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!! Ce capteur obtient sa propre température rendant la mesure inutilisable !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def temperature():
    alt = MPL3115A2(py,mode=ALTITUDE)
    temperature_data = str("{0:.1f}".format((alt.temperature())))
    return temperature_data

def altitude():
    alt = MPL3115A2(py,mode=ALTITUDE)
    altitude_data = str("{0:.1f}".format((alt.altitude()))) # Returns height in meters
    return altitude_data

def pression():
    press = MPL3115A2(py,mode=PRESSURE)
    pression_data = str("{0:.1f}".format((press.pressure()))) # Returns pressure in Pa
    return pression_data

#-----------------------------------------------------------------------
# ===== Capteur SI7006A20 =====

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!! Ce capteur obtient sa propre température rendant la mesure inutilisable !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# def temperature():
#     dht = SI7006A20(py)
#     temperature_data = str("{0:.1f}".format((dht.temperature())))
#     return temperature_data

def humidity():
    dht = SI7006A20(py)
    humidity_data = str("{0:.1f}".format((dht.humidity())))
    return humidity_data

def dew_point():
    dht = SI7006A20(py)
    dew_point_data = str("{0:.1f}".format((dht.humidity())))
    return dew_point_data

#-----------------------------------------------------------------------
# ===== Capteur LTR329ALS01 =====

def lux():
    li = LTR329ALS01(py)
    lumiere = (li.light())
    lux_data = str(lumiere[0]) # Read the light levels of light sensor.
    return lux_data

#-----------------------------------------------------------------------
# ===== Capteur LIS2HH12 =====

def acceleration():
    acc = LIS2HH12(py)
    acceleration_data = str(acc.acceleration()) # Read the acceleration from the accelerometer. Returns a tuple with the 3 values of acceleration in g-force: (x, y, z).
    return acceleration_data

def roll():
    acc = LIS2HH12(py)
    roll_data = str(acc.roll()) # Read the current roll from the accelerometer. Returns a float in degrees in the range -180 to 180.
    return roll_data

def pitch():
    acc = LIS2HH12(py)
    pitch_data = str(acc.pitch()) # Read the current pitch from the accelerometer. Returns a float in degrees in the range -90 to 90. 
    return pitch_data

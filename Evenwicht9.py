from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor
from spike import App, DistanceSensor, Motor, MotorPair, Speaker, ColorSensor
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

hub = PrimeHub()

hub.light_matrix.show_image('HAPPY')
motorA = Motor('A')

def evenwicht9(Delta, Snelheid,Richting):
    Snelheid = abs(Snelheid)
    klaar = 1
    Soll = 0
    SollMax = Soll+Delta
    SollMin = Soll-Delta
    while klaar==1:
        Ist = hub.motion_sensor.get_roll_angle()
        if Ist < SollMin or Ist > SollMax: 
            if Ist>SollMax:
                motorA.start(-1*Snelheid*Richting)
            if Ist<SollMin:
                motorA.start( 1*Snelheid*Richting)
        else:
            motorA.stop()
#============================================ RUN
k = 1
while k==1:
    evenwicht9(2,50,1)

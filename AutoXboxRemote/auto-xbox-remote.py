from pybricks.hubs import TechnicHub
from pybricks.iodevices import XboxController
from pybricks.pupdevices import DCMotor
from pybricks.parameters import Port
from pybricks.tools import wait

hub = TechnicHub()
motor = DCMotor(Port.A) 

motor.dc(100)
wait(1000)
motor.dc(-100)
wait(1000)
motor.dc(0)

pad = XboxController()  # start pairing: zie stappen hieronder

# XboxController, De Knoppen RT en LT geven een waarde van 0-100 afhankelijk hoe hard je ze indrukt


def throttle(): # geeft een waarde tussen -100 en +100
    lt, rt = pad.triggers()        # 0..100 %
    return max(-100, min(100, rt - lt))  # vooruit = RT, achteruit = LT

while True:
    motor.dc(throttle())
    wait(20)

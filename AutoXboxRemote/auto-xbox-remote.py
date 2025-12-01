from pybricks.hubs import TechnicHub
from pybricks.iodevices import XboxController
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Button, Stop
from pybricks.tools import wait

hub = TechnicHub()
motorGroot = Motor(Port.D)

pad = XboxController()

MAX_SPEED = 1000        # deg/s
STEP = 20               # stapgrootte per loop als D-pad wordt vastgehouden

# offset die je met de D-pad langzaam omhoog/omlaag “sleurt”
offset_speed = 0


def clamp(value, lo, hi):
    return max(lo, min(hi, value))


# korte test om de motor/poort te checken
motorGroot.run_time(300, 300, wait=True)
motorGroot.stop()

while True:
    # 0..100 voor LT (links) en RT (rechts)
    lt, rt = pad.triggers()
    if lt > 8 or rt > 8:
        offset_speed = 0

    # basis-snelheid vanuit de triggers (rt vooruit, lt achteruit)
    trigger_speed = int((rt - lt) * MAX_SPEED / 100)

    # ingedrukte knoppen ophalen
    pressed = pad.buttons.pressed()

    # D-pad UP ingedrukt → offset loopt steeds op
    if Button.UP in pressed:
        offset_speed += STEP

    # D-pad DOWN ingedrukt → offset loopt steeds af
    if Button.DOWN in pressed:
        offset_speed -= STEP

    # Y = reset + vrij uitrollen
    if Button.Y in pressed:
        offset_speed = 0
        motorGroot.stop()

    # offset begrenzen zodat we nooit buiten bereik komen
    offset_speed = clamp(offset_speed, -MAX_SPEED, MAX_SPEED)

    # totale snelheid = triggers + offset
    drive_speed = clamp(trigger_speed + offset_speed, -MAX_SPEED, MAX_SPEED)

    # motor draaien
    motorGroot.run(drive_speed)

    # kleine delay, bepaalt ook hoe “snel” de D-pad accelereert
    wait(20)

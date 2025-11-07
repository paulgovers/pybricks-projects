from pybricks.hubs import TechnicHub
from pybricks.iodevices import XboxController
from pybricks.pupdevices import DCMotor, Motor
from pybricks.parameters import Port
from pybricks.tools import wait

hub = TechnicHub()
motor = DCMotor(Port.A)          # aandrijving
motorGroot = Motor(Port.D)       # sturen (tacho-motor)

pad = XboxController()           # pairen: controller aan, pair-knop vasthouden, dan script starten

def throttle():
    lt, rt = pad.triggers()      # 0..100
    return max(-100, min(100, rt - lt))

def steering():
    x, y = pad.joystick_right()  # -100..100 (horizontaal, verticaal)
    # kleine deadzone tegen jitter
    return 0 if -8 < x < 8 else x

# optioneel: korte test van motoren
motor.dc(100); wait(300); motor.dc(0)
motorGroot.run_time(300, 300, wait=True)  # kleine tik, bewijst dat D-poort werkt
motorGroot.stop()

while True:
    motor.dc(throttle())
    # Motor.run verwacht deg/s; schaal joystickwaarde naar snelheid
    motorGroot.run(steering() * 30)
    wait(20)

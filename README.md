# pybricks-projects
Lego Pybricks projects

# besturing motor
Je hebt verschillende type lego motoren 
- simpele motor (zonder sensor) in pybricks bekend als DCMotor
- slimme (geavanceerde) motor in pybricks bekend als Motor

## slimme motor
Technic Large Angular Motor (21980) of Medium Angular Motor (45603)
- Heeft ingebouwde rotatiesensor (encoder).
- Kan snelheid en positie regelen.
- Kan actief remmen of een hoek aanhouden.
- Kan met nauwkeurige PID-regeling werken.
```
from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

motor = Motor(Port.A)

motor.run(500)           # draait met 500°/s
wait(2000)
motor.stop()             # stopt (met rem)
motor.run_target(500, 90)  # draait precies naar 90°
```

## simpele motor
```
from pybricks.pupdevices import DCMotor
motor = DCMotor(Port.A) 
motor.dc(100)   # volledige aan vooruit
motor.dc(-50)   # halve kracht achteruit
motor.dc(0)    # uit
```
"""
Pybricks code voor LEGO Technic Hub (88012) met DC motor

Dit programma demonstreert basis DC motor besturing met de Technic Hub.
"""

from pybricks.hubs import TechnicHub
from pybricks.pupdevices import DCMotor
from pybricks.parameters import Port, Direction
from pybricks.tools import wait

# Initialiseer de Technic Hub
hub = TechnicHub()

# Initialiseer de DC motor op poort A
# Pas de poort aan indien de motor op een andere poort is aangesloten
motor = DCMotor(Port.A)

# Voorbeeldprogramma: Motor besturing
print("Start DC motor programma")

# Zet motor aan met 50% snelheid (positieve waarde = vooruit)
print("Motor draait vooruit op 50% snelheid")
motor.dc(50)
wait(2000)  # Wacht 2 seconden

# Zet motor aan met 100% snelheid (maximale snelheid vooruit)
print("Motor draait vooruit op 100% snelheid")
motor.dc(100)
wait(2000)  # Wacht 2 seconden

# Stop de motor
print("Motor stopt")
motor.dc(0)
wait(1000)  # Wacht 1 seconde

# Zet motor aan met -50% snelheid (negatieve waarde = achteruit)
print("Motor draait achteruit op 50% snelheid")
motor.dc(-50)
wait(2000)  # Wacht 2 seconden

# Stop de motor
print("Motor stopt")
motor.dc(0)
wait(1000)  # Wacht 1 seconde

# Rem de motor actief
print("Motor remt actief")
motor.brake()

print("Programma voltooid")

# Laat de hub een geluid maken om te bevestigen dat het programma klaar is
hub.light.on()

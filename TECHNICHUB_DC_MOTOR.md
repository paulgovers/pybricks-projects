# Pybricks Project - LEGO Technic Hub met DC Motor

## Hardware vereisten
- **Hub**: LEGO Technic Hub (88012)
- **Motor**: DC motor (aangesloten op poort A)

## Over dit project
Dit project bevat Pybricks code voor het besturen van een DC motor met de LEGO Technic Hub.

## Installatie en gebruik

### Vereisten
1. LEGO Technic Hub (88012)
2. Een DC motor
3. Pybricks firmware geïnstalleerd op de hub
4. Pybricks Code editor (https://code.pybricks.com/) of Visual Studio Code met Pybricks extensie

### Stappen
1. Sluit de DC motor aan op poort A van de Technic Hub
2. Open het `main.py` bestand in Pybricks Code
3. Verbind met de hub via Bluetooth
4. Upload en run het programma

## Code overzicht

Het programma demonstreert de volgende functionaliteiten:
- Motor vooruit laten draaien met verschillende snelheden (50% en 100%)
- Motor achteruit laten draaien (negatieve snelheid)
- Motor stoppen
- Motor actief remmen

## Motor besturing

De DC motor wordt bestuurd met de `motor.dc()` methode:
- `motor.dc(50)` - Motor draait vooruit op 50% snelheid
- `motor.dc(100)` - Motor draait vooruit op maximale snelheid
- `motor.dc(-50)` - Motor draait achteruit op 50% snelheid
- `motor.dc(0)` - Motor stopt
- `motor.brake()` - Motor remt actief

## Aanpassingen

### Andere poort gebruiken
Als je de motor op een andere poort hebt aangesloten, wijzig dan:
```python
motor = DCMotor(Port.A)  # Verander A naar B, C, of D
```

### Snelheid aanpassen
De snelheid kan worden ingesteld tussen -100 en 100:
- `-100` tot `-1`: Achteruit (variabele snelheid)
- `0`: Stop
- `1` tot `100`: Vooruit (variabele snelheid)

## Documentatie
Voor meer informatie over Pybricks en de beschikbare functies:
- [Pybricks Documentatie](https://docs.pybricks.com/)
- [Technic Hub API](https://docs.pybricks.com/en/latest/hubs/technichub.html)
- [DC Motor API](https://docs.pybricks.com/en/latest/pupdevices/dcmotor.html)

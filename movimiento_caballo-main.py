# Imports go at the top
from microbit import *
from Maqueen import*
ma=Maqueen()
while True:
    if button_a.get_presses():
        ma.turn_right()
        sleep(190)
        ma.mover_celda() 
        ma.mover_celda() 
        ma.forward() 
        sleep(100)
        ma.motor_stop_all()
        
        

# Imports go at the top
from microbit import *
from Maqueen import*

ma=Maqueen()
ma.forward()
sleep(1000)
ma.turn_right()
sleep(410)
ma.mover_celda()
ma.turn_left()
sleep(410)
ma.forward()
sleep(1150)
ma.turn_left()
sleep(410)
ma.mover_celda()
ma.turn_right()
sleep(410)
ma.forward()
sleep(1500)
ma.motor_stop_all()

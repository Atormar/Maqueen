from microbit import*
from Maqueen import*

ma=Maqueen()
if button_a.get_presses():
    ma.mover_celda()
if button_b.get_presses():
    ma.mover_celda()
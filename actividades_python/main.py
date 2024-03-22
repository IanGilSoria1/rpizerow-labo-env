from gpiozero import LED, Button
from signal import pause

Rojo = LED(13)
boton = Button(18)

boton.when_pressed = Rojo.on
boton.when_released = Rojo.off

pause()

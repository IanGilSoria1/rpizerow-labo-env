from gpiozero import LED
from time import sleep

rojo = LED(13)
azul = LED(26)
verde = LED(19)

while True:
	rojo.on()
	sleep(1)
	rojo.off()
	azul.on()
	sleep(0.5)
	azul.off()
	verde.on()
	sleep(0.25)
	verde.off()

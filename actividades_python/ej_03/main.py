from gpiozero import LED, Buzzer
from signal import pause

bz = Buzzer(22)
led_rojo = LED(19)
led_verde = LED(26)
led_azul = LED(13)
while True:
	comando = input("Se ingresa las ordenes de buzz/rgb: ")
	if comando == "rgb":
		opcion = input("Se diferencian entre cada LED")
	elif comando == "buzz":
		opcion = input("Selecciona El encendido/apagado")		

	if comando == "buzz":
		if opcion == "on":
			bz.on()
		elif opcion == "off":
			bz.off()

	elif comando == "rgb":
		if opcion == "red":
			led_rojo.toggle()
		elif opcion == "green":
			led_verde.toggle()
		elif opcion == "blue":
			led_azul.toggle()			

pause()


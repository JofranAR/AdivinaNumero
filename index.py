import random
intentosRealizados = 0
nombre = input("Como te llamas? -")
numero = random.randint(1,20)
print(f"Bueno {nombre} estoy pensando en un numero del 1 al 20")
while intentosRealizados < 6:
	print("Intenta adivinar")
	estimacion = int(input("<<"))
	intentosRealizados += 1
	if estimacion < numero:
		print("Tu estimacion es muy baja")
	if estimacion > numero:
		print("Tu estimacion es muy alta")
	if estimacion == numero:
		break
if estimacion == numero:
	print(f"Buen trabajo {nombre} has adivinado el numero: {numero} en {intentosRealizados} intentos!")
	if estimacion != numero:
		print("El numero que estaba pensando era el {numero}")
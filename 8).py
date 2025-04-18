#Realice un programa que permita a un usuario ingresar un determinado año. Deberá
#imprimirse por pantalla si dicho año es bisiesto o no.
#Observación: Para saber si un año es bisiesto se divide entre 4, si la división es exacta
#entonces es bisiesto. Sin embargo, hay que tener cuidado con esta regla, ya que si el
#año también es divisible entre 100 ya no será bisiesto. La excepción a la regla anterior
#se da cuando el año es divisible entre 400.

año = int(input("Ingrese un año"))
resultado = año / 4
if resultado.is_integer():
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")
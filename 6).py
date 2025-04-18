#Las dos raíces de la ecuación cuadrática “𝑎𝑥2 + 𝑏𝑥 + 𝑐 = 0” pueden ser obtenidas
#usando la siguiente formula
#La expresión “(𝑏2 − 4𝑎𝑐)” es llamada discriminante de la ecuación cuadrática:
#- Si es positiva, la ecuación tiene 2 raíces reales
#- Si es “0”, la ecuación tiene una raíz
#- Si es negativo, la ecuación no tiene raíces reales.
#Escriba un programa donde el usuario ingrese los valores de “a”, “b” y “c” y muestre el
#resultado de la discriminante:
#- Si el discriminante es positivo, debe mostrar las 2 raíces
#- Si el discriminante es cero, debe mostrar la raíz.
#- De otro modo, muestre el mensaje: “La ecuación no tiene raíces reales"

print("Ingrese valores constantes de una ecuacion cuadratica para calcular su discriminante y mostrar sus raices")
a = int(input("Ingrese el valor a") )
b = int(input("Ingrese el valor b") )
c = int(input("Ingrese el valor c") )

discriminante = (b ** 2) - 4 * a * c
raiz_1 = ( - b - pow(discriminante,0.5) )/ 2 * a
raiz_2 = ( - b + pow(discriminante,0.5) )/ 2 * a

if discriminante > 0:
    print("La ecuación tiene 2 raíces reales")
    print(f"Las 2 raices de la ecuacion cuadratica son: {raiz_1} o {raiz_2}")

if discriminante == 0:
    print("La ecuación tiene una raíz")
    print(f"La raiz de la ecuación cuadratica es: {raiz_1}")

if discriminante < 0:
    print("La ecuación no tiene raíces reales")

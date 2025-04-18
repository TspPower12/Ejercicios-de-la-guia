#Escriba un programa solicite pida tres números y que muestre un mensaje indicando si
#los tres son iguales, si hay dos iguales o si son los tres distintos. Los mensajes serían:
#“Ha escrito tres veces el mismo número”, “Ha escrito un número dos veces”, “Los tres
#números son distintos” respectivamente

n1 = int(input("Ingrese un primer número"))
n2 = int(input("Ingrese un segundo número"))
n3 = int(input("Ingrese un tercer número"))

if n1 == n2 == n3:
    print("Ha escrito tres veces el mismo número")
elif n1 == n2 or n1 == n3 or n2 == n3:
    print("Ha escrito un número dos veces")
elif n1 != n2 != n3:
    print("Los tres números son distintos")
    
#Escriba un programa que solicite dos números enteros y calcule su división, mostrando 
#si la división es exacta o no. Debe tener en cuenta que no se puede dividir entre cero

n1 = int(input("Ingrese el primer numero"))
n2 = int(input("Ingrese el segundo numero"))

division = n1/n2
residuo = n1%n2

if n2 == 0:
    print("No se puede dividir por cero")

else:
    if residuo == 0:
        print("Division exacta")
    else:
        print("Division inexacta")
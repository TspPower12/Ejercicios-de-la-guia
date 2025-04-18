#Una tienda ha puesto en oferta la venta al por mayor de cierto producto, ofreciendo un
#descuento del 15% por la compra de más de 3 docenas y 10% en caso contrario. Los
#clientes que compren más de 3 docenas reciben como obsequio una unidad del producto
#por cada docena adicional. Diseñe un programa que determine el monto de la compra,
#el monto del descuento, el monto a pagar y el número de unidades de obsequio por la
#compra de cierta cantidad de docenas del producto

producto = "paquete de sal"
cantidad_docena = int(input("Ingrese la cantidad de docenas que desea comprar"))
cantidad_unidad = int(input("Ingrese la cantidad de unidades que desea comprar"))
costo_docena = float(input("Ingrese el costo por docena"))
costo_unidad = float(input("Ingrese el costo por unidad"))
monto_compra = (cantidad_docena * costo_docena) + (cantidad_unidad * costo_unidad)

if cantidad_docena <= 3:
    descuento = 10
    monto_total = monto_compra * (100 - descuento)/100
    cantidad_total = int((12 * cantidad_docena) + cantidad_unidad) 
    print(f"Usted esta comprando {cantidad_total} unidades de {producto}")
    print(f"El monto a pagar con descuento incluido es s/ {monto_total:.2f} soles")
    

elif cantidad_docena > 3:
   obsequio = cantidad_docena - 3
   descuento = 15
   monto_total = monto_compra * ( 100 - descuento )/100
   cantidad_total = int(( 12 * cantidad_docena) + cantidad_unidad + obsequio)
   print(f"Usted esta comprando {cantidad_total} unidades de {producto}")
   print(f"El monto a pagar con descuento incluido es s/ {monto_total:.2f} soles")
   
   

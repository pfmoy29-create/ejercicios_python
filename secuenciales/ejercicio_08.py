#Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, 
#el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por 
#las tres ventas que realiza en el mes y el total que recibirá en el mes tomando 
#en cuenta su sueldo base y comisiones.

sueldo_base = float(input("Dame el sueldo base :"))

venta_1 = ("Dime el precio de la venta :")
venta_2 = ("Dime el precio de la venta :")
venta_3 = ("Dime el precio de la venta :")

comision =(venta_1 * 0.1 + venta_2 * 0.1 + venta_3 * 0.1)

print("sueldo total :", sueldo_base + comision)
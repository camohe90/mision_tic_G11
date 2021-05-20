"""Una tienda ofrece un descuento del 15% sobre el total de la compra y un
cliente desea saber cuanto deberá pagar finalmente por su compra.."""

DESCUENTO = 0.15

total_compra = float(input("Ingrese el total de la compra: "))
descuento_compra = total_compra * DESCUENTO
total_pagar = total_compra - descuento_compra

print("El valor a pagar incluyendo el descuento es:", round(total_pagar, 2))
print(f"El valor a pagar incluyendo el descuento es: {total_pagar}")

print("¡Vegetales a la venta!")
print("Tomates - Unidad x 10$")
print("Cebollas - Unidad x 15$")
print("Pimentones - Unidad x 20$")

tom = int(input("¿Cuantos tomates llevará?: "))
ceb = int(input("¿Cuantos cebollas llevará?: "))
pim = int(input("¿Cuantos pimentones llevará?: "))

if tom > 0: 
    tom = tom * 10
    print("El costo de los tomates es: ", tom, "$")

if ceb > 0: 
    ceb = ceb * 15
    print("El costo de las cebollas es: ", ceb, "$")

if pim > 0: 
    pim = pim * 20
    print("El costo de los pimentones es: ", pim, "$")


total = tom + ceb + pim 

if total > 100: 
    print ("Total con descuento es: ")
    total = total - (total *0.10)
    print (total)
else: 
    print("El total neto es: ", total)
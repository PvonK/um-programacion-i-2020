"""
Ejercicio 2
La   pizzería   Bella   Napoli   ofrece   pizzas   vegetarianas   y   no   vegetarianas   a   sus   clientes.   Los
ingredientes para cada tipo de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu. 

Ingredientes no vegetarianos: Peperoni, Jamón y Salmón. 
Escribir   un   programa   que   pregunte   al   usuario   si   quiere   una   pizza   vegetariana   o   no,   y   en
función de su respuesta le muestre un menú con los ingredientes disponibles para que elija.
Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la
pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los
ingredientes que lleva
"""

vegetariano = input("quere una pizza vegetariana? s/n")
print("eliga un ingrediente: ")

if vegetariano == "s":
    print("Pimiento")
    print("Tofu")
    pizza = "es vegetariana"

else:
    print("Peperoni")
    print("Jamón")
    print("Salmón")
    pizza = "no es vegetariana"

ingrediente = input("")

print("\nSu pizza " + pizza + " y lleva los siguentes ingredientes:")
print("Mozzarella")
print("Tomate")
print(ingrediente)

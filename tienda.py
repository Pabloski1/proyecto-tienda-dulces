print("¡Bienvenido a Dulce Tentación! \n"
    "Aquí tiene un listado de categorías de nuestros productos: \n"
    "1. Dulces.\n"
    "2. Salados.\n"
    "3. Helados.\n"
    "4. Colaciones.")

productos = {
    "Dulces": {"Alfajor": 800, "Galletas": 1000, "Chocolates": 1500},
    "Salados": {"Papas fritas": 1000, "Maní": 800, "Ramitas": 900},
    "Helados": {"Centella": 300, "Trululú": 600, "Danky": 1000},
    "Colaciones": {"Empanada": 1800, "Tapaditos": 1000, "Cereales": 800}
}

categorias = list(productos.keys())
carrito = {}

while True:
    categoria = int(input("¿Que categoría quiere comprar? (Ingrese el número correspondiente): "))
    if 1 <= categoria <= len(categorias):
        categoria = categorias[categoria - 1]
        print(f"Estos son los productos disponibles en {categoria}")
        productos_categoria = productos[categoria]
        producto_num = 1
        for producto, precio in productos_categoria.items():
            print(f"{producto_num}. {producto}: ${precio}")
            producto_num += 1
        
        while True:
            seleccion_producto = int(input("¿Qué producto desea agregar al carrito? (Ingrese el número correspondiente): "))
            if 1 <= seleccion_producto <= len(productos_categoria):
                producto_seleccionado = list(productos_categoria.keys())[seleccion_producto - 1]
                cantidad = int(input(f"Ingrese la cantidad de {producto_seleccionado}: "))
                carrito[producto_seleccionado] = cantidad
                print(f"{cantidad} {producto_seleccionado} fue agregado al carrito.")
            else:
                print("Producto no válido. Inténtelo nuevamente")
                continue
            
            otro_producto = input("¿Desea agregar otro producto de esta categoría a su carrito? (Si/No): ").lower()
            if otro_producto == "no":
                break
        otra_categoria = input("¿Desea seleccionar otra categoría? (Si/No): ").lower()
        if otra_categoria == "no":
            break
    else:
        print("La categoria no es valida. Vuelva a intentarlo.")

total_productos = sum(carrito.values())

descuento = 0
for categoria in productos:
    productos_en_categoria = productos[categoria]
    contador_productos = 0

for producto in carrito:
    if producto in productos_en_categoria:
        contador_productos += 1

if contador_productos >= 10:
    descuento += 0.1
if sum(carrito.values()) >= 5:
    descuento += 0.02

todos_los_productos = set()
for categoria in productos:
    productos_categoria = productos[categoria]
    for producto in productos_categoria:
        todos_los_productos.add(producto)

if todos_los_productos == set(carrito.keys()):
    descuento_categorias = 0.05
else:
    descuento_categorias = 0

nombre = input("Ingrese su nombre: ")
direccion = input("Ingrese su dirección: ")
forma_de_pago = input("Ingrese su forma de pago (Tarjeta de credito, Tarjeta de debito o Transferencia bancaria): ")

descuento_pago = 0
if forma_de_pago == "Tarjeta de debito":
    descuento_pago = 0.02
    descuento += descuento_pago
elif forma_de_pago == "Transferencia bancaria":
    print("Por su forma de pago, ¡tiene envió gratis a su domicilio!")

total = 0

print("***********FACTURA***********\n"
    f"Cliente: {nombre}\n"
    f"Dirección: {direccion}\n"
    f"Forma de pago: {forma_de_pago}\n"
    "Detalle de compra: \n")
for producto, cantidad in carrito.items():
    for categoria, productos_categoria in productos.items():
        if producto in productos_categoria:
            precio_unitario = productos_categoria[producto]
            subtotal = precio_unitario * cantidad
            total += subtotal
            print(f"- Producto: {producto}\n"
            f"  Cantidad: {cantidad}\n"
            f"  Precio unitario: ${precio_unitario}\n"
            f"  Subtotal: ${subtotal}\n"
            "-----------------------------\n")

print("Descuento aplicados: \n"
    f"- Descuentos por cantidad de la misma categoría: ${total * descuento}\n"
    f"- Descuentos por comprar en todas las categorías: ${total * descuento_categorias}\n"
    f"- Descuentos por pago con {forma_de_pago}: ${total * descuento_pago}\n"
    )
total_descuentos = total * (descuento + descuento_categorias + descuento_pago)
total_final = total - total_descuentos
print(f"Total a pagar: ${total_final}\n"
    "***************************************")

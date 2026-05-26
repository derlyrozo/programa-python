# Matriz de inventario: [Código, Nombre, Stock Actual, Stock Mínimo]
inventario = [
    ["A001", "Papel resma",       15,  20],
    ["A002", "Bolígrafos caja",    8,   5],
    ["A003", "Tóner impresora",    2,  10],
    ["A004", "Carpetas",          30,  25],
    ["A005", "Grapadora",          0,   3],
]

def cantidad_a_pedir(stock_actual, stock_minimo):
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    return 0

print("=" * 40)
print("     AUDITORÍA DE INVENTARIO")
print("=" * 40)
print(f"{'Artículo':<20} {'Pedir':>8}")
print("-" * 40)

hay_pedidos = False
for codigo, nombre, stock_actual, stock_minimo in inventario:
    cantidad = cantidad_a_pedir(stock_actual, stock_minimo)
    if cantidad > 0:
        print(f"{nombre:<20} {cantidad:>8} unidades")
        hay_pedidos = True

if not hay_pedidos:
    print("  Todo el inventario está al día.")

print("=" * 40)

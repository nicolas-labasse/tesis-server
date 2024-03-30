valorMaximo = 10

TotalProductos = [
    {"nombre": "Producto 1", "precio": 20},
    {"nombre": "Producto 2", "precio": 30},
    {"nombre": "Producto 3", "precio": 40}
]



def CalcularTotalProductos(TotalProductos):
  valorTotalProductos = 0
  for Productos in TotalProductos:
    valorTotalProductos += Productos.precio

  print(valorTotalProductos)
  return valorTotalProductos

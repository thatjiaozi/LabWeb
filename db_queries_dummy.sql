-- SELECT Generales para mostrar informacion de tablas

SELECT * FROM Productos;

SELECT * FROM Ventas;

SELECT * FROM Administradores;

SELECT * FROM Empleados;

SELECT * FROM VentaProductos;

-- Query para obtener detalles de un Producto

SELECT Descripcion 
FROM Productos
WHERE Productos.IDProducto = '1';

-- Queries para obtener nombres de todos los productos de acuerdo ciertos filtros

-- Por categoria
SELECT Nombre
FROM Productos
WHERE Productos.Categoria IN ('Cocina');

-- Por rango de precio
SELECT Nombre
FROM Productos
WHERE Productos.Precio 
BETWEEN 50 AND 250;

-- Por cantidad de existencia
SELECT Nombre
FROM Productos
WHERE Productos.CantidadExistencia >= 10;

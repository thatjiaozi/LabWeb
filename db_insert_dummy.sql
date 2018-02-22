USE ProyectoWeb;

-- Productos
INSERT INTO Productos(IDProducto, Nombre, Descripcion, Categoria, CantidadExistencia, Precio) 
VALUES (1, "Tupper", "Es un tupper chido", "Cocina", 10, 100);

INSERT INTO Productos(IDProducto, Nombre, Descripcion, Categoria, CantidadExistencia, Precio) 
VALUES (2, "Plato", "Es un plato chido", "Cocina", 5, 50);

-- Ventas
INSERT INTO Ventas(IDVenta, PagoTotal, Fecha) 
VALUES(100, 200, '2018-02-21'); 

-- Administradores
INSERT INTO Administradores(IDAdministrador, NombreCompleto, PasswordHash) 
VALUES(1000, "Jefferson Gutierritos", "Password"); 

-- Empleados
INSERT INTO Empleados(IDEmpleado, IDAdministrador, NombreCompleto, PasswordHash) 
VALUES(200, 1000, "Carlos Santana", "Password");

-- VentaProductos
INSERT INTO VentaProductos(IDProducto, IDVenta, Cantidad) 
VALUES(001, 100, 2);

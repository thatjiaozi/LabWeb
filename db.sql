CREATE DATABASE Proyecto;
USE Proyecto;
 
CREATE TABLE Productos(
    IDProducto VARCHAR(40) NOT NULL,
    CantidadExistencia INT NOT NULL,
    PRIMARY KEY (IDProducto)
);
 
CREATE TABLE Ventas(
    IDVenta VARCHAR(40) NOT NULL,
    IDCliente VARCHAR(40) NOT NULL,
    PagoTotal FLOAT(10, 2) NOT NULL,
    Fecha DATE NOT NULL,
    PRIMARY KEY (IDVenta)
    FOREIGN KEY(IDCliente) REFERENCES Clientes(IDCliente)
);
 
 
CREATE TABLE Empleados(
    IDEmpleado VARCHAR(40) NOT NULL,
    IDAdministrador VARCHAR(40) NOT NULL,
    NombreCompleto VARCHAR(40) NOT NULL,
    PasswordHash VARCHAR(40) NOT NULL,
    PRIMARY KEY(IDEmpleado),
    FOREIGN KEY(IDAdministrador) REFERENCES Administradores(IDAdministrador)
);
 
CREATE TABLE Administradores(
    IDAdministrador VARCHAR(40) NOT NULL,
    NombreCompleto VARCHAR(40) NOT NULL,
    PasswordHash VARCHAR(40) NOT NULL,
    PRIMARY KEY(IDAdministrador)
);
 
CREATE TABLE VentaProductos(
    IDAuto INT NOT NULL AUTO_INCREMENT NOT NULL,
    IDProducto VARCHAR(40) NOT NULL,
    IDVenta VARCHAR(40) NOT NULL,
    Cantidad INT NOT NULL,
    PRIMARY KEY(IDAuto),
    FOREIGN KEY(IDProducto) REFERENCES Productos(IDProducto),
    FOREIGN KEY(IDVenta) REFERENCES Ventas(IDVenta)
);
 

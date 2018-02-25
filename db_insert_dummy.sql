-- -------------------------------------------------------------------------------
/* 	PRODUCTS 
	INSERT INTO Products(IDProduct, ProductName, Description, Price, Quantity) */
INSERT INTO Products VALUES(1, "Paquete vasos", "Paquete de 5 vasos de hielo seco", 50, 100);
INSERT INTO Products VALUES(2, "Tupper", "Tupper de plástico", 100, 30);
INSERT INTO Products VALUES(3, "Tina", "Tina infantil de 90 cm x 60 cm", 450, 10);
-- -------------------------------------------------------------------------------

-- -------------------------------------------------------------------------------
/* 	CATEGORIES 
	INSERT INTO Categories(IDCategory, CategoryName) */
INSERT INTO Categories VALUES(1, "Cocina");
INSERT INTO Categories VALUES(2, "Juguetes");
INSERT INTO Categories VALUES(3, "Hogar");
INSERT INTO Categories VALUES(4, "Artículos escolares");
-- -------------------------------------------------------------------------------

-- -------------------------------------------------------------------------------
/* 	SALES 
	INSERT INTO Sales(IDSale, TotalPayment, SaleDate) */
INSERT INTO Sales VALUES(1, 100, '2018-02-21'); 
INSERT INTO Sales VALUES(2, 200, '2018-02-23');
INSERT INTO Sales VALUES(3, 600, '2018-02-25');
-- -------------------------------------------------------------------------------

-- -------------------------------------------------------------------------------
/* 	PRODUCTS_CATEGORIES 
	INSERT INTO Products_Categories(IDAuto, IDProduct, IDCategory)*/
INSERT INTO Products_Categories VALUES(DEFAULT, 1, 1);
INSERT INTO Products_Categories VALUES(DEFAULT, 2, 1);
INSERT INTO Products_Categories VALUES(DEFAULT, 2, 2);
INSERT INTO Products_Categories VALUES(DEFAULT, 3, 2);
INSERT INTO Products_Categories VALUES(DEFAULT, 3, 3);
-- -------------------------------------------------------------------------------

-- -------------------------------------------------------------------------------
/* 	SALES_PRODUCTS 
	INSERT INTO Sales_Products(IDAuto, IDSale, IDProduct, Quantity) */
INSERT INTO Sales_Products VALUES(DEFAULT, 1, 1, 2);
INSERT INTO Sales_Products VALUES(DEFAULT, 2, 2, 2);
INSERT INTO Sales_Products VALUES(DEFAULT, 3, 1, 1);
INSERT INTO Sales_Products VALUES(DEFAULT, 3, 2, 1);
INSERT INTO Sales_Products VALUES(DEFAULT, 3, 3, 1);
-- -------------------------------------------------------------------------------

---------------------------------------------------------------------------------
/* 	ADMINISTRATORS 
	INSERT INTO Administrators(IDAdmin, Name, PasswordHash) */
INSERT INTO Administrators VALUES(1, "Jefferson Gutierritos", "lala");
INSERT INTO Administrators VALUES(2, "Watts Humphrey", "PSP"); 
-- -------------------------------------------------------------------------------

-- -------------------------------------------------------------------------------
/* 	EMPLOYEES 
	INSERT INTO Employees(IDEmployee, IDAdmin, Name, PasswordHash) */
INSERT INTO Employees VALUES(1, 1, "Carlos Santana", "lolo");
INSERT INTO Employees VALUES(2, 2, "Pepe el Toro", "123");
-- -------------------------------------------------------------------------------
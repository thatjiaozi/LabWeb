-- Check the content of tables
SELECT * FROM Products;
SELECT * FROM Categories;
SELECT * FROM Sales;
SELECT * FROM Products_Categories;
SELECT * FROM Sales_Products;
SELECT * FROM Administrators;
SELECT * FROM Employees;

/*  FILTER QUERIES 
	These queries obtain details about products (name, description, etc)
	based on certain filter criteria */

-- Obtain name of all existent products
SELECT ProductName 
FROM Products;

-- Obtain description of a specific product given an ID
SELECT Description 
FROM Products
WHERE Products.IDProduct = 1;

-- Obtain names of products that comply certain categories criteria
SELECT P.ProductName
FROM Products P, Categories C, Products_Categories CP
WHERE P.IDProduct = CP.IDProduct
AND C.IDCategory = CP.IDCategory
AND C.CategoryName IN ("Juguetes", "Hogar")
GROUP BY P.ProductName
HAVING COUNT(CP.IDCategory) >= 2; 

-- Obtains names of products which are in a range of price
SELECT ProductName
FROM Products
WHERE Products.Price
BETWEEN 0 AND 500;

-- Obtains names of products which are in a range of quantity
SELECT ProductName 
FROM Products
WHERE Products.Quantity 
BETWEEN 0 AND 100;
-------------------------------------------------
SELECT customerID, date, description, amount, currency, status
FROM Transaction
INNER JOIN Customer
ON Transaction.customerID = Customer.customerID;
-------------------------------------------------
SELECT first_name, last_name, clubName
FROM Customer, Club
WHERE Customer.clubID = Club.clubID;
-------------------------------------------------
SELECT category_name
FROM Category
INNER JOIN Accounting_Module
ON Accounting_Module.moduleID = Category.moduleID;
-------------------------------------------------
SELECT bar_name
FROM Bar
INNER JOIN Accounting_Module
ON Accounting_Module.moduleID = Bar.moduleID;
-------------------------------------------------
SELECT transaction_type_name
FROM Transaction_Types
INNER JOIN Category
ON Category.moduleID = Transaction_Types.moduleID;
-------------------------------------------------
SELECT clubName, club_address, club_city
FROM Club
INNER JOIN Bank
ON Bank.bankID = Club.bankID;
-------------------------------------------------
SELECT first_name, last_name, bank_info, amount_available, clubName
FROM Customer, Transaction, Club
WHERE Transaction.customerID = Customer.customerID AND Transaction.clubID = Club.clubID
INNER JOIN Bank
ON Bank.bankID = Transaction.bankID;
-------------------------------------------------


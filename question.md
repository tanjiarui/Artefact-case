Test 1
======

In the database, there is a table of superheroes (table name superhero). Inside
this table, there are three columns; name, gender, and height.

**Superhero**

| Name (text type) | Gender (text type) | Height (numeric type) |
|------------------|--------------------|-----------------------|
| Arachne          | Female             | 175                   |
| Agent 13         | Female             | 173                   |
| Abin Sur         | Male               | 185                   |
| Absorbing Man    | Male               | 193                   |
| Adam Strange     | Male               | 185                   |
| Abe Sapien       | Male               | 191                   |

Please write a SQL query to find superheroes based on gender and height. If an
exact match cannot be found search for taller superheroes that have the same
gender and closest height. If more than one superheroes found rank them by name
in alphabetical order.

Sample
------

Input: Female, 173

Output: Agent 13

Input: Male, 192

Output: Absorbing Man

Input: Male, 183

Output: Abin Sur, Adam Strange

Test 2
======

Company X has a record of its customers, products, and orders. They need a
process to find the top 10 selling products for each country for each year. For
example, the 10 products that have the highest total sales quantity in France
for 2011.

1.  Write a program to read input files and output results to an output file.
    Instruction should be provided explaining how to run this program.

2.  Design the output file format. Write a description explaining how to read
    this file.

3.  Create your own test input and output for this process. Explain why your
    test data are created like that.

Input Schema
------------

**Customer**

| Name     | Type   | Description                |
|----------|--------|----------------------------|
| ID       | STRING | ID of the customer         |
| COUNTRY  | STRING | Country of this customer   |
| ORDER_ID | STRING | ID of the customer's order |

**Product**

| Name | Type   | Description         |
|------|--------|---------------------|
| ID   | STRING | ID of the product   |
| NAME | STRING | Name of the product |

**Orders**

| Name       | Type    | Description              |
|------------|---------|--------------------------|
| ID         | STRING  | ID of the order          |
| PRODUCT_ID | STRING  | ID of the product        |
| QUANTITY   | STRING  | Quantity of the purchase |
| ORDER_DATE | INTEGER | Date of the order        |

Sample Input
------------

**Customer**

| ID    | COUNTRY        | ORDER_ID |
|-------|----------------|----------|
| 17850 | United Kingdom | 536365   |
| 17850 | United Kingdom | 536366   |
| 12583 | France         | 536370   |

**Customer**

| ID     | NAME                               |
|--------|------------------------------------|
| 85123A | WHITE HANGING HEART T-LIGHT HOLDER |
| 71053  | WHITE METAL LANTERN                |
| 10002  | INFLATABLE POLITICAL GLOBE         |

**Orders**

| ID     | PRODUCT_ID | QUANTITY | ORDER_DATE |
|--------|------------|----------|------------|
| 536365 | 85123A     | 6        | 1-Dec-10   |
| 536365 | 71053      | 6        | 1-Dec-10   |
| 536370 | 22728      | 24       | 1-Dec-10   |
| 536370 | 10002      | 24       | 1-Dec-10   |
| 536371 | 22086      | 80       | 1-Dec-10   |

Sample Output
-------------

Please design your own output format.